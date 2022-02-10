import configparser
import paramiko
import os
import time
import pytest
from Library import check_sysdescr

ini = configparser.ConfigParser()
ini.read('SanityTest.ini')


@pytest.mark.order(1)
def system_description_match_with_arris():
    cm_mac = ini['database']['CM_MAC']
    emta_mac = ini['database']['MTA_MAC']

    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    session.connect('172.21.38.254', port=22, username='root', password='')
    connection = session.invoke_shell()
    connection.send("enable\n")
    time.sleep(1)
    connection.send("show cable modem " + cm_mac + " verbose\n")
    time.sleep(1)

    # show system description with CM MAC address
    connection.send("show cable modem " + cm_mac + " system-description\n")
    time.sleep(3)
    output = connection.recv(12800)
    output = str(output.decode('utf-8', errors='ignore'))
    all_info = output
    # check all elements
    sysdescr_compare_result = check_sysdescr.check(all_info)
    if sysdescr_compare_result:
        print("MIB sysDescr check by CM MAC: Pass")
        assert 1 == 1
    else:
        print("MIB sysDescr check by CM MAC: Fail")
        assert 1 != 1

    connection.send("show cable modem cpe-mac " + emta_mac + " system-description\n")
    time.sleep(3)
    output = connection.recv(12800)
    output = str(output.decode('utf-8', errors='ignore'))
    all_info += output
    # check all elements
    sysdescr_compare_result = check_sysdescr.check(all_info)
    if sysdescr_compare_result:
        print("MIB sysDescr check by MTA MAC: Pass")
        assert 1 == 1
    else:
        print("MIB sysDescr check by MTA MAC: Fail")
        assert 1 != 1

    connection.close()

    print('Please check the test result under "Test_Report".')

    # export all information we got from CMTS to directory "Test_Report"
    file = open(os.path.join(os.getcwd(),
                             r'Test_Report\Test_1_General_CMTS_Response_Arris\General_CMTS_Response.txt'), 'w')
    file.write(all_info)
    file.close()


if __name__ == "__main__":
    system_description_match_with_arris()
