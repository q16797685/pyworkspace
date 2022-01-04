#!/bin/python3
# -*- encoding:utf-8 -*-
# TODO pytest方法


import pytest,os
from interfaceTest.result.run_test import RunTest
from interfaceTest.base.base_path import _report_path
rc = RunTest().go_on_run()


@pytest.mark.parametrize('data',rc)
def test_name(data):
    return data
    # assert 200 == data



if __name__ == '__main__':
    pytest.main(['--alluredir', _report_path+'/result', 'test.py'])
    split = 'allure ' + 'generate ' + _report_path+'/result ' + '-o ' + _report_path+'/result/html --clean'
    os.system(split)