import configparser
import os
from pathlib import Path

current_dir = os.getcwd()
ini_file_path = Path(current_dir)
ini = configparser.ConfigParser()
ini.read(str(ini_file_path) + '\SanityTest.ini')


def check(sysdescr_str: str):
    cm_hw_rev = ini['sysDescr']['HW_REV']
    cm_vendor = ini['sysDescr']['VENDOR']
    cm_bootr = ini['sysDescr']['BOOTR']
    cm_sw_rev = ini['sysDescr']['SW_REV']
    cm_model = ini['sysDescr']['MODEL']

    if sysdescr_str.find('HW_REV: ' + cm_hw_rev) != -1:
        trigger1 = True
    else:
        trigger1 = False
        print('HW_Rev is not correct. The expected HW_Rev is ' + cm_hw_rev)

    if sysdescr_str.find('VENDOR: ' + cm_vendor) != -1:
        trigger2 = True
    else:
        trigger2 = False
        print('VENDOR is not correct. The expected VENDOR is ' + cm_vendor)

    if sysdescr_str.find('BOOTR: ' + cm_bootr) != -1:
        trigger3 = True
    else:
        trigger3 = False
        print('BOOTR is not correct. The expected BOOTR is ' + cm_bootr)

    if sysdescr_str.find('SW_REV: ' + cm_sw_rev) != -1:
        trigger4 = True
    else:
        trigger4 = False
        print('SW_Rev is not correct. The expected SW_Rev is ' + cm_sw_rev)

    if sysdescr_str.find('MODEL: ' + cm_model) != -1:
        trigger5 = True
    else:
        trigger5 = False
        print('MODEL is not correct. The expected MODEL is ' + cm_model)

    if trigger1 and trigger2 and trigger3 and trigger4 and trigger5:
        return True
    else:
        return False


if __name__ == "__main__":
    check()
