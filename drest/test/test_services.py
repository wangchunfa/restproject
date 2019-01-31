#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 0024 16:29
# @Author  : chunfa.wang
# @Email   : wang_chun_fa@163.com
# @File    : test_services.py
# @Software: PyCharm
import unittest
from drest.services import MyMath

"""
注意：下面的4代码一定要加在执行代码前面，用于初始化django设置环境
"""
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restproject.settings")
django.setup()


class TestMyMath(unittest.TestCase):

    def setUp(self):
        """
        这里可以初始化环境
        :return:
        """
        self.x = 10
        self.y = 0
        # self.y = 2
        self.my_math = MyMath(self.x, self.y)

    def tearDown(self):
        """
        这里可以清除测试残留资源
        :return:
        """
        pass

    def test_div(self):
        my_math = MyMath(10, 2)
        result = my_math.div()
        # 断言的提示信息要准确详尽，方便后续排查问题
        # self.assertEqual(result, 5, 'the div result must be 5.') # 不详尽的记录方式
        self.assertEqual(result, 5, ('x=%s，y=%s, the div result must be 5.' % (10, 2)))

    def test_sum(self):
        result = self.my_math.sum()
        self.assertEqual(result, self.x + self.y, ('x=%s，y=%s, the sum result muster be 12.' % (self.x, self.y)))

    def test_div_zero(self):
        result = self.my_math.div()
        self.assertEqual(result, 5, ('x=%s，y=%s, the div result must be 5.' % (self.x, self.y)))


