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

    # TODO: Check if `tor` exists and it is executable

    tor_path = os.path.join(os.environ["LAMBDA_TASK_ROOT"], "tor")

    process = Popen([tor_path, "-f", tmp], cwd=os.path.dirname(data_dir), stdout=PIPE)
    return process


def get_url(url="http://ipinfo.io/", user_agent=""):
    headers = {
        'User-Agent': user_agent
    }
    proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
    result = requests.get(url, headers=headers, proxies=proxies)
    return result


def lambda_handler(event, context):
    process = setup_tor_proxy()
    # TODO: Add function to verify that TOR set up successfully
    sleep(20)
    # TODO: refactor this. This is quick and dirty, there are cleaner ways to do this
    if not event['url']:
        output = get_url()
    else:
        if event['user_agent']:
            output = get_url(event['url'], event['user_agent'])
        else:
            output = get_url(event['url'])
    process.terminate()
    return output.raw
