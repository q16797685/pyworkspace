#!/bin/python3
# -*- encoding:utf-8 -*-


import os


os.path.dirname(__file__)   # TODO 获取当前目录
os.path.dirname(os.path.dirname(__file__))      # TODO 获取当前目录的上一级目录

# TODO 项目根路径
_root_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# TODO 报告路径
_report_path = os.path.join(_root_path,'report', 'report.html')

# TODO 配置文件路径
_config_path = os.path.join(_root_path, 'config', 'config.ini')

# TODO 日志文件路径
_log_path = os.path.join(_root_path, 'logs')

# TODO 测试用例数据路径
_testcase_path = os.path.join(_root_path, 'testCase')
