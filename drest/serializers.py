#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/23 0023 18:11
# @Author  : chunfa.wang
# @Email   : wang_chun_fa@163.com
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from drest.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'created')


