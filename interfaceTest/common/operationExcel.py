#!/bin/python3
# -*- encoding:utf-8 -*-

# TODO 获取excel表数据
"""获取excel表数据"""


import xlrd
import os
from interfaceTest.base.base_path import _testcase_path
import json,pytest


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
        self.columns = self.sheet.ncols

    # TODO 获取excel每行数据
    def get_excel_data(self):
        data = []
        for row in range(1, self.sheet.nrows):
            row_value = self.sheet.row_values(row)
            data.append(dict(zip(self.keys, row_value)))
        return data

    # TODO 获取某个单元格写入数据
    def get_value(self,rows,columns):
        values = self.sheet.cell_value(rows,columns)
        return values

    # TODO 获取每个列第一行的标题
    def get_case_Id(self):
        return ExcelVarles.case_Id

    def get_case_Name(self):
        return ExcelVarles.case_Name

    def get_case_Url(self):
        return ExcelVarles.case_Url

    def get_case_Method(self):
        return ExcelVarles.case_Method

    def get_case_Headers(self):
        return ExcelVarles.case_Headers

    def get_case_Parameter(self):
        return ExcelVarles.case_Parameter

    def get_case_Data(self):
        return ExcelVarles.case_Data

    def get_case_Code(self):
        return ExcelVarles.case_Code

    def get_case_Result(self):
        return ExcelVarles.case_Result

    # def get_excel_list_data(self):
    #     #   TODO 定义excel中行数据
    #     # rows_count = self.rows
    #     #   TODO 遍历每个行数字段数据
    #     for i in range(0, self.rows - 1):
    #         return OperationExcel().get_excel_data()[i]


if __name__ == '__main__':
    r = OperationExcel()
    test = r.get_value(2,5)
    print(test)

