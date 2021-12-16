#!/bin/python3
# -*- encoding:utf-8 -*-


import requests
from interfaceTest.common.configRead import ReadConfig
import json
import time


class BaseLogin:

    def __init__(self):
        self.readConfig = ReadConfig()

    def get_login_token(self):

        s = requests.session()
        url = self.readConfig.get_login('baseurl')
        api = self.readConfig.get_login('api')
        username = self.readConfig.get_login('username')
        password = self.readConfig.get_login('password')
        data = {'username': username, 'password': password}
        res = s.post(url + api, json.dumps(data))
        token = res.json()['data']['token']
        token_headers = {"Content-Type": "application/json;charset=UTF-8",
                         "X-Ajax-Req": "1",
                         "Authorization": token}
        #   TODO 日期格式方法
        visit_date = time.strftime("%Y-%m-%d")
        s.post(url + "/api/emr/workbench/bindWorkbench?workbenchId=6857", headers=token_headers)
        patient_data = {"departmentId": 2850,
                        "doctorId": 610,
                        "firstVisitFlag": "1",
                        "visitDate": visit_date,
                        "patientId": "40288f86-6dd283e0-016d-d91c4c69-0001"}
        s.post(url + "/api/emr/reservation/add", headers=token_headers, json=patient_data)
        patient_dict_data = s.get(url + "/api/api/dw/v2/outpatient/clinic/patient/search?pageNo=1&pageSize=10&patientName=&total=1&status=1", headers=token_headers)
        patient_data = patient_dict_data.json()['results']
        return patient_data


if __name__ == '__main__':
    r = BaseLogin()
    r.get_login_token()

