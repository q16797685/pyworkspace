#!/bin/python3
# -*- encoding:utf-8 -*-


import requests
from interfaceTest.base.base_path import _testcase_path
import json


class BaseRequests:

    # TODO 初始化request请求默认参数
    def __init__(self, case, proxies=None, headers=None, cookies=None, timeout=15, max_retries=3):

        self.case = case
        self.proxies = proxies
        self.headers = headers
        self.cookies = cookies
        self.timeout = timeout
        self.base_url = "http://192.168.100.253:8884/"

    def run_main(self):
        method = self.case['method']
        url = self.base_url + self.case['url']
        if self.case['parameter']:
            data = eval(self.case['parameter'])
            print(data)
            print(type(data))
        else:
            data = None

        s = requests.session()
        res = ''
        if method.upper() == 'POST':
            try:
                res = s.request(method='post', url=url, data=json.dumps(data), headers=self.headers)
            except Exception as e:
                print('test post')
        elif method.upper() == 'GET':
            try:
                res = s.request(method='get', url=url, data=json.dumps(data), headers=self.headers)
            except Exception as e:
                print('test get')
        else:
            raise ValueError('method方法为get和post')

        return res

    def get_response(self):
        response_run = self.run_main()
        return response_run

if __name__ =='__main__':
    case = {'method': 'post', 'url': '/api/login',
            'parameter': '{"username": "3870", "password": "68e0b554c4828b7f19c8507e4c091aa42472ff01"}'}
    response = BaseRequests(case).get_response()
    print(response.text)