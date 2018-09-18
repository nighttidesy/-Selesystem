#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author: heaven

class Teacher(object):
    '''讲师类,定义讲师姓名,讲师登录密码,性别，年龄,工资,电话'''
    def __init__(self,teacher_name,teacher_passwd,teacher_gender,teacher_age,teacher_salary,teacher_phonenumber):
        self.teacher_name = teacher_name
        self.teacher_passwd = teacher_passwd
        self.teacher_gender = teacher_gender
        self.teacher_age = teacher_age
        self.teacher_salary = teacher_salary
        self.teacher_phonenumber = teacher_phonenumber
        