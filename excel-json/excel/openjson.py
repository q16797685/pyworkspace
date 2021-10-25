#!/bin/python3
# -*- encoding:utf-8 -*-


import json, xlwt


def read_score(jsonfile):
    with open(jsonfile, encoding='utf-8') as f:  # 将json文件转化为字典
        score_all = json.load(f)
        print(score_all)

    book = xlwt.Workbook()  # 创建excel文件
    sheet = book.add_sheet('sheet1')  # 创建一个表
    title = ['name', 'type_name', 'children']
    for col in range(len(title)):  # 存入第一行标题
        sheet.write(0, col, title[col])
    # row = 1  # 定义行
    # for k in score_all:
    #     data = score_all[k]  # data保存姓名和分数的list
    #     print(data)
    #     for index in range(len(data)):  # 依次写入每一行
    #         sheet.write(row, index, data[index])
    #     row += 1
    book.save(r"e:\\demo\\test123.xls")


read_score("e:\\demo\\d1.txt")
