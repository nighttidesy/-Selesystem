#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
#author: heaven

class Student(object):
    '''学生类,定义学生的姓名,登录密码,性别,年龄,缴费状态（默认是False）'''
    def __init__(self,student_name,student_passwd,student_gender,student_age,paycost_status=False):
        self.student_name = student_name
        self.student_passwd = student_passwd
        self.student_gender = student_gender
        self.student_age = student_age
        self.paycost_status = paycost_status
        
        
