#!/bin/python3
# -*- encoding:utf-8 -*-
# TODO 读取配置文件类

from interfaceTest.base.base_path import _config_path
import configparser


class ReadConfig:

    def __init__(self):
        fd = open(_config_path, encoding='utf-8')

        self.cf = configparser.ConfigParser()
        self.cf.read(_config_path, encoding="utf-8")

    def get_login(self, name):
        values = self.cf.get("Login", name)
        return values

    def get_database(self, name):
        values = self.cf.get("DATABASE", name)
        return values


cf = configparser.ConfigParser()
cf.read("E:\pyworkspace\interfaceTest\config\config.ini",encoding="utf-8")
print(cf.items('DATABASE'))

test = ReadConfig()
print(test.get_login('username'))