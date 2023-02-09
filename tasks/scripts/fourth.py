from ipaddress import ip_address
from urllib.error import URLError
import urllib.request


def get_my_public_ip_address() -> ip_address:
    try:
        url = "https://ifconfig.me/"
        f = urllib.request.urlopen(url)

        ip_addr = f.read().decode('utf-8')
        return ip_address(ip_addr)
    except URLError:
        print("Интернет не работает или https://ifconfig.me/ не доступен")
    except Exception as err:
        raise Exception(f"It's my fault\n{err}")


if __name__ == '__main__':
    get_my_public_ip_address()
