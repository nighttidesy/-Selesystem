#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author heaven

import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BASE_DIR)


def main_page():
    while True:	
        first_page = '''
            欢迎进入选课系统
            
            1.学生登录
            2.讲师登录
            3.管理员登录	
            q.退出
            '''	
        print('{}'.format(first_page))
        yourinput = str(input("请选择：")).strip()
        if yourinput == "1":
            print("student");
        elif yourinput == "2":
            print("teacher");
        elif yourinput == "3":
            administrator_page();
        elif yourinput == "q":
            exit();
        else:
            print("您的输入不正确，请重新输入。")

def administrator_page():
    page1count = '''
    1.创建讲师
    2.创建课程
    3.创建学校
    4.查看学校列表及详细信息
    r.返回上级
    q.退出
    '''
    print(page1count);
    yourinput = str(input("请选择：")).strip();
    if yourinput == "1":
        print("创建讲师 ");
    elif yourinput == "2":
        print("创建课程");
    elif yourinput == "3":
        print("创建学校");
        
    elif yourinput == "4":
        print("查看信息");
    elif yourinput == "r":
        main_page();
    elif yourinput == "q":
        exit();

def create_school():
    school_name = str(input("请输入学校名称: ")).strip()
    school_addr = str(input("请输入学校地址: ")).strip()
    school_addr = str(input("请输入学校地址: ")).strip()

        
        
        
        
main_page()

        
    
    
    
