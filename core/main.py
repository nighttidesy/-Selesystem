#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author: heaven

import os,sys,shelve,time

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
        logging.debug('program begain running...')
        while True:
            logging.debug('进入选课系统')
            mainpage = '''
                欢迎进入选课系统
                
                1.学员视图
                2.讲师视图
                3.管理员
                q.退出
            '''
            print('\033[1;35m{}\033[0m'.format(mainpage))
            yourinput = input("\033[1;35m请输入你的选择： \033[0m").strip()
            logging.debug('你的选择: ' + yourinput)
            if yourinput == "1":
                studen_view_obj = Student_view()
                studen_view_obj.run_student_view()
#                Student_view()
            elif yourinput == "2":
                teacher_view_obj = Teacher_view()
                teacher_view_obj.run_teacher_view()
#                Teacher_view()
            elif yourinput == "3":
                admin_view_obj = Admin_view()
                admin_view_obj.run_admin_view()
#                Admin_view()            最开始使用这种方式，后面发现虽然也能达到效果但是不符合规范，而且当需要调用另外一个类中的方法的时候就会很麻烦
            elif yourinput == "q":
                logging.info('退出系统')
                sys.exit()
                
            else:
                print("\033[1;31m您的输入不正确。\033[0m")
                logging.error('您的输入不正确')
            
class Student_view(object):
    '''学员视图类，提供注册,交学费,上课等功能'''
    def __init__(self):
#        with shelve.open(SCHOOL_DATADIR + "school.db",writeback = True ) as self.schooldata:
#            self.run_student_view()        
#        self.schooldata = shelve.open(SCHOOL_DATADIR + "school.db",writeback = True)
         self.admin_view_obj = Admin_view()
    def __del__(self):
        self.admin_view_obj.schooldata.close()
        logging.info('调用student_view __del__')
    def run_student_view(self):
        logging.info('running run_student_view')
        self.admin_view_obj.school_list()                                                            #展示学校列表
        self.your_choiseschool1 = input("\033[1;35m 请输入你要进入的学校：\033[0m").strip()
        logging.info('您输入的学校: ' + self.your_choiseschool1)
        self.your_choiseschool_obj = self.admin_view_obj.schooldata[self.your_choiseschool1]         #将选择学校实例赋值个一个变量your_choiseschool_obj方便调用，这步可能有点绕
               
        for i in self.your_choiseschool_obj.school_grade:                                             #展示该学校当前开设课程
            grade_obj = self.your_choiseschool_obj.school_grade[i]
            print('''\033[1;35m
            班级名称: {}
            班级所开课程: {}
            班级讲师: {}
            \n\n\033[0m'''.format(grade_obj.grade_name,grade_obj.grade_course,grade_obj.grade_teacher))
            
        
        self.your_choisegrade = str(input("\033[1;35m请输入你要登录的班级: \033[0m").strip())
        logging.info('您要登录的班级' + self.your_choisegrade)
        self.grade_obj = self.admin_view_obj.schooldata[self.your_choiseschool1].school_grade[self.your_choisegrade]                    #实例化一个班级实例
        print('\033[1;35m欢迎来到 国际精英培训学院{}分院 \033[0m'.format(self.your_choiseschool1))
        logging.info('进入国际精英培训学院' + self.your_choiseschool1 + '分院')
        while True:
            student_view_page = '''
            1:学员注册
            2:学员登录
            3:学员注销
            r:返回上一级
            q:退出登录
            '''
            student_view_page_data = {
            '1':'student_registered',
            '2':'student_login',
            '3':'student_del',
            }
            print('\033[1;35m\n\n{}\n\n\033[0m'.format(student_view_page))
            your_input4 = str(input("\033[1;35m请选择：  \033[0m").strip())
            if your_input4 == "r":
                self.admin_view_obj.schooldata.close()                #这个操作很重要,在退出这个页面返回到上个页面时候如果不关闭这个文件，在返回上级进入其他视图的时候就会报错，因为当一个文件通过shelve打开后，如果没有关闭这个状态,便不能再通过shelve再去打开。
                break
            if your_input4 == "q":
                self.admin_view_obj.exit_program()
            if hasattr(self,student_view_page_data[your_input4]):
                getattr(self,student_view_page_data[your_input4])()
            else:
                print("\033[1;35m您的输入有误 !\033[0m")
                logging.error('您的输入有误' + your_input4)
                        
    def student_registered(self):
        '''学员注册'''
        logging.info('开始学员注册')
        student_name = str(input("\033[1;35m请输入你的姓名 \033[0m").strip())
        if student_name in self.grade_obj.grade_student:
            print("\033[1;35m该学生已经存在。 \033[0m")
            logging.error('该学生已经存在' + student_name)
        else:
            student_passwd = str(input("\033[1;35m请设置你的用户密码: \033[0m").strip())
            student_gender = str(input("\033[1;35m请设置你的性别: \033[0m").strip())
            student_age = str(input("\033[1;35m请输入你的年龄: \033[0m").strip())
            self.grade_obj.add_grade_student(student_name,student_passwd,student_gender,student_age)
            print('''\033[1;35m\n恭喜添加{}用户成功.\n\n
            您所在的班级是: {}
            您报名的课程是: {}
            您的班级讲师是: {}\033[0m'''.format(student_name,self.your_choisegrade,self.grade_obj.grade_course,self.grade_obj.grade_teacher))
            logging.info(student_name + '用户添加注册成功')
 
    def student_login(self):
        '''学员登录'''
        logging.info('开始学员登录')
        student_name = str(input("\033[1;35m请输入你的姓名 \033[0m").strip())
        student_passwd = str(input("\033[1;35m请输入你的密码 \033[0m").strip())
        self.student_obj = self.grade_obj.grade_student[student_name]                     #实例化学生对象
        while True:    
            if student_name  in self.grade_obj.grade_student and student_passwd == self.student_obj.student_passwd:
                student_page = '''
                1.上课打卡            
                2.缴费
                3.提交作业
                4.查看我的信息
                5.修改我的信息
                6.提问
                7.下课打卡
                r.返回上级
                q.退出
                '''
                student_page_data = {
                    '1':'studen_clock_in',
                    '2':'studen_paycost',
                    '3':'studen_submitjob',
                    '4':'studen_info',
                    '5':'studen_changeinfo',
                    '6':'studen_askquestions',
                    '7':'studen_clock_out'
                }
                
                print("\033[1;35m恭喜你登陆成功，欢迎您{}\n{} \033[0m".format(student_name,student_page))
                logging.info(student_name + '登录成功')
                your_input5 = str(input("\033[1;35m请输入你的选择:  \033[0m").strip())
                if your_input5 == "r":
                    break
                if your_input5 == "q":   
                    self.admin_view_obj.exit_program()
                if hasattr(self,student_page_data[your_input5]):
                    getattr(self,student_page_data[your_input5])()
                else:
                    print("\033[1;35m您的输入不正确。 \033[0m")
                    logging.error('您的输入不正确' + your_input5)
                
            else:    
                print("\033[1;35m您输入的用户不存在或者密码错误。 \033[0m")
                logging.error('您输入的用户不存在或者密码错误' + student_name)
            
            
        
    def student_del(self):
        '''学员注销'''
        print("学员注销")
        input_name = str(input("\033[1;35m请输入注销用户的用户名: \033[0m").strip())
        input_passwd = str(input("\033[1;35m请输入注销用户的用户密码: \033[0m").strip())
        if input_name in self.grade_obj.grade_student and input_passwd == self.student_obj.student_passwd:
            self.grade_obj.grade_student.pop[input_name]
            print("\033[1;35m用户{}删除成功 \033[0m".format(input_name))
            logging.info('用户' + input_name + '删除成功')
        else:
            print("\033[1;35m您输入的用户不存在或者密码错误. \033[0m".format(input_name))
            logging.error('您输入的用户不存在或者密码错误' + input_name)
    def studen_clock_in(self):
        '''上课打卡'''
        print("上课打卡成功")
        logging.info('上课打卡成功')
    def studen_clock_out(self):
        '''下课打卡'''
        print("下课打卡成功")
        logging.info('下课打卡成功')
    def studen_paycost(self):
        '''缴费'''
        logging.info('开始缴费')
        course_obj1 = self.admin_view_obj.schooldata[self.your_choiseschool1].school_course[self.grade_obj.grade_course]                #实例化当前课程,这一步需要仔细琢磨，我们是需要获取到我们存储在School类中school_course字典中的课程对象
        print("\033[1;35m你报名的课程是{},需要支付{}元 \033[0m".format(self.grade_obj.grade_course,course_obj1.course_price))
        logging.info('你报名的课程是' + self.grade_obj.grade_course + ',需要支付' + course_obj1.course_price + '元')
        your_input6 = str(input("\033[1;35m确认支付请输入yes|YES，输入其他视为放弃支付。 \033[0m").strip())
        if your_input6 == "yes" or "YES":
            print("\033[1;34m 正在链接银行......请稍等。\033[0m")
            logging.info('正在链接银行......请稍等')
            print("\033[1;34m正在支付...... \033[0m")
            logging.info('正在支付......')
            time.sleep(2)
            self.student_obj.paycost_status = True
            print("\033[1;34m 恭喜你 ，支付完成，你已经缴费成功\033[0m")
            logging.info('支付完成，你已经缴费成功')
            
        else:
            print("\033[1;34m 您的输入有误。\033[0m")
            logging.error('您的输入有误')
            
    def studen_submitjob(self):
        '''提交作业'''
        print("提交作业成功")
        logging.info('提交作业成功')
    def studen_info(self):
        '''查看个人信息'''
        logging.info('查看个人信息')
        print(  '''\033[1;34m\n\n您的详细信息如下: \n\n\n
        您的姓名: {}
        您的性别: {}
        您的年龄: {}
        您所在的班级: {}
        您所报课程: {}
        您的缴费状态: {}
        
        \033[0m'''.format(self.student_obj.student_name,self.student_obj.student_gender,self.student_obj.student_age,self.grade_obj.grade_name,self.grade_obj.grade_course,self.student_obj.paycost_status))
        
        
    def studen_changeinfo(self):
        '''修改个人信息'''
        print("修改个人信息")
        logging.info('修改个人信息')
    def studen_askquestions(self):
        '''提问'''
        print("提问")
        logging.info('提问')
        
class Teacher_view(object):
    '''讲师视图类,拥有讲课功能，能查看交班级学生名单及成绩'''
    def __init__(self):
        self.admin_view_obj = Admin_view()
    def __del__(self):
        self.admin_view_obj.schooldata.close()
    
    def run_teacher_view(self): 
        logging.info('running run_teacher_view')
        self.admin_view_obj.school_list()                                                            #展示学校列表
        self.your_choiseschool1 = input("\033[1;35m 请输入你要进入的学校：\033[0m").strip()
        if self.your_choiseschool1 in self.admin_view_obj.schooldata:
            self.your_choiseschool_obj = self.admin_view_obj.schooldata[self.your_choiseschool1]
            teacher_name = str(input("\033[1;35m 请输入你的讲师姓名：\033[0m").strip())
            teacher_passwd = str(input("\033[1;35m 请输入你的登录密码：\033[0m").strip())
            if teacher_name in self.your_choiseschool_obj.school_teacher and teacher_passwd ==  self.your_choiseschool_obj.school_teacher[teacher_name].teacher_passwd:    # 判断讲师存在,且密码正确
                self.teacher_obj = self.your_choiseschool_obj.school_teacher[teacher_name]          #实例化讲师对象
                print("\033[1;35m{}讲师,欢迎你\033[0m".format(teacher_name))
                logging.info('讲师登录成功，' + teacher_name)
                while True:
                    teacher_page = '''
                        1.讲课
                        2.查看个人信息
                        3.查看班级学生名单
                        4.查看学生成绩
                        5.修改个人信息
                        r.返回上一级
                        q.退出登录
                    '''
                    teacher_page_data = {
                    '1':'teacher_teaching',
                    '2':'teacher_info',
                    '3':'student_list',
                    '4':'student_chengji',
                    '5':'change_teacherinfo'
                    }
                     
                    print("\033[1;35m{}\033[0m".format(teacher_page))
                    your_input7 = str(input("\033[1;35m 请输入你的选择：\033[0m").strip())
                    if your_input7 == "r":
                        self.admin_view_obj.schooldata.close()
                        break
                    if your_input7 == "q":
                        self.admin_view_obj.exit_program()
                    if hasattr(self,teacher_page_data[your_input7]):
                        getattr(self,teacher_page_data[your_input7])()
                    else:
                        print("\033[1;35m您的输入有误。\033[0m")
                        logging.error('您的输入有误。' + your_input7)
            
            
            
            else:
                print("\033[1;35m您的输的账户不存在或者密码错误。\033[0m")
                logging.error('您的输的账户不存在或者密码错误')
        else:
            print("\033[1;35m您的输入有误。\033[0m")
            logging.error('您的输入有误。' + self.your_choiseschool1)
        
    def teacher_teaching(self):
        '''讲课'''
        print("\033[1;35m开始讲课 \033[0m")
        logging.info('开始讲课')
        time.sleep(2)
        
    def teacher_info(self):
        '''讲师个人信息'''
        logging.info('查看讲师个人信息' + self.teacher_obj.teacher_name)
        print('''\033[1;35m\n讲师个人信息如下:  
        讲师名称：{}
        讲师性别：{}
        讲师年龄：{}
        讲师工资：{}
        讲师电话号码：{}
        \033[0m'''.format(self.teacher_obj.teacher_name,self.teacher_obj.teacher_gender,self.teacher_obj.teacher_age,self.teacher_obj.teacher_salary,self.teacher_obj.teacher_phonenumber))
        
    def student_list(self):
        '''班级学生名单'''
        logging.info('查看班级学生名单')
        print("\033[1;35m 当前的班级如下: \033[0m")
        for i in self.your_choiseschool_obj.school_grade:
            print("\033[1;34m{}\033[0m".format(i))
        your_input8 = str(input("\033[1;35m请输入你要查看的班级名: \033[0m").strip())
        if your_input8 in self.your_choiseschool_obj.school_grade:
            grade_obj = self.your_choiseschool_obj.school_grade[your_input8]              #实例化班级对象,班级中存放了学生对象字典grade_student
            print("\033[1;34m\n\n{}学生列表如下: \033[0m".format(your_input8))
            for j in grade_obj.grade_student:
                student_obj = grade_obj.grade_student[j]
                print('''\033[1;35m
                姓名: {}  性别: {}  年龄: {}  缴费状态: {} 
                \033[0m'''.format(student_obj.student_name,student_obj.student_gender,student_obj.student_age,student_obj.paycost_status))
        else:
            print("\033[1;35m您的输入有误。\033[0m")
        
        
    def student_chengji(self):
        '''查看学生成绩'''
        print("学生成绩列表（这个的方法和学生缴费的方法类似，鉴于时间问题，就不写了）")            
        
    def change_teacherinfo(self):
        '''修改讲师个人信息'''
        logging.info('修改讲师个人信息')
        print("\033[1;35m注意: 修改讲师个人信息,不能修改姓名,姓名需与之前一样。 \033[0m。")
        teacher_name = str(input("\033[1;35m请输入讲师姓名:\033[0m").strip())
        teacher_passwd = str(input("\033[1;35m请输入讲师登录密码:\033[0m").strip())
        teacher_gender = str(input("\033[1;35m请输入讲师性别:\033[0m").strip())
        teacher_age = str(input("\033[1;35m请输入讲师年龄:\033[0m").strip())
        teacher_phonenumber = str(input("\033[1;35m请输入讲师电话号码:\033[0m").strip())
        print('\033[1;35m你输入的信息如下: \n 姓名: {}\n性别: {}\n年龄: {}\n电话号码: {}\033[0m'.format(teacher_name,teacher_gender,teacher_age,teacher_salary,teacher_phonenumber))
        your_input = str(input("\033[1;35m确认请输入yes|YES，输入其他视为取消修改。 :\033[0m").strip())
        if your_input == "yes" or "YES":
            self.teacher_obj.teacher_name = teacher_name
            self.teacher_obj.teacher_passwd = teacher_passwd
            self.teacher_obj.teacher_gender = teacher_gender
            self.teacher_obj.teacher_age = teacher_age
            self.teacher_obj.teacher_phonenumber = teacher_phonenumber
            print('\033[1;35m 修改讲师{}信息成功\033[0m'.format(teacher_name))
            logging.info('修改讲师' + teacher_name + '信息成功')
            
        
        else:
            print("\033[1;35m您取消了修改 \033[0m")
            logging.info('您取消了修改')
        
        
        
class Admin_view(object):
    '''管理员视图类,创建/删除讲师 创建/删除班级 创建/删除学校 创建/删除课程 创建/删除讲师'''
    def __init__(self):
 #       if os.path.exists(SCHOOL_DATADIR + "school.db"):
        self.schooldata = shelve.open(SCHOOL_DATADIR + "school.db",writeback = True)
 #      with shelve.open(SCHOOL_DATADIR + "school.db",writeback = True ) as self.schooldata:
 #          pass
 #           self.run_admin_view()
 #       else:
 #           print("school.db文件不存在")
    def __del__(self):
        self.schooldata.close()
        logging.info('调用Admin_view __del__')
    def run_admin_view(self):
        logging.info('running run_admin_view')
        while True:
            logging.info('进入管理视图')
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
                self.schooldata.close()
                break
            if yourinput in admin_view_page_data:
                if hasattr(self,admin_view_page_data[yourinput]):
                    getattr(self,admin_view_page_data[yourinput])()
            
            else:
                print("\033[1;31m您的输入不正确。\033[0m")
                logging.error('您的输入不正确' + yourinput)
                continue
    
    def add_school(self):                 #添加学校
        logging.info('开始添加学校')
        school_name = str(input("\033[1;35m请输入学校名称: \033[0m").strip())
        if school_name in self.schooldata:
            print("\033[1;31m该学校已经创建。\033[0m")
            logging.error('该学校已经创建')
        else:
            school_addr = str(input("\033[1;35m请输入学校地址: \033[0m").strip())                
            self.schooldata[school_name] = School(school_name,school_addr)                      #将学校对象存储于school.db文件中，通过shelve存储模式
            print("\033[1;32m学校添加成功。\033[0m")
            logging.info('学校添加成功')

    def school_list(self):
        '''显示学校列表'''
        print("\033[1;34m当前学校列表如下： \n\033[0m")
        logging.info('显示学校列表')
        for i in self.schooldata:
            print('\033[1;34m国际精英培训学院{}分院\033[0m'.format(i))
    
    def del_school(self):
        '''删除学校'''
        logging.info('开始删除学校')
        getattr(self,"school_list")()
        your_input = str(input("\033[1;31m请输入你要删除的学校名称(输入对应分校的名称就行，如国际精英培训学院山城分院，就只需要输入山城。): \033[0m").strip())
        print('\033[1;31m你将要删除学校: {}\033[0m'.format(your_input))
        if your_input in self.schooldata:
            your_comfirm = str(input("\033[1;31m确认请输入yes|YES,输入其他视为放弃。\033[0m").strip())
            if your_comfirm == "yes" or "YES":
                del self.schooldata[your_input]
                print('\033[1;31m删除学校{}成功\033[0m'.format(your_input))
                logging.info('删除学校' + your_input + '成功')
            else:
                print("\033[1;31m您取消了删除操作。\033[0m")
                logging.info('您取消了删除操作')
        else:
            print("\033[1;31m你输入的学校不存在。\033[0m")
            logging.error('你输入的学校不存在')
    def manage_school(self):
        '''管理学校'''
        logging.info('进入管理学校')
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
                    logging.error('你的输入有误' + your_choise1)
            else:
                print("\033[1;35m 您输入的学校不存在\033[0m")
                logging.error('你输入的学校不存在')
                break
            
        
    def add_teacher(self):                #添加讲师
        logging.info('添加讲师')
        teacher_name = str(input("\033[1;35m请输入讲师姓名:\033[0m").strip())
        teacher_passwd = str(input("\033[1;35m请输入讲师登录密码:\033[0m").strip())
        teacher_gender = str(input("\033[1;35m请输入讲师性别:\033[0m").strip())
        teacher_age = str(input("\033[1;35m请输入讲师年龄:\033[0m").strip())
        teacher_salary = str(input("\033[1;35m请输入讲师工资:\033[0m").strip())
        teacher_phonenumber = str(input("\033[1;35m请输入讲师电话号码:\033[0m").strip())
        print('\033[1;35m你输入的信息如下: \n 姓名: {}\n性别: {}\n年龄: {}\n工资: {}\n电话号码: {}\033[0m'.format(teacher_name,teacher_gender,teacher_age,teacher_salary,teacher_phonenumber))
        your_input = str(input("\033[1;35m确认请输入yes|YES，重新输入请输入 r,退出请输入 q。 :\033[0m").strip())
        if your_input == "yes" or "YES":
            self.school_obj.add_schoolteacher(teacher_name,teacher_passwd,teacher_gender,teacher_age,teacher_salary,teacher_phonenumber)
            print('\033[1;35m 添加讲师{}成功\033[0m'.format(teacher_name))
            logging.info('添加讲师成功' + teacher_name)
        elif your_input == "r":
            getattr("add_teacher")
        elif your_input == "q":
            getattr("exit_program")
        else:
            print("\033[1;35m您的输入有误 \033[0m")
            logging.error('你的输入有误' + your_input)
        
    def add_grade(self):                  #添加班级
        logging.info('添加班级')   
        grade_name = str(input("\033[1;35m请输入班级名称:\033[0m").strip())
        if grade_name in self.school_obj.school_grade:
            print("\033[1;35m您添加的班级已经存在。 \033[0m")
            logging.error('您添加的班级已经存在' + grade_name)
        else:
            getattr(self,'see_teacher_list')()
            grade_teacher = str(input("\033[1;35m请为班级分配讲师（输入讲师姓名）: \033[0m").strip())
            getattr(self,'see_course_list')()
            grade_course = str(input("\033[1;35m请输入班级开班课程（输入课程名称）: \033[0m").strip())
            self.school_obj.add_schoolgrade(grade_name,grade_teacher,grade_course)
            print("\033[1;35m班级添加成功 \033[0m")
            logging.info('添加班级成功' + grade_name)
        
    def add_course(self):                  #添加课程
        logging.info('添加课程')
        course_name = str(input("\033[1;35m请输入添加的课程名称:\033[0m").strip())
        if course_name in self.school_obj.school_course:
            print("\033[1;35m您添加的课程已经存在。 \033[0m")
            logging.error('您添加的班级已经存在' + course_name)
        else:
            cource_cycle = str(input("\033[1;35m请输入添加的课程的周期:\033[0m").strip())
            course_price = str(input("\033[1;35m请输入添加的课程的价格:\033[0m").strip())
            self.school_obj.add_schoolcourse(course_name,cource_cycle,course_price)
            print("\033[1;35m课程添加成功 \033[0m")
            logging.info('添加课程成功' + course_name)
    def see_teacher_list(self):             #查看讲师列表
        logging.info('查看讲师列表')
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
        logging.info('查看班级列表')
        print("\033[1;35m本校当前班级列表如下: \033[0m")
        for i in self.school_obj.school_grade:
            grade_obj = self.school_obj.school_grade[i]
            print('''\033[1;35m
            班级名称: {}
            班级所开课程: {}
            班级讲师: {}
            \n\n\033[0m'''.format(grade_obj.grade_name,grade_obj.grade_course,grade_obj.grade_teacher))
        
    def see_course_list(self):             #查看课程列表
        logging.info('查看课程列表')
        print("\033[1;35m 当前学校开设课程情况如下: \033[0m")
        for i in self.school_obj.school_course:
            course_obj = self.school_obj.school_course[i]
            print('''\033[1;35m
            课程名称: {}
            课程周期: {}
            课程价格: {}
            
            \n\n\033[0m'''.format(course_obj.course_name,course_obj.cource_cycle,course_obj.course_price))
        
    def del_teacher(self):                #删除讲师
        logging.info('删除讲师')
        getattr(self,'see_teacher_list')()
        your_input1 = str(input("\033[1;35m请输入你要删除的讲师姓名: \033[0m").strip())
        if your_input1 in self.school_obj.school_teacher:
            self.school_obj.school_teacher.pop(your_input1)
            print('\033[1;35m讲师{}删除成功。 \033[0m'.format(your_input1))
            logging.info('删除讲师成功' + your_input1)
        else:
            print("\033[1;35m你输入的讲师不存在。\033[0m")
            logging.error('您输入的讲师不存在' + your_input1)
        pass
        
    def del_grade(self):                  #删除班级
        logging.info('删除班级')
        getattr(self,'see_grade_list')()
        your_input3 = str(input("\033[1;35m请输入你要删除的班级名称: \033[0m").strip())
        if your_input3 in self.school_obj.school_grade:
            self.school_obj.school_grade.pop(your_input3)
            print('\033[1;35m班级{}删除成功。 \033[0m'.format(your_input3))
            logging.info('删除班级成功' + your_input3)
        else:
            print("\033[1;35m你输入的班级不存在。\033[0m")
            logging.error('您输入的讲师不存在' + your_input3)
        
    def del_course(self):                  #删除课程
        logging.info('删除课程')
        getattr(self,'see_course_list')()
        your_input2 = str(input("\033[1;35m请输入你要删除的课程名称: \033[0m").strip())
        if your_input2 in self.school_obj.school_course:
            self.school_obj.school_course.pop(your_input2)
            print('\033[1;35m课程{}删除成功。 \033[0m'.format(your_input2))
            logging.info('删除课程成功' + your_input2)
        else:
            print("\033[1;35m你输入的课程不存在。\033[0m")
            logging.error('您删除的讲师不存在' + your_input2)
    def return_previouspage(self):         #返回 通过映射功能返回上一级，么有实现这个，貌似直接将break写到这个函数里面并不管用，后续继续研究方法。
        
        pass
     
    def exit_program(self):               #退出选课系统
        self.schooldata.close()
        logging.info('退出选课系统')
        sys.exit("\033[1;32m拜拜。。0.0  感谢使用选课系统! ^.^\033[0m")
        
        
        
    
    
    
if __name__ == "__main__":
    selectsystem = Mainprogram()
    selectsystem.run()
        
        
        
        
        
        
        
        
        
