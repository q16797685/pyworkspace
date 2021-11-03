#!/bin/python3
# -*- encoding:utf-8 -*-


import requests
from interfaceTest.common.configRead import ReadConfig
import json


class BaseLogin:

    def __init__(self):
        self.readConfig = ReadConfig()

    def get_login_token(self):

        s = requests.session()
        url = self.readConfig.get_login('baseurl')
        api = self.readConfig.get_login('api')
        username = self.readConfig.get_login('username')
        password = self.readConfig.get_login('password')
        data = {'username':username,'password':password}
        res = s.post(url + api, json.dumps(data))
        token_headers = {"Authorization": res.json()['data']['token']}
        return res


if __name__ == '__main__':
    r = BaseLogin()
    r.get_login_token()

