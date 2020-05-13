import os

TIME_FORMAT = "%Y-%m-%d/%H:%M:%S"
# CURRENT_DATETIME = datetime.fromtimestamp(CURRENT_TIME).strftime(TIME_FORMAT_LOG)
PYTHON_DIRECTORY = "/".join(os.path.realpath(__file__).split("/")[:-1])

PORT = 143

USERS = {
    "root": "03f4697afc55f208ad95dbc423e98adc",
}

USER_MAX_TCP_CONNS = {
}

USER_EXPIRATIONS = {
}

USER_DATA_QUOTA = {
}

try:
    with open(PYTHON_DIRECTORY + "/user_list.txt") as file:
        user_list = [s.strip() for s in file.readlines()]
        for user in user_list:
            user_split = user.split(" ")
            username = user_split[0]
            secret = user_split[1]
            max_tcp = int(user_split[2])
            time = user_split[3]
            quota = int(user_split[4])
            USERS[username] = secret
            USER_MAX_TCP_CONNS[username] = max_tcp
            USER_EXPIRATIONS[username] = time
            USER_DATA_QUOTA[username] = quota

except Exception as e:
    print(e)

MODES = {
    # Classic mode, easy to detect
    "classic": True,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": True,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start

TLS_DOMAIN = "www."
for i in range(8):
    TLS_DOMAIN = TLS_DOMAIN + "abcdefghijklmnopqrstuvwxyz"
TLS_DOMAIN = TLS_DOMAIN + ".co"

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "25c6e35ed50e853cedba73667a8240ae"
