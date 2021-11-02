#!/bin/python3
# -*- encoding:utf-8 -*-


import requests
from interfaceTest.common.configRead import ReadConfig
from interfaceTest.common.operationExcel import OperationExcel
from interfaceTest.common.operationExcel import ExcelVarles
import json



class BaseRequests:

    # TODO 初始化request请求默认参数
    def __init__(self, case, proxies=None, headers=None, cookies=None, timeout=15, base_url=None):

        self.case = case
        self.proxies = proxies
        self.headers = headers
        self.cookies = cookies
        self.timeout = timeout
        self.base_url = base_url

    # TODO request主方法
    def run_main(self):
        method = self.case['method']
        url = self.case['url']
        headers = self.case['headers']
        if self.case['parameter']:
            # TODO 字符串转化成字典类型eval函数
            data = eval(self.case['parameter'])
        else:
            data = None

        s = requests.session()
        res = ''
        if method.upper() == 'POST':
            try:
                res = s.request(method='post', url=url, data=json.dumps(data), headers=headers)
            except Exception as e:
                print('why post')
        elif method.upper() == 'GET':
            try:
                res = s.request(method='get', url=url, data=json.dumps(data), headers=headers)
            except Exception as e:
                print('why get')
        else:
            raise ValueError('method方法为get和post')
        return res

#   TODO 获取返回内容
    def get_response(self):
        response_run = self.run_main()
        return response_run

