#!/bin/python3
# -*- encoding:utf-8 -*-
# TODO 主方法类


from interfaceTest.base.base_requests import BaseRequests
from interfaceTest.common.operationExcel import OperationExcel
from interfaceTest.common.operationExcel import ExcelVarles
from interfaceTest.common.configRead import ReadConfig
from interfaceTest.base.base_login import BaseLogin
from interfaceTest.base import base_data
from interfaceTest.base.base_path import *
import json

global token_headers


class RunTest:

    #   TODO 初始化类方法
    def __init__(self):
        self.data = OperationExcel()
        self.header_information = ExcelVarles()
        self.readConfig = ReadConfig()
        self.loginToken = BaseLogin()
        self.patient = base_data

    #   TODO 运行主方法
    def go_on_run(self):

        cookies_token_headers = self.loginToken.get_bind_workbench()
        self.loginToken.get_add_patient()
        get_all_excel = self.data.get_excel_data()
        #   TODO 定义excel中行数据
        rows_count = self.data.rows
        #   TODO 遍历每个行数字段数据
        item = []
        for i in range(0, rows_count - 1):
            is_run = get_all_excel[i]
            if is_run:
                #   TODO 获取excel遍历中各列信息
                run_id = is_run[self.header_information.case_Id]
                run_method = is_run[self.header_information.case_Method]
                run_url = is_run[self.header_information.case_Url]
                run_headers = is_run[self.header_information.case_Headers]
                run_data = is_run[self.header_information.case_Data]
                run_name = is_run[self.header_information.case_Name]
                run_parameter = is_run[self.header_information.case_Parameter]
                #   TODO 下诊断接口
                if run_name == '下诊断':
                    case_diagnosis = {'method': run_method,
                                  'url': self.readConfig.get_login('baseurl') + run_url,
                                  'headers': cookies_token_headers,
                                  'parameter': self.patient.diagnosis_information}
                    response = BaseRequests(case_diagnosis).get_response()
                    item.append(response.json())
                #   TODO 开医嘱接口
                elif run_name == '开医嘱':
                    case_submit = {'method': run_method,
                                      'url': self.readConfig.get_login('baseurl') + run_url,
                                      'headers': cookies_token_headers,
                                      'parameter': self.patient.order_submit_information}
                    response = BaseRequests(case_submit).get_response()
                    # print('test case_submit %s',case_submit)
                    # print(response.json())
                    item.append(response.json())
                # TODO 其他用例
                else:
                    case_get = {'method': run_method,
                                  'url': self.readConfig.get_login('baseurl') + run_url,
                                  'headers': cookies_token_headers,
                                  'parameter': run_data}
                    response = BaseRequests(case_get).get_response()
                    item.append(response.json())
        return item


if __name__ == '__main__':
    a = RunTest()
    a.go_on_run()

