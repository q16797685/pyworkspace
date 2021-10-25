#!/bin/python3
# -*- encoding:utf-8 -*-


from interfaceTest.base.method import RunMethod
import requests


def login_token():
    url = "http://192.168.100.253"
    methed = 'POST'
    port = 8884
    url = "/api/login/"
    username = 3870
    password = "68e0b554c4828b7f19c8507e4c091aa42472ff01"
    data = {"X-Ajax-Req":1,
            "Content-Type":"application/json;charset=UTF-8"}




