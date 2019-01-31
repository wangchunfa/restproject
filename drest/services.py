#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 0024 16:24
# @Author  : chunfa.wang
# @Email   : wang_chun_fa@163.com
# @File    : services.py
# @Software: PyCharm

from drest.serializers import UserSerializer


class MyMath:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def div(self):
        z = self.x / self.y
        return z

    def sum(self):
        z = self.x + self.y
        return z


class UserService:

    def add_user(self, data):
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return serializer.errors

