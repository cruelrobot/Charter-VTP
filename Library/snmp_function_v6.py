from pysnmp.entity.rfc3413.oneliner import cmdgen


def snmp(action, cm_ipv6, community, oid, value):
    cmd_gen = cmdgen.CommandGenerator()

    if action == "get":
        errorIndication, errorStatus, errorIndex, varBinds = cmd_gen.getCmd(
            cmdgen.CommunityData(community),
            cmdgen.Udp6TransportTarget((cm_ipv6, 161)),
            oid
        )
        for name, val in varBinds:
            return val.prettyPrint()

    elif action == "set":
        cmd_gen.setCmd(
            cmdgen.CommunityData(community),
            cmdgen.Udp6TransportTarget((cm_ipv6, 161)),
            (oid, value)
        )

    elif action == "walk":
        errorIndication, errorStatus, errorIndex, varBindTable = cmd_gen.nextCmd(
            cmdgen.CommunityData(community),
            cmdgen.Udp6TransportTarget((cm_ipv6, 161)),
            oid
        )
        data = ""
        for varBindRow in varBindTable:
            for name, val in varBindRow:
                data += name.prettyPrint() + "=" + val.prettyPrint() + "\n"
        return data


if __name__ == "__main__":
    snmp()
