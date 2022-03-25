# Lan Device is the PC installed 2.5 Ethernet Card which IP is 172.21.2.118

import re
import time
import paramiko


def access(telnet_ip: str):
    lan_pc_ip = '172.21.2.118'
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    output = '\n=================================================================================\n'

    cnr = paramiko.SSHClient()
    cnr.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cnr.connect(lan_pc_ip, port=22, username='UBEEi7', password='20040401')
    cnr_connection = cnr.invoke_shell()
    time.sleep(1)
    cnr_connection.send('ssh ' + telnet_ip + '\n')
    time.sleep(10)
    output += str(cnr_connection.recv(12800).decode('utf-8', errors='ignore'))
    output = ansi_escape.sub("", output)

    cnr_connection.close()
    output += '\n=================================================================================\n'

    if output.find('port 22: Connection refused') == -1 or output.find('在連接埠 23: 連線失敗') == -1:
        return output, False
    else:
        return output, True


if __name__ == "__main__":
    access()
