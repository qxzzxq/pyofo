# coding: utf-8
from requests.auth import HTTPProxyAuth

# URL
BASE_URL = 'https://one.ofo.com'

# Proxy
proxies = None
auth = None


def set_proxies(**new_proxies):
    """Modify proxies"""
    global proxies
    proxies = new_proxies


def set_auth(username, password):
    global auth
    auth = HTTPProxyAuth(username, password)