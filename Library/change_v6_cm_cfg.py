import time
import paramiko


def configuration_file_change(cm_mac: str, policy_name: str):
    cnr_ip = '172.21.1.187'

    print('CM MAC: ' + cm_mac)
    print('Using Policy: ' + policy_name)
    cnr = paramiko.SSHClient()
    cnr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cnr.connect(cnr_ip, port=22, username='CNRv7.2.3.2', password='20040401')
    cnr_connection = cnr.invoke_shell()
    time.sleep(1)
    cnr_connection.send(r'cd C:\Program Files (x86)\Network Registrar\Local\bin' + '\n')
    time.sleep(1)
    cnr_connection.send('nrcmd.bat -N admin -P 20040401\n')
    time.sleep(1)
    cnr_connection.send('client 00:03:00:01:' + cm_mac + ' delete\n')
    time.sleep(1)
    cnr_connection.send('client 00:03:00:01:' + cm_mac + ' create\n')
    time.sleep(1)
    cnr_connection.send('client 00:03:00:01:' + cm_mac + ' set policy-name=' + policy_name + '\n')
    time.sleep(1)
    cnr_connection.send('save\n')
    time.sleep(1)
    cnr_connection.send('server dhcp reload\n')
    time.sleep(1)

    cnr_connection.close()


if __name__ == "__main__":
    configuration_file_change()
