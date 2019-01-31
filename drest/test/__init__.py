#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 0024 16:03
# @Author  : chunfa.wang
# @Email   : wang_chun_fa@163.com
# @File    : __init__.py.py
# @Software: PyCharm

from django.test.runner import DiscoverRunner


class MyDiscoverRunner(DiscoverRunner):
    """
    去掉创建/销毁数据库过程
    """

    def run_tests(self, test_labels, extra_tests=None, **kwargs):
        """
        Run the unit tests for all the test labels in the provided list.

        Test labels should be dotted Python paths to test modules, test
        classes, or test methods.

        A list of 'extra' tests may also be provided; these tests
        will be added to the test suite.

        Return the number of tests that failed.
        """
        # self.setup_test_environment()
        suite = self.build_suite(test_labels, extra_tests)
        print(234567)
        # 不创建test_数据库
        # old_config = self.setup_databases()
        self.run_checks()
        result = self.run_suite(suite)
        # 不删除数据库
        # self.teardown_databases(old_config)
        # self.teardown_test_environment()
        return self.suite_result(suite, result)

