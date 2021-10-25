#!/bin/python3
# -*- encoding:utf-8 -*-


import json
ftbm_dict = {}
ywy_dict = {}
ywzj_dict = {}
xt_dict = {}
gnd_dict = {}
ftbm_list = []
ywy_list = []
ywzj_list = []
xt_list = []
gnd_list = []

a = {'访谈部门': '企业管理部', '业务域': '加工生产', '业务组件': '业务管理', '系统': '湖南中烟SEM可视化综合管控系统行业采购管理信息子系统', '功能点': '实施管理'}
b = {'访谈部门': '企业管理部', '业务域': '加工生产', '业务组件': '业务管理', '系统': '湖南中烟SEM可视化综合管控系统行业采购管理信息子系统', '功能点': '业务扩展功能管理'}
c = {'访谈部门': '企业管理部', '业务域': '加工生产', '业务组件': '业务管理', '系统': '湖南中烟SEM可视化综合管控系统售后服务系统模块子系统', '功能点': '工单受理'}
d = {'访谈部门': '企业管理部', '业务域': '加工生产', '业务组件': '业务管理', '系统': '湖南中烟ERP系统', '功能点': '供应商管理'}
e = {'访谈部门': '企业管理部', '业务域': '采购', '业务组件': '采购计划', '系统': '湖南中烟SEM可视化综合管控系统集中审批模块子系统', '功能点': '采购计划查询'}

aset = set(a.items())
eset = set(e.items())
ae = aset|eset
aelist = list(ae)
print(aelist)
if aelist['访谈部门'] == '企业管理部':
    ftbm_dict['department'] = '企业管理部'
    ftbm_dict['type_name'] = '访谈部门'
    ftbm_dict['chldren'] = ftbm_list
if aelist['业务域'] == '加工生产':
    ywy_dict['name'] = '加工生产'
    ywy_dict['type_name'] = '业务域'
    ywy_dict['children'] = ywy_list
    ftbm_list.append(ywy_dict.copy())
if aelist['业务组件'] == '业务管理':
    ywzj_dict['name'] = '业务管理'
    ywzj_dict['type_name'] = '业务组件'
    ywzj_dict['chldren'] = ywzj_list
    ywy_list.append(ywzj_dict.copy())
if aelist['系统'] == '湖南中烟SEM可视化综合管控系统行业采购管理信息子系统':
    xt_dict['name'] = '湖南中烟SEM可视化综合管控系统行业采购管理信息子系统'
    xt_dict['type_name'] = '系统'
    xt_dict['chldren'] = xt_list
    ywzj_list.append(xt_dict.copy())
if aelist['功能点'] == '实施管理':
    gnd_dict['name'] = '实施管理'
    gnd_dict['type_name'] = '功能点'
    xt_list.append(gnd_dict.copy())


excel_json = json.dumps(ftbm_dict,ensure_ascii=False)
print(excel_json)