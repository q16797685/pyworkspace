#!/bin/python3
# -*- encoding:utf-8 -*-


from interfaceTest.base.base_requests import BaseRequests
from interfaceTest.common.operationExcel import OperationExcel
from interfaceTest.common.operationExcel import ExcelVarles
from interfaceTest.common.configRead import ReadConfig
import json


class RunTest:

    def __init__(self):
        self.data = OperationExcel()
        self.header_informations = ExcelVarles()
        self.readConfig = ReadConfig()


    def go_on_run(self):
        rows_count = self.data.rows
        for i in range(0, rows_count-1):
            is_run =  self.data.get_excel_data()[i]
            if is_run:
                run_method = is_run[self.header_informations.case_Method]
                run_url = is_run[self.header_informations.case_Url]
                run_headers = is_run[self.header_informations.case_Headers]
                run_data = is_run[self.header_informations.case_Data]
                case = {'method': run_method,
                        'url': self.readConfig.get_login('baseurl') + run_url,
                        'headers': json.loads(run_headers),
                        'parameter': run_data}
                response = BaseRequests(case).get_response()
                print('test %s' % response.text)


if __name__ == '__main__':
    r = RunTest()
    test = r.go_on_run()