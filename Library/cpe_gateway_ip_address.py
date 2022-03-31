cpe_gateway_dict = {"CBR8": "192.168.9.254", "E6k": "192.168.8.254", "C4C": "192.168.7.254", "C10G": "192.168.6.254",
                    "C40G": "192.168.3.254"}


def match(cmts: str):
    return cpe_gateway_dict[cmts]


if __name__ == "__main__":
    match()
