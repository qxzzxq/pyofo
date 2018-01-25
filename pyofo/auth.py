# coding: utf-8

from . import config
from .ofo import Wrapper


class LoginHandler(Wrapper):
    """
    Login is in two step: + Request code with your phone number, you ll receive an sms + Send back this code
    https://github.com/ubahnverleih/WoBike/blob/master/Ofo.md
    """

    def __init__(self, tel, ccc, lat, lng):
        """

        :param tel: phone number intl format
        :param ccc: Country calling codes (like 33)
        :param lat: latitude
        :param lng: Longitude
        """
        super().__init__(proxies=config.PROXIES, auth=config.AUTH)
        self.tel = tel
        self.ccc = ccc
        self.lat = lat
        self.lng = lng

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

        r = self._post(url=_url, data=data)
        return r
