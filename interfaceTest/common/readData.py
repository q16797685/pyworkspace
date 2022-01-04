#!/bin/python3
# -*- encoding:utf-8 -*-


import pymysql
from interfaceTest.common.configRead import *


class ReadDataBase:

    def __init__(self):
        self.readConfig = ReadConfig()
        self.connect = pymysql.Connect(
            host=self.readConfig.get_database('host'),
            port=int(self.readConfig.get_database('port')),
            user=self.readConfig.get_database('username'),
            passwd=self.readConfig.get_database('password'),
            db=self.readConfig.get_database('database')
        )

    def get_diagnosis_information(self):
        connect_mysql = self.connect.cursor()
        sql = "SELECT id,name from EMR_DIAGNOSIS where `status` = '1' limit 100"
        connect_mysql.execute(sql)
        results = connect_mysql.fetchall()
        return results

    def get_patient_information(self):
        connect_mysql = self.connect.cursor()
        sql = "SELECT id from PT_PATIENT limit 100"
        connect_mysql.execute(sql)
        results = connect_mysql.fetchall()
        print(results[0])


# if __name__ == '__main__':
#     r = ReadDataBase()
#     r.get_diagnosis_information()
#     r.get_patient_information()