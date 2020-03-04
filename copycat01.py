#!/usr/bin/env python3

#import additional code
import shutil
import os

#move to different directory to start
os.chdir("/home/student/mycode")
#copy file
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#copy dir
shutil.copytree("5g_research/", "5g_research_backup/")
