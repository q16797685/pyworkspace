#!/bin/python3
# -*- encoding:utf-8 -*-

import json
from collections import Counter
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
ywy_test = ['加工生产','采购']
ywzj_test = ['计划管理','采购计划']
xt_test = ['湖南中烟SEM可视化综合管控系统行业采购管理信息子系统','湖南中烟SEM可视化综合管控系统集中审批模块子系统']
gnd_test = ['需求管理','统计分析']

a = [{'访谈部门': '企业管理部', '业务域': '加工生产', '业务组件': '计划管理', '系统': '湖南中烟SEM可视化综合管控系统行业采购管理信息子系统', '功能点': '需求管理'},
     {'访谈部门': '企业管理部', '业务域': '采购', '业务组件': '采购计划', '系统': '湖南中烟SEM可视化综合管控系统集中审批模块子系统', '功能点': '统计分析'}]

set_list = []


for i in a:
    # print(i)
    if (i.get('访谈部门') == '企业管理部'):
        ftbm_dict['department'] = i.get('访谈部门')
        ftbm_dict['type_name'] = '访谈部门'
        ftbm_dict['chldren'] = ftbm_list
        if i.get('业务域') == '加工生产' or i.get('业务域') == '采购':
            ywy_dict['ywy_name'] = i.get('业务域')
            ywy_dict['ywy_type_name'] = '业务域'
            ywy_dict['chldren'] = ywy_list
            ftbm_list.append(ywy_dict.copy())
            if i.get('业务组件') == '计划管理' or i.get('业务组件') == '采购计划':
                ywzj_dict['ywzj_name'] = i.get('业务组件')
                ywzj_dict['ywzj_type_name'] = '业务组件'
                ywzj_dict['chldren'] = ywzj_list
                ywy_list.append(ywzj_dict.copy())
            # else:
            #     if ftbm_dict['department'] == '企业管理部':
            #         ftbm_dict['department'] = a[i].get('访谈部门')
            #         ftbm_dict['type_name'] = '访谈部门'
            #         ftbm_dict['chldren'] = ftbm_list
            #         print('---1*----%s' % ftbm_dict)
            #         break
            #     else:
            #         break
                # if (a[i].get('业务域') == '加工生产'):
                #     ywy_dict['name'] = a[i].get('业务域')
                #     ywy_dict['type_name'] = '业务域'
                #     ywy_dict['chldren'] = ywy_list
                #     ftbm_list.append(ywy_dict.copy())
                #     if a[i].get('业务组件') == '计划管理':
                #         ywzj_dict['name'] = a[i].get('业务组件')
                #         ywzj_dict['type_name'] = '业务组件'
                #         ywzj_dict['chldren'] = ywzj_list
                #         ywy_list.append(ywzj_dict.copy())
                #         if a[i].get('系统') == '湖南中烟SEM可视化综合管控系统行业采购管理信息子系统':
                #             xt_dict['name'] = a[i].get('系统')
                #             xt_dict['type_name'] = '系统'
                #             xt_dict['chldren'] = xt_list
                #             ywzj_list.append(xt_dict.copy())
                #             if a[i].get('功能点') == '需求管理':
                #                 gnd_dict['name'] = a[i].get('功能点')
                #                 gnd_dict['type_name'] = '功能点'
                #                 xt_list.append(gnd_dict.copy())
            #     counters +=1
            # else:
            #     break




    # if i.get('访谈部门') == '企业管理部':
    #     ftbm_dict['department'] = i.get('访谈部门')
    #     ftbm_dict['type_name'] = '访谈部门'
    #     ftbm_dict['chldren'] = ftbm_list
    # if i.get('业务域') in ywy_test:
    #     ywy_dict['name'] = i.get('业务域')
    #     ywy_dict['type_name'] = '业务域'
    #     ywy_dict['chldren'] = ywy_list
    #     ftbm_list.append(ywy_dict.copy())
    # if i.get('业务组件') in ywzj_test:
    #     ywzj_dict['name'] = i.get('业务组件')
    #     ywzj_dict['type_name'] = '业务组件'
    #     ywzj_dict['chldren'] = ywzj_list
    #     ywy_list.append(ywzj_dict.copy())
    # if i.get('系统') in xt_test:
    #     xt_dict['name'] = i.get('系统')
    #     xt_dict['type_name'] = '系统'
    #     xt_dict['chldren'] = xt_list
    #     ywzj_list.append(xt_dict.copy())
    # if i.get('功能点') in gnd_test:
    #     gnd_dict['name'] = i.get('功能点')
    #     gnd_dict['type_name'] = '功能点'
    #     xt_list.append(gnd_dict.copy())
#         break
#
#
print(ftbm_dict)
# print(xt_dict)
# print(ywzj_list)
# print(xt_list)
excel_json = json.dumps(ftbm_dict,ensure_ascii=False)
print(excel_json)
