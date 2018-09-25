#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author heaven

import sys,os,logging
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BASE_DIR)

from core.main import Mainprogram


if __name__ == '__main__':
    selectsystem = Mainprogram()
    selectsystem.run()

        
    
    
    
