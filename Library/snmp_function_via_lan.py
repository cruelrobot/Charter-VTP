# Lan Device is the PC installed 2.5 Ethernet Card which IP is 172.21.2.118

import time
import paramiko


def snmpget(version: str, snmp_ip: str, oid: str):
    lan_pc_ip = '172.21.2.118'

    if version == "1":
        used_version = '1'
    elif version == "2":
        used_version = '2c'

    if snmp_ip.find(':') != -1:
        snmp_ip = 'udp6:[' + snmp_ip + ']'

    output = '\n=================================================================================\n'

    cnr = paramiko.SSHClient()
    cnr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cnr.connect(lan_pc_ip, port=22, username='UBEEi7', password='20040401')
    time.sleep(1)
    stdin, stdout, stderr = cnr.exec_command('snmpget -v' + used_version + ' -c private ' + snmp_ip + ' ' + oid + '\n')
    time.sleep(10)
    output += str(stdout.readlines()[0].rstrip())

    cnr.close()
    output += '\n=================================================================================\n'

    return output


def snmpwalk(version: str, snmp_ip: str, oid: str):
    lan_pc_ip = '172.21.2.118'

    if version == "1":
        used_version = '1'
    elif version == "2":
        used_version = '2c'

    if snmp_ip.find(':') != -1:
        snmp_ip = 'udp6:[' + snmp_ip + ']'

    output = '\n=================================================================================\n'

    cnr = paramiko.SSHClient()
    cnr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cnr.connect(lan_pc_ip, port=22, username='UBEEi7', password='20040401')
    time.sleep(1)
    stdin, stdout, stderr = cnr.exec_command('snmpwalk -v' + used_version + ' -c private ' + snmp_ip + ' ' + oid + '\n')
    time.sleep(10)
    stdout = stdout.readlines()
    for i in range(0, len(stdout)):
        output += str(stdout[i].rstrip())
        output += '\n'

    cnr.close()
    output += '\n=================================================================================\n'

    return output


def snmpset(version: str, snmp_ip: str, oid: str, parameter_type: str, value: str):
    lan_pc_ip = '172.21.2.118'

    if version == "1":
        used_version = '1'
    elif version == "2":
        used_version = '2c'

    if snmp_ip.find(':') != -1:
        snmp_ip = 'udp6:[' + snmp_ip + ']'

    output = '\n=================================================================================\n'

    cnr = paramiko.SSHClient()
    cnr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cnr.connect(lan_pc_ip, port=22, username='UBEEi7', password='20040401')
    time.sleep(1)
    stdin, stdout, stderr = cnr.exec_command('snmpset -v' + used_version + ' -c private ' + snmp_ip + ' ' + oid +
                                             ' ' + parameter_type + ' ' + value + '\n')
    time.sleep(10)
    stdout = stdout.readlines()
    for i in range(0, len(stdout)):
        output += str(stdout[i].rstrip())

    cnr.close()
    output += '\n=================================================================================\n'

    return output
