#!/bin/python3
# -*- encoding:utf-8 -*-


import requests
import json


class BaseRequests:

    def get_main(self, url, data, headers):
        res = requests.get(url=url, headers=headers, data=data)
        return res.json()

    def post_main(self, url, data, headers):
        res = requests.post(url=url, headers=headers, data=data)
        return res.json()

    def run_main(self, method, url, headers=None, data=None):
        if method == 'post' or method == 'POST':
            res = self.post_main(url, headers, data)
            print(res)
        elif method == 'get' or method == 'GET':
            res = self.get_main(url,headers,data)
            print(res)
        else:
            print('请求方法不正确')


if __name__ == '__main__':
    data = {"username":"3870","password":"68e0b554c4828b7f19c8507e4c091aa42472ff01"}
    print(data)
    test = BaseRequests()
    test.run_main(method = 'POST',
                  url = 'http://192.168.100.253:8884/api/login',
                  data=data)


