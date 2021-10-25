#!/bin/python3
# -*- encoding:utf-8 -*-


from interfaceTest.base.method import RunMethod
import yaml

filepath = 'E:\\pyworkspace\\interfaceTest\\config\\api_config.yml'
with open(filepath,'r',encoding="utf-8") as file_object:
    for files in file_object.readlines():
        print(files.find('host'))