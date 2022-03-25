from pysnmp.proto import rfc1902
from pysnmp.entity.rfc3413.oneliner import cmdgen


def snmp(action: str, cm_ip: str, community: str, oid: str, value: rfc1902):
    cmd_gen = cmdgen.CommandGenerator()

    if action == "get":
        errorIndication, errorStatus, errorIndex, varBinds = cmd_gen.getCmd(
            cmdgen.CommunityData(community),
            cmdgen.UdpTransportTarget((cm_ip, 161)),
            oid
        )
        for name, val in varBinds:
            return val.prettyPrint()

    elif action == "set":
        cmd_gen.setCmd(
            cmdgen.CommunityData(community),
            cmdgen.UdpTransportTarget((cm_ip, 161)),
            (oid, value)
        )

    elif action == "walk":
        errorIndication, errorStatus, errorIndex, varBindTable = cmd_gen.nextCmd(
            cmdgen.CommunityData(community),
            cmdgen.UdpTransportTarget((cm_ip, 161)),
            oid
        )
        data = ""
        for varBindRow in varBindTable:
            for name, val in varBindRow:
                data += name.prettyPrint() + "=" + val.prettyPrint() + "\n"
        return data


if __name__ == "__main__":
    snmp()
