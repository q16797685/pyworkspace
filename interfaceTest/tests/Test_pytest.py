#!/bin/python3
# -*- encoding:utf-8 -*-


from interfaceTest.result.run_test import RunTest
import pytest


class TestPytest:

    def test_go(self):
        RunTest().go_on_run()


if __name__ == '__main__':
    TestPytest().test_go()
    pytest.main(['-x', '--html=./report.html', 'Test_pytest.py'])