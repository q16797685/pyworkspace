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
            data = eval(self.case['parameter'])
        else:
            data = None

        s = requests.session()
        res = ''
        if method.upper() == 'POST':
            try:
                res = s.request(method='post', url=url, data=json.dumps(data), headers=headers)
                print('test111 %s' % res.json()['data']['token'])
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

    def get_response(self):
        response_run = self.run_main()
        return response_run


if __name__ =='__main__':
    readConfig = ReadConfig()
    operationExcel = OperationExcel()
    header_informations = ExcelVarles()
    testCase = operationExcel.get_excel_data()
    for i in range(0, operationExcel.rows - 1):
        is_run = operationExcel.get_excel_data()[i]
        if is_run:
            run_method = is_run[header_informations.case_Method]
            run_url = is_run[header_informations.case_Url]
            run_headers = is_run[header_informations.case_Headers]
            run_data = is_run[header_informations.case_Data]
            case = {'method': run_method,
                    'url': readConfig.get_login('baseurl') + run_url,
                    'headers': json.loads(run_headers),
                    'parameter': run_data}
            print(case)
            response = BaseRequests(case).get_response()
            print(response.text)
