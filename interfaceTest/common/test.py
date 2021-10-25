#!/bin/python3
# -*- encoding:utf-8 -*-


import requests
import json
import xlrd
import xlwt


s = requests.session()
b = s.request(method='POST',
              url='http://192.168.100.253:8884/api/login/',
              data=json.dumps({'username': 3870, "password": "68e0b554c4828b7f19c8507e4c091aa42472ff01"}),
              headers={"X-Ajax-Req":"1"})


wb = xlrd.open_workbook('E:/pyworkspace/interfaceTest/testCase/workstation.xls')
table = wb.sheet_by_index(0)
data = []
title = table.row_values(0)
for row in range(1,table.nrows):
    row_value = table.row_values(row)
    data.append(dict(zip(title,row_value)))
print(data)