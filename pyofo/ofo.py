# coding: utf-8

import requests

from . import config


class Wrapper:

    def __init__(self, header=None, proxies=None, auth=None):
        self.header = header or {
            'content-type': 'application/x-www-form-urlencoded'
        }
        self.proxies = proxies
        self.auth = auth

    def complete_url(self, path):
        return '{base}/{path}'.format(base=config.BASE_URL, path=path)

    def _post(self, url, data):
        return requests.post(url=url, headers=self.header, data=data, proxies=self.proxies, auth=self.auth)


class Ofo(Wrapper):

    def __init__(self):
        super().__init__(proxies=config.PROXIES, auth=config.AUTH)
        self.token = config.TOKEN

    def nearby_ofo_car(self, lng, lat, token=None):

        __token = token or self.token
        if not __token:
            raise PermissionError('No user token is given. Auth are mandatory for searching nearby ofo bikes.')

        __data = {
            'source': '2',
            'token': self.token,
            'lng': lng,
            'lat': lat
        }
        __url = self.complete_url(path='nearbyofoCar')

        r = self._post(url=__url, data=__data)
        return r



