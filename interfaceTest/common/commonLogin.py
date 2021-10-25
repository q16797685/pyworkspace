#!/bin/python3
# -*- encoding:utf-8 -*-


import pytest
import requests
import json
from interfaceTest.common.operationExcel import *


# @pytest.fixture(scope='module')
def company_login_token():
    url = "http://192.168.100.253:8884/api/login"
    headers = ExcelVarles().case_Headers
    data = {"username": "3870", "password": "68e0b554c4828b7f19c8507e4c091aa42472ff01"}
    r = requests.post(url=url, headers=headers, data=json.dumps(data))
    return str(r.json())


a = company_login_token()
print(a)
