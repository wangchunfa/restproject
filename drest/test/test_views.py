#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 0024 16:04
# @Author  : chunfa.wang
# @Email   : wang_chun_fa@163.com
# @File    : test_views.py
# @Software: PyCharm
import json
from django.test import TestCase
from rest_framework.test import APITestCase

"""
注意：下面的4代码一定要加在执行代码前面，用于初始化django设置环境
"""
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restproject.settings")
django.setup()


class TestViews(APITestCase):

    def setUp(self):
        """
        这里可以初始化环境信息，如初始化VDC，初始化用户。
        :return:
        """
        self.vdc = 'vdc0000001'
        self.vm_id = 'vm0000001'
        self.current_user = 'wangcf'
        self.base_url = "http://testserver:8000/user"

    def tearDown(self):
        """
        这里可以清除测试残留资源
        :return:
        """
        pass

    def test_add_user(self):
        """
        这里测试用例，相当于写接口的客户端，同时兼顾清理测试过程产生的数据。
        :return:
        """
        import inspect, pprint
        pprint.pprint(inspect.stack())
        headers = {"Content-Type": "application/json"}
        json_data = json.dumps({
            "created": "2019-01-29 18:31:57",
            "password": "123456",
            "username": "奥巴马"
        })
        conten_type = json.dumps({"Content-Type": "application/json"})
        # 1: 正常业务调用
        resp = self.client.post(path="/user/add/", data=json_data, content_type=conten_type)
        # 2: 断言状态码
        self.assertEqual(resp.status_code, 200, 'add user error!')
        # 3: 清除测试数据
        user = json.loads(str(resp.content,  encoding="utf-8"))
        print("new user info: ")
        print(user)
        # resp = self.client.post(path="/user/del/", data=json.dumps(user), content_type=conten_type)
        # # 4: 再次断言清除数据状态码
        # self.assertEqual(resp.status_code, 200, 'del user error!')
        # print("clear new user info success.")
        return resp


    def test_add_user_1(self):
        """
        这里测试用例，相当于写接口的客户端，同时兼顾清理测试过程产生的数据。
        :return:
        """
        from drest.models import User
        user = User.objects.first()
        print(user,  1111, len(User.objects.all()))
        user.username =  "tdk"
        user.save()
        self.assertEqual(len(User.objects.all()), 19)