#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
#author: heaven

import os,sys,logging


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))


DBDIR = "/home/python"

#存放学校信息目录
SCHOOL_DATADIR = BASE_DIR + "/data/school/"

#日志配置
LOGFILE = BASE_DIR + "/logs/service.log"

logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename=LOGFILE,
                    filemode='a+')


if __name__ == '__main__':
    print(SCHOOL_DATADIR)
