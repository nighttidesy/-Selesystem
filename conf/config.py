#!/usr/bin/env python3
# -*- encoding = utf-8 -*-
#author: heaven

import os,sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))


DBDIR = "/home/python"

#存放学校信息目录
SCHOOL_DATADIR = BASE_DIR + "/data/school/"


if __name__ == '__main__':
    print(SCHOOL_DATADIR)
