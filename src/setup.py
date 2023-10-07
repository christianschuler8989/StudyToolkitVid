# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 09:58:56 2023

@author: Domi
"""

import os
import shutil


dirs = ["./../projects",
"./../projects/exampleProject/mediaEditing",
"./../projects/exampleProject/mediaEditing/input",
"./../projects/exampleProject/mediaEditing/temp",
"./../projects/exampleProject/mediaEditing/output",

"./../projects/exampleProject/studySetup",
"./../projects/exampleProject/studySetup/input",
"./../projects/exampleProject/studySetup/temp",
"./../projects/exampleProject/studySetup/output",

"./../projects/exampleProject/statisticalAnalysis"
"./../projects/exampleProject/statisticalAnalysis/input",
"./../projects/exampleProject/statisticalAnalysis/temp",
"./../projects/exampleProject/statisticalAnalysis/output",
"./../projects/exampleProject/studySetup/study/video",
"./../projects/exampleProject/studySetup/study/config"]


def setupWorkplace():
    for dir_to_create in dirs:
        if not os.path.exists(dir_to_create):
            os.makedirs(dir_to_create)
    
    shutil.copytree('./../examples/mediaEditing/', './../projects/exampleProject/mediaEditing/input/', dirs_exist_ok  = True)
    shutil.copytree('./../examples/studySetup/study/', './../projects/exampleProject/studySetup/study/', dirs_exist_ok = True) 