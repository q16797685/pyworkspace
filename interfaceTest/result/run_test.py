#!/bin/python3
# -*- encoding:utf-8 -*-
# TODO 主方法类


from interfaceTest.base.base_requests import BaseRequests
from interfaceTest.common.operationExcel import OperationExcel
from interfaceTest.common.operationExcel import ExcelVarles
from interfaceTest.common.configRead import ReadConfig
from interfaceTest.base.baseLogin import BaseLogin
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

        global token_headers

        #   TODO 定义excel中行数据
        rows_count = self.data.rows
        #   TODO 遍历每个行数字段数据
        for i in range(0, rows_count - 1):
            is_run = self.data.get_excel_data()[i]
            if is_run:
                #   TODO 获取excel遍历中各列信息
                run_id = is_run[self.header_information.case_Id]
                run_method = is_run[self.header_information.case_Method]
                run_url = is_run[self.header_information.case_Url]
                run_headers = is_run[self.header_information.case_Headers]
                run_data = is_run[self.header_information.case_Data]
                run_name = is_run[self.header_information.case_Name]
                run_status_code = is_run[self.header_information.case_Result]
                run_parameter = is_run[self.header_information.case_Parameter]
                #   TODO 登录接口
                if run_id == 'case_001':
                    case_login = {'method': run_method,
                                  'url': self.readConfig.get_login('baseurl') + run_url,
                                  'headers': json.loads(run_headers),
                                  'parameter': json.loads(run_data)}
                    response = BaseRequests(case_login).get_response()
                    assert response.status_code == 200
                    #  TODO 获取返回体json信息中token字段
                    token_headers = {"Authorization": response.json()['data']['token'],
                                     "Content-Type": "application/json;charset=UTF-8",
                                     "X-Ajax-Req": "1"}
                #   TODO 获取科室列表信息
                elif run_id == 'case_002':
                    case_department = {'method': run_method,
                                       'url': self.readConfig.get_login('baseurl') + run_url,
                                       'headers': token_headers,
                                       'parameter': run_data}
                    BaseRequests(case_department).get_response()
                # TODO 下诊断
                elif run_name == '下诊断':
                    case_diagnosis = {'method': run_method,
                                      'url': self.readConfig.get_login('baseurl') + run_url,
                                      'headers': token_headers,
                                      'parameter': self.patient.diagnosis_information}
                    BaseRequests(case_diagnosis).get_response()
                # TODO 开医嘱
                elif run_name == '开医嘱':
                    case_order = {'method': run_method,
                                  'url': self.readConfig.get_login('baseurl') + run_url,
                                  'headers': token_headers,
                                  'parameter': self.patient.order_submit_information}
                    response = BaseRequests(case_order).get_response()
                    print(response.json())
                #   TODO 其他用例
                else:
                    case = {'method': run_method,
                            'url': self.readConfig.get_login('baseurl') + run_url + run_parameter,
                            'headers': token_headers,
                            'parameter': self.patient.order_submit_information}
                    response = BaseRequests(case).get_response()
                    print('test %s' % response.json())


