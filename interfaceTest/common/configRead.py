#!/bin/python3
# -*- encoding:utf-8 -*-
# TODO 读取配置文件类


from interfaceTest.base.base_path import _config_path
import configparser


class ReadConfig:

    #   TODO 初始化读取配置文件方法
    def __init__(self):

        self.cf = configparser.ConfigParser()
        self.cf.read(_config_path, encoding="utf-8")

    #    TODO 获取[Login]配置文件信息
    def get_login(self, name):
        values = self.cf.get("Login", name)
        return values

    #    TODO 获取[DATABASE]配置文件信息
    def get_database(self, name):
        values = self.cf.get("DATABASE", name)
        return values

