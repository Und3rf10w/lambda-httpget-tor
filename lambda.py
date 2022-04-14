import requests
from requests.auth import HTTPBasicAuth
from time import sleep


def setup_tor_proxy():
    """Sets up the Tor proxy. Taken from: https://github.com/qrtt1/aws-lambda-tor"""

    from tempfile import mkstemp
    from subprocess import Popen, PIPE
    import os

    fd, tmp = mkstemp(".torrc")
    fd_datadir, data_dir = mkstemp(".data")
    os.unlink(data_dir)
    os.makedirs(data_dir)

    with open(tmp, "w") as f:
        f.write("SOCKSPort 9050\n")
        f.write(f"DataDirectory {data_dir}\n")

    tor_path = os.path.join(os.environ["LAMBDA_TASK_ROOT"], "tor")

    process = Popen([tor_path, "-f", tmp], cwd=os.path.dirname(data_dir), stdout=PIPE)
    return process


def get_url(url):
    headers = {
        'User-Agent': ''
    }
    proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
    result = requests.get(url, headers=headers, proxies=proxies)
    return result


def lambda_handler(event, context):
    process = setup_tor_proxy()
    sleep(20)
    output = get_url("http://ifconfig.me/all")
    process.terminate()
    return output.text
