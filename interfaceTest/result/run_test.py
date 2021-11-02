#!/bin/python3
# -*- encoding:utf-8 -*-


from interfaceTest.base.base_requests import BaseRequests
from interfaceTest.common.operationExcel import OperationExcel
from interfaceTest.common.operationExcel import ExcelVarles
from interfaceTest.base.method import BaseRequests
from interfaceTest.common.configRead import ReadConfig
import json


class RunTest:

    def __init__(self):
        self.data = OperationExcel()
        self.header_informations = ExcelVarles()
        self.run_request = BaseRequests()
        self.readConfig = ReadConfig()


    def go_on_run(self):
        rows_count = self.data.rows
        print(rows_count)
        for i in range(0, rows_count-1):
            is_run =  self.data.get_excel_data()[i]
            print(is_run)
            if is_run:
                run_method = is_run[self.header_informations.case_Method]
                run_url = is_run[self.header_informations.case_Url]
                run_headers = is_run[self.header_informations.case_Headers]
                run_data = is_run[self.header_informations.case_Data]
                res = self.run_request.run_main('post',url='http://192.168.100.253:8884/api/login',headers=run_headers,data=run_data)
                # print(res)





if __name__ == '__main__':
    r = RunTest()
    test = r.go_on_run()