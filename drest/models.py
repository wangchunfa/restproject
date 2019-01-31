from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=10, default='ls', )
    password = models.CharField(max_length=100, default='toor', )

    class Meta:
        # 这个表示数据表的内容按创建时间排序
        ordering = ('created',)

