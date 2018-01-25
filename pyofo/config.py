# coding: utf-8
from requests.auth import HTTPProxyAuth

# URL
BASE_URL = 'https://one.ofo.com'

# Proxy
PROXIES = None  # {'http': 'xxx', ...}
AUTH = None

# Token
TOKEN = None


def set_proxies(**new_proxies):
    """Modify PROXIES"""
    global PROXIES
    PROXIES = new_proxies


def set_auth(username, password):
    global AUTH
    AUTH = HTTPProxyAuth(username, password)


def set_token(new_token):
    global TOKEN
    TOKEN = new_token
