# Create your tests here.

from django.test import TestCase
from drest.models import User
import time

"""
注意：下面的4代码一定要加在执行代码前面，用于初始化django设置环境
"""
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restproject.settings")
django.setup()


class UserModelTest(TestCase):
    def setUp(self):
        pass
        # print("run set up function...")
        # user = User(username='wuxiaxia', password='njkkas', created=time.time())
        # user.save()
        # user = User(userna[ame='wuxiaxia2', password='njkkas', created=time.time())
        # user.save()

    def test_list_user(self):
        result = User.objects.all()
        for u in result:
            print(u.username)
        self.assertIsNotNone(result)

    def test_add_del_user(self):
        user = User(username='telangf', password='njk1234', created=time.time())
        user.save()
        total = User.objects.count()
        print('total。。。。。。。')
        print(total)
        # 模拟错误正常记录是3条
        self.assertEqual(3, total, 'add user fail!')

