import time
import paramiko


def reserve(cm_mac: str, cm_ipv6: str):
    cnr_ip = '172.21.1.187'

    cnr = paramiko.SSHClient()
    cnr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cnr.connect(cnr_ip, port=22, username='CNRv7.2.3.2', password='20040401')
    cnr_connection = cnr.invoke_shell()
    time.sleep(1)
    cnr_connection.send(r'cd C:\Program Files (x86)\Network Registrar\Local\bin' + '\n')
    time.sleep(1)
    cnr_connection.send('nrcmd.bat -N admin -P 20040401\n')
    time.sleep(1)
    cnr_connection.send('reservation6 ' + cm_ipv6 + ' create 00:03:00:01:' + cm_mac + '\n')
    time.sleep(1)
    cnr_connection.send('save\n')
    time.sleep(1)
    cnr_connection.send('server dhcp reload\n')
    time.sleep(1)

    cnr_connection.close()


if __name__ == "__main__":
    reserve()
