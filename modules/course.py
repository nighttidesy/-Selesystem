#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author: heaven

class Course(object):
    '''课程类,定义课程名称，周期，价格'''
    def __init__(self,course_name,course_cycle,course_price):
        self.course_name = course_name
        self.cource_cycle = course_cycle
        self.course_price = course_price