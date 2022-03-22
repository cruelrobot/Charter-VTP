import os


def check_accessibility(ping_target: str):
    response = os.system("ping -n 1 " + ping_target)

    # and then check the response...
    if response == 0:
        ping_status = True
    else:
        ping_status = False

    return ping_status


if __name__ == "__main__":
    check_accessibility()
