# coding: utf-8

import requests

from . import config


class LoginHandler:
    """
    Login is in two step: + Request code with your phone number, you ll receive an sms + Send back this code
    https://github.com/ubahnverleih/WoBike/blob/master/Ofo.md
    """

    def __init__(self, tel, ccc, lat, lng):
        self.tel = tel
        self.ccc = ccc
        self.lat = lat
        self.lng = lng
        self.header = {
            'content-type': 'application/x-www-form-urlencoded'
        }
        self.proxies = config.proxies
        self.auth = config.auth

    def complete_url(self, path):
        return '{base}/{path}'.format(base=config.BASE_URL, path=path)

    def _post(self, url, data):
        return requests.post(url=url, headers=self.header, data=data, proxies=self.proxies, auth=self.auth)

    def request_sms_code(self):
        """
        Request a code for login. The code will be sent to your mobile phone
        :return:
        """
        _path = 'verifyCode_v2'
        _url = self.complete_url(_path)
        data = {
            'tel': self.tel,
            'type': '1',
            'ccc': self.ccc,
            'lng': self.lng,
            'lat': self.lat
        }
        # r = requests.post(url=_url, headers=self.header, data=data, proxies=config.proxies)
        r = self._post(url=_url, data=data)

        return r

    def login_with_code(self, otp_code):
        """
        Login with the received OPT code
        :param otp_code:
        :return:
        """
        _path = 'api/login_v2'

        _url = self.complete_url(_path)
        data = {
            'tel': self.tel,
            'code': otp_code,
            'ccc': self.ccc,
            'lng': self.lng,
            'lat': self.lat
        }

        # r = requests.post(url=_url, headers=self.header, data=data, proxies=config.proxies)
        r = self._post(url=_url, data=data)
        return r


