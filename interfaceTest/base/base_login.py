#!/bin/python3
# -*- encoding:utf-8 -*-


import requests
from interfaceTest.common.configRead import ReadConfig
from interfaceTest.base.base_requests import BaseRequests
import json
import time


class BaseLogin:

    def __init__(self):
        self.readConfig = ReadConfig()

    def get_login_token(self):

        url = self.readConfig.get_login('baseurl')
        api = self.readConfig.get_login('api')
        username = self.readConfig.get_login('username')
        password = self.readConfig.get_login('password')
        data = {'username': username, 'password': password}
        case = {'method': 'POST',
                'url': url+api,
                'headers': {"X-Ajax-Req": "1"},
                'parameter': data}
        a = BaseRequests(case).run_main()
        token = a.json()['data']['token']
        token_headers = {"Content-Type": "application/json;charset=UTF-8",
                         "Authorization": token}
        return token_headers

    def get_bind_workbench(self):

        login_token_headers = BaseLogin().get_login_token()
        case = {'method': 'POST',
                'url': self.readConfig.get_login('baseurl') + "/api/emr/workbench/bindWorkbench?workbenchId=6857",
                'headers': login_token_headers,
                'parameter': {}}
        BaseRequests(case).run_main()
        return login_token_headers

    def get_add_patient(self):
        #   TODO 日期格式方法
        visit_date = time.strftime("%Y-%m-%d")
        patient_data = {"departmentId": 2850,
                        "doctorId": 610,
                        "firstVisitFlag": "1",
                        "visitDate": visit_date,
                        "patientId": "40288f86-6dd283e0-016d-d91c4c69-0001"}
        case = {'method': 'POST',
                'url': self.readConfig.get_login('baseurl') + "/api/emr/reservation/add",
                'headers': BaseLogin().get_bind_workbench(),
                'parameter': patient_data}
        BaseRequests(case).run_main()

    def get_all_patient(self):

        case = {'method': 'get',
                'url': self.readConfig.get_login('baseurl') + "/api/api/dw/v2/outpatient/clinic/patient/search?pageNo=1&pageSize=10&patientName=&total=0&t=1640934840902",
                'headers': BaseLogin().get_bind_workbench(),
                'parameter': {}}
        patient_dict_data = BaseRequests(case).run_main()
        return patient_dict_data

# if __name__ == '__main__':
#     r = BaseLogin()
#     print(r.get_add_patient())

