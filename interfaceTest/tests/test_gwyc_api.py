#!/bin/python3
# -*- encoding:utf-8 -*-


import requests
import json
from interfaceTest.base.base_path import *
from interfaceTest.common.operationExcel import *



def test_gwyc_api():
    headers = ExcelVarles.case_Headers
    test = OperationExcel().get_excel_data()
    url = "http://192.168.100.253:8884/api/login"
    print(test)
    headerstest = test[0]['请求头']
    data = {"username": "3870", "password": "68e0b554c4828b7f19c8507e4c091aa42472ff01"}
    print(data)
    print(headerstest)
    # r = requests.post(url=url, headers=headerstest, data=json.dumps(data))
    # return str(r.json())


a = test_gwyc_api()
print(a)
