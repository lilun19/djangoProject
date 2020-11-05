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

class Student(models.Model):
    '''学生成绩'''
    student_id = models.CharField(max_length=30, verbose_name="学号")
    name = models.CharField(max_length=30, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    score = models.IntegerField(verbose_name="分数")

    class Meta:
        verbose_name = "学生成绩"
        verbose_name_plural = verbose_name