#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author: heaven

from modules.student import Student

class Grade(object):
    '''班级类，定义班级类名称,班级讲师，绑定班级课程,班级包含的学生'''
    def __init__(self,grade_name,grade_teacher,grade_course):
        self.grade_name = grade_name
        self.grade_teacher = grade_teacher
        self.grade_course = grade_course
        self.grade_student = {}
        
    def add_grade_student(self,student_name,student_passwd,student_gender,student_age):
        newstudent = Student(student_name,student_passwd,student_gender,student_age)
        self.grade_student[student_name] = newstudent
        
    
        
    