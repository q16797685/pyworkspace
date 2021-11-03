#!/bin/python3
# -*- encoding:utf-8 -*-

# TODO 获取excel表数据
"""获取excel表数据"""


import xlrd
import os
from interfaceTest.base.base_path import _testcase_path


class ExcelVarles:
    case_Id = '用例ID'
    case_Module = '用例模块'
    case_Name = '用例名称'
    case_Url = '接口地址'
    case_Method = '请求方法'
    case_Type = '请求类型'
    case_Headers = '请求头'
    case_Parameter = '参数'
    case_Data = '请求参数'
    case_Code = '状态码'
    case_Result = '期望结果'


class OperationExcel:

    def __init__(self, file_name=None, sheet_name=None):

        if file_name:
            self.file_path = os.path.join(_testcase_path, file_name)
            self.sheet_name = sheet_name
        else:
            self.file_path = os.path.join(_testcase_path, 'workstation.xls')
            self.sheet_name = 'workstation'

        # TODO Excel打开
        self.wb = xlrd.open_workbook(self.file_path)
        # TODO Excel表空间
        self.sheet = self.wb.sheet_by_index(0)
        # TODO Excel表头
        self.keys = self.sheet.row_values(0)
        # TODO Excel行数
        self.rows = self.sheet.nrows
        # TODO Excel列数
        self.colums = self.sheet.ncols

    def get_excel_data(self):
        data = []
        for row in range(1,self.sheet.nrows):
            row_value = self.sheet.row_values(row)
            data.append(dict(zip(self.keys,row_value)))
        return data



# if __name__ == '__main__':
#     r = OperationExcel()
    # a = r.get_excel_data()[0]['请求头']
    # b = json.loads(a)
    # print(b)
