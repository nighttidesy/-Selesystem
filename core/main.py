#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author: heaven

import os,sys,shelve

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from conf.config     import *
from modules.school  import School
from modules.course  import Course
from modules.grade   import Grade
from modules.student import Student
from modules.teacher import Teacher


class Mainprogram(object):
    '''程序接入类'''
    def __init__(self):
        pass
    
    def run(self):
        while True:
            mainpage = '''
                欢迎进入选课系统
                
                1.学员视图
                2.讲师视图
                3.管理员
                q.退出
            '''
            print('\033[1;35m{}\033[0m'.format(mainpage))
            yourinput = input("\033[1;35m请输入你的选择： \033[0m").strip()
            if yourinput == "1":
                Student_view()
            elif yourinput == "2":
                Teacher_view()
            elif yourinput == "3":
                Admin_view()
            elif yourinput == "q":
                sys.exit()
            else:
                print("\033[1;31m您的输入不正确。\033[0m")
            
class Student_view(object):
    '''学员视图类，提供注册,交学费,上课等功能'''
    def __init__(self):
#        with shelve.open(SCHOOL_DATADIR + "school.db",writeback = True ) as self.schooldata:
#            self.run_student_view()        
        self.run_student_view() 
    def run_student_view(self):
        print("进入学员视图")
        admin_view_obj = Admin_view()
        admin_view_obj.school_list()
        your_choiseschool1 = input("\033[1;35m 请输入你要登录的学校：\033[0m").strip()
        while True:
            student_view_page = '''
            1:学员注册
            2:学员登录
            '''
            sudent_view_page_data = {
            '1':'student_registered',
            '2':'student_login'
            }
            
            
    def student_registered(self):
        '''学员注册'''
        pass
        
    def student_login(self):
        '''学员登录'''
        pass
        
class Teacher_view(object):
    '''讲师视图类,拥有讲课功能，能查看交班级学生名单及成绩'''
    def __init__(self):
        self.run_teacher_view()
        pass
    def run_teacher_view(self):
        print("进入讲师视图")

        
        
class Admin_view(object):
    '''管理员视图类,创建/删除讲师 创建/删除班级 创建/删除学校 创建/删除课程 创建/删除讲师'''
    def __init__(self):
 #       if os.path.exists(SCHOOL_DATADIR + "school.db"):
        with shelve.open(SCHOOL_DATADIR + "school.db",writeback = True ) as self.schooldata:
            self.run_admin_view()
 #       else:
 #           print("school.db文件不存在")
    def run_admin_view(self):
        while True:
            
            admin_view_page = '''
            1:添加学校
            2:管理学校
            3:查看学校列表
            4:删除学校
            r:返回上一级
            q:退出 
            '''
            #将序号与方法通过字典关系起来
            admin_view_page_data = {
            '1':'add_school',
            '2':'manage_school',
            '3':'school_list',
            '4':'del_school',
            'q':'exit_program'
            }
            
            print('\033[1;35m{}\033[0m'.format(admin_view_page))
            yourinput = input("\033[1;35m 请输入你的选择：\033[0m").strip()
            
            if yourinput == "r":
                break
            if yourinput in admin_view_page_data:
                if hasattr(self,admin_view_page_data[yourinput]):
                    getattr(self,admin_view_page_data[yourinput])()
            
            else:
                print("\033[1;31m您的输入不正确。\033[0m")
                continue
    
    def add_school(self):                 #添加学校
        
        print("添加学校")
        school_name = str(input("\033[1;35m请输入学校名称: \033[0m").strip())
        if school_name in self.schooldata:
            print("\033[1;31m该学校已经创建。\033[0m")
            
        else:
            school_addr = str(input("\033[1;35m请输入学校地址: \033[0m").strip())                
            self.schooldata[school_name] = School(school_name,school_addr)                      #将学校对象存储于school.db文件中，通过shelve存储模式
            print("\033[1;32m学校添加成功。\033[0m")

    def school_list(self):
        '''显示学校列表'''
        print("\033[1;34m当前学校列表如下： \n\033[0m")
        for i in self.schooldata:
            print('\033[1;34m国际精英培训学院{}分院\033[0m'.format(i))
    
    def del_school(self):
        '''删除学校'''
        getattr(self,"school_list")()
        your_input = str(input("\033[1;31m请输入你要删除的学校名称(输入对应分校的名称就行，如国际精英培训学院山城分院，就只需要输入山城。): \033[0m").strip())
        print('\033[1;31m你将要删除学校: {}\033[0m'.format(your_input))
        if your_input in self.schooldata:
            your_comfirm = str(input("\033[1;31m确认请输入yes|YES,输入其他视为放弃。\033[0m").strip())
            if your_comfirm == "yes" or "YES":
                del self.schooldata[your_input]
                print('\033[1;31m删除学校{}成功\033[0m'.format(your_input))
            else:
                print("\033[1;31m您取消了删除操作。\033[0m")
        else:
            print("\033[1;31m你输入的学校不存在。\033[0m")
    def manage_school(self):
        '''管理学校'''
        getattr(self,"school_list")()
        your_choiseschool = str(input("\033[1;35m请输入你要管理的学校名称(输入对应分校的名称就行，如国际精英培训学院山城分院，就只需要输入山城。): \033[0m").strip())
        while True:
            if your_choiseschool in self.schooldata:
                self.school_obj = self.schooldata[your_choiseschool]   #将当前选择的学校对象传递给school_obj
                print('\033[1;35m 欢迎来到国际精英人才培训学院{}分院 \033[0m \n\n'.format(your_choiseschool))
                manage_school_page = '''
                
                1:添加讲师
                2:添加班级
                3:添加课程
                4:查看讲师列表
                5:查看班级列表
                6:查看学校开设课程列表
                7:删除讲师
                8:删除班级
                9:删除课程
                r:返回上级
                q:退出程序
                
                '''
                
                #将序号与方法通过字典关系起来
                manage_school_page_data = {
                '1':'add_teacher',
                '2':'add_grade',
                '3':'add_course',
                '4':'see_teacher_list',
                '5':'see_grade_list',
                '6':'see_course_list',
                '7':'del_teacher',
                '8':'del_grade',
                '9':'del_course',               
                'q':'exit_program'
                }
                
                print('\033[1;35m {} \033[0m'.format(manage_school_page))
                your_choise1 = str(input("\033[1;35m 请输入你的选择： \033[0m").strip())
                if your_choise1 == 'r':
                    break
                if hasattr(self,manage_school_page_data[your_choise1]):
                    getattr(self,manage_school_page_data[your_choise1])()
                else:
                    print("\033[1;31m您的输入有误\033[0m")
            else:
                print("\033[1;35m 您输入的学校不存在\033[0m")
            
        
    def add_teacher(self):                #添加讲师

        teacher_name = str(input("\033[1;35m请输入讲师姓名:\033[0m").strip())
        teacher_gender = str(input("\033[1;35m请输入讲师性别:\033[0m").strip())
        teacher_age = str(input("\033[1;35m请输入讲师年龄:\033[0m").strip())
        teacher_salary = str(input("\033[1;35m请输入讲师工资:\033[0m").strip())
        teacher_phonenumber = str(input("\033[1;35m请输入讲师电话号码:\033[0m").strip())
        print('\033[1;35m你输入的信息如下: \n 姓名: {}\n性别: {}\n年龄: {}\n工资: {}\n电话号码: {}\033[0m'.format(teacher_name,teacher_gender,teacher_age,teacher_salary,teacher_phonenumber))
        your_input = str(input("\033[1;35m确认请输入yes|YES，重新输入请输入 r,退出请输入 q。 :\033[0m").strip())
        if your_input == "yes" or "YES":
            self.school_obj.add_schoolteacher(teacher_name,teacher_gender,teacher_age,teacher_salary,teacher_phonenumber)
            print('\033[1;35m 添加讲师{}成功\033[0m'.format(teacher_name))
            
        elif your_input == "r":
            getattr("add_teacher")
        elif your_input == "q":
            getattr("exit_program")
        else:
            print("\033[1;35m您的输入有误 \033[0m")
        
        
        pass
        
    def add_grade(self):                  #添加班级
        print("添加班级")
        grade_name = str(input("\033[1;35m请输入班级名称:\033[0m").strip())
        if grade_name in self.school_obj.school_grade:
            print("\033[1;35m您添加的班级已经存在。 \033[0m")
        else:
            getattr(self,'see_teacher_list')()
            grade_teacher = str(input("\033[1;35m请为班级分配讲师（输入讲师姓名）: \033[0m").strip())
            getattr(self,'see_course_list')()
            grade_course = str(input("\033[1;35m请输入班级开班课程（输入课程名称）: \033[0m").strip())
            self.school_obj.add_schoolgrade(grade_name,grade_teacher,grade_course)
            print("\033[1;35m班级添加成功 \033[0m")
        
    def add_course(self):                  #添加课程
        print("添加课程")
        course_name = str(input("\033[1;35m请输入添加的课程名称:\033[0m").strip())
        if course_name in self.school_obj.school_course:
            print("\033[1;35m您添加的课程已经存在。 \033[0m")
        else:
            cource_cycle = str(input("\033[1;35m请输入添加的课程的周期:\033[0m").strip())
            course_price = str(input("\033[1;35m请输入添加的课程的价格:\033[0m").strip())
            self.school_obj.add_schoolcourse(course_name,cource_cycle,course_price)
            print("\033[1;35m课程添加成功 \033[0m")
        
    def see_teacher_list(self):             #查看讲师列表
        print("\033[1;35m本校当前教师列表如下: \033[0m")
        for i in self.school_obj.school_teacher:
            teacher_obj = self.school_obj.school_teacher[i]
            print('''\033[1;35m
            讲师名称：{}
            讲师性别：{}
            讲师年龄：{}
            讲师工资：{}
            讲师电话号码：{}
             \n\n\n\033[0m'''.format(teacher_obj.teacher_name,teacher_obj.teacher_gender,teacher_obj.teacher_age,teacher_obj.teacher_salary,teacher_obj.teacher_phonenumber))
            
        
    def see_grade_list(self):             #查看班级列表
        print("\033[1;35m本校当前班级列表如下: \033[0m")
        for i in self.school_obj.school_grade:
            grade_obj = self.school_obj.school_grade[i]
            print('''\033[1;35m
            班级名称: {}
            班级所开课程: {}
            班级讲师: {}
            \n\n\033[0m'''.format(grade_obj.grade_name,grade_obj.grade_course,grade_obj.grade_teacher))
        
    def see_course_list(self):             #查看课程列表
        print("\033[1;35m 当前学校开设课程情况如下: \033[0m")
        for i in self.school_obj.school_course:
            course_obj = self.school_obj.school_course[i]
            print('''\033[1;35m
            课程名称: {}
            课程周期: {}
            课程价格: {}
            
            \n\n\033[0m'''.format(course_obj.course_name,course_obj.cource_cycle,course_obj.course_price))
        
    def del_teacher(self):                #删除讲师
        print("删除讲师")
        getattr(self,'see_teacher_list')()
        your_input1 = str(input("\033[1;35m请输入你要删除的讲师姓名: \033[0m").strip())
        if your_input1 in self.school_obj.school_teacher:
            self.school_obj.school_teacher.pop(your_input1)
            print('\033[1;35m讲师{}删除成功。 \033[0m'.format(your_input1))
        else:
            print("\033[1;35m你输入的讲师不存在。\033[0m")
        pass
        
    def del_grade(self):                  #删除班级
        print("删除班级")
        getattr(self,see_grade_list)()
        your_input3 = str(input("\033[1;35m请输入你要删除的班级名称: \033[0m").strip())
        if your_input3 in self.schol_obj.school_grade:
            self.schol_obj.school_grade.pop(your_input3)
            print('\033[1;35m班级{}删除成功。 \033[0m'.format(your_input1))
        else:
            print("\033[1;35m你输入的班级不存在。\033[0m")
        
    def del_course(self):                  #删除课程
        print("删除课程")
        getattr(self,'see_course_list')()
        your_input2 = str(input("\033[1;35m请输入你要删除的课程名称: \033[0m").strip())
        if your_input2 in self.school.school_course:
            self.school_obj.school_course.pop(your_input2)
            print('\033[1;35m课程{}删除成功。 \033[0m'.format(your_input2))
        else:
            print("\033[1;35m你输入的课程不存在。\033[0m")
        
    def return_previouspage(self):         #返回 通过映射功能返回上一级，么有实现这个，貌似直接将break写到这个函数里面并不管用，后续继续研究方法。
        
        pass
     
    def exit_program(self):               #退出选课系统
        sys.exit("\033[1;32m拜拜。。0.0  感谢使用选课系统! ^.^\033[0m")
        
        
        
    
    
    
if __name__ == "__main__":
    selectsystem = Mainprogram()
    selectsystem.run()
        
        
        
        
        
        
        
        
        
