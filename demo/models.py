from django.db import models


# 创建表
# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

#用户表
class User(models.Model):
    user_name = models.CharField(max_length=30,primary_key=True)#设置主健
    psw = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
