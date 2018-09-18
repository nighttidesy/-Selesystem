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

#此脚本用于初始化系统以及生成测试数据


#初始化系统,清除数据
def init_system():
    os.rename(SCHOOL_DATADIR + "school.db",SCHOOL_DATADIR + "school.db.bak")
    
 
#生成测试数据
def create_test_data():
    schooldata = shelve.open(SCHOOL_DATADIR + "school.db",writeback = True)
    
    newschool1 = School("清华","北京")
    newschool2 = School("武大","武汉")
    newschool3 = School("川大","四川")
    
    newcourse1 = Course("java全站开发","5个月","20000元")
    newcourse2 = Course("python自动化运维","4个月","30000元")
    newcourse3 = Course("大数据","5个月","50000元")
    
    newteacher1 = Teacher("讲师马云A","123456","男","30","20000","13211114444")
    newteacher2 = Teacher("讲师马云B","123456","男","30","20000","13211114444")
    newteacher3 = Teacher("讲师马云C","123456","男","30","20000","13211114444")
    newteacher4 = Teacher("讲师马云D","123456","男","30","20000","13211114444")
    newteacher5 = Teacher("讲师马云E","123456","男","30","20000","13211114444")
    
    newgrade1 = Grade("1班","讲师马云A","java全站开发")
    newgrade2 = Grade("2班","讲师马云B","python自动化运维")
    newgrade3 = Grade("3班","讲师马云C","大数据")
    
    newstudent1 = Student("周杰伦1","123456","男","22","False")
    newstudent2 = Student("周杰伦2","123456","男","22","False")
    newstudent3 = Student("周杰伦3","123456","男","22","False")
    newstudent4 = Student("周杰伦4","123456","男","22","False")
    newstudent5 = Student("周杰伦5","123456","男","22","False")
    newstudent6 = Student("周杰伦6","123456","男","22","False")
    newstudent7 = Student("周杰伦7","123456","男","22","False")
    newstudent8 = Student("周杰伦8","123456","男","22","False")
    newstudent9 = Student("周杰伦9","123456","男","22","False")
    
    newgrade1.grade_student["周杰伦1"] = newstudent1
    newgrade1.grade_student["周杰伦2"] = newstudent2
    newgrade1.grade_student["周杰伦3"] = newstudent3
    newgrade1.grade_student["周杰伦4"] = newstudent4
    newgrade1.grade_student["周杰伦5"] = newstudent5
    newgrade1.grade_student["周杰伦6"] = newstudent6
    newgrade1.grade_student["周杰伦7"] = newstudent7
    newgrade1.grade_student["周杰伦8"] = newstudent8
    newgrade1.grade_student["周杰伦9"] = newstudent9
    
    newschool1.school_course["java全站开发"] = newcourse1
    newschool1.school_course["python自动化运维"] = newcourse2
    newschool1.school_course["大数据"] = newcourse3

    newschool1.school_grade["1班"] = newgrade1
    newschool1.school_grade["2班"] = newgrade2
    newschool1.school_grade["3班"] = newgrade3
    
    
    newschool1.school_teacher["讲师马云A"] = newteacher1
    newschool1.school_teacher["讲师马云B"] = newteacher2
    newschool1.school_teacher["讲师马云C"] = newteacher3
    newschool1.school_teacher["讲师马云D"] = newteacher4
    newschool1.school_teacher["讲师马云E"] = newteacher5
    
    
    schooldata["清华"] = newschool1
    schooldata["武大"] = newschool2
    schooldata["川大"] = newschool3
    schooldata.close()
    
    
    
if __name__ == "__main__":
    init_system()
    create_test_data()
    


    
    
    
    
