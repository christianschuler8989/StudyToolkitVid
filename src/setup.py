# -*- coding: utf-8 -*-
# StudyToolkitVid - Setup
# 
# Authors: Christian Schuler & Dominik Hauser & Anran Wang
################################################################################

import os
import shutil


# Creating the directories for a new project
def setupDirectories(projectName):
    dirs = [
    "./../projects",
    "./../projects/"+projectName+"/mediaEditing",
    "./../projects/"+projectName+"/mediaEditing/input",
    "./../projects/"+projectName+"/mediaEditing/temp",
    "./../projects/"+projectName+"/mediaEditing/output",
    "./../projects/"+projectName+"/studySetup",
    "./../projects/"+projectName+"/studySetup/input",
    "./../projects/"+projectName+"/studySetup/temp",
    "./../projects/"+projectName+"/studySetup/output",
    "./../projects/"+projectName+"/statisticalAnalysis",
    "./../projects/"+projectName+"/statisticalAnalysis/input",
    "./../projects/"+projectName+"/statisticalAnalysis/temp",
    "./../projects/"+projectName+"/statisticalAnalysis/output",
    "./../projects/"+projectName+"/studySetup/study/video",
    "./../projects/"+projectName+"/studySetup/study/config"
    ]

    for dir_to_create in dirs:
        if not os.path.exists(dir_to_create):
            os.makedirs(dir_to_create)

# Copying the example media files into the project directory
def setupExampleFiles(projectName):
    shutil.copytree('./../examples/mediaEditing/', 
                    './../projects/'+projectName+'/mediaEditing/input/', 
                    dirs_exist_ok  = True)
    shutil.copytree('./../examples/studySetup/study/', 
                    './../projects/'+projectName+'/studySetup/study/', 
                    dirs_exist_ok = True)     


# Complete setup for the exampleProject
def setupWorkplace(projectName="exampleProject"):
    dirs = [
    "./../projects",
    "./../projects/"+projectName+"/mediaEditing",
    "./../projects/"+projectName+"/mediaEditing/input",
    "./../projects/"+projectName+"/mediaEditing/temp",
    "./../projects/"+projectName+"/mediaEditing/output",
    "./../projects/"+projectName+"/studySetup",
    "./../projects/"+projectName+"/studySetup/input",
    "./../projects/"+projectName+"/studySetup/temp",
    "./../projects/"+projectName+"/studySetup/output",
    "./../projects/"+projectName+"/statisticalAnalysis",
    "./../projects/"+projectName+"/statisticalAnalysis/input",
    "./../projects/"+projectName+"/statisticalAnalysis/temp",
    "./../projects/"+projectName+"/statisticalAnalysis/output",
    "./../projects/"+projectName+"/studySetup/study/video",
    "./../projects/"+projectName+"/studySetup/study/config"
    ]

    for dir_to_create in dirs:
        if not os.path.exists(dir_to_create):
            os.makedirs(dir_to_create)
    
    shutil.copytree('./../examples/mediaEditing/', 
                    './../projects/'+projectName+'/mediaEditing/input/', 
                    dirs_exist_ok  = True)
    shutil.copytree('./../examples/studySetup/study/', 
                    './../projects/'+projectName+'/studySetup/study/', 
                    dirs_exist_ok = True) 