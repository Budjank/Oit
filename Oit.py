#!/usr/bin/python
# Author  :  D3n0l  Ganz
# Team    :  Indonesian Sad Cyber
# Version :  1.0
# Date    :  27/09/2018

import sys
import httplib
import socket
import os
import sys
import time

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()
class warna:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

class oit():
    print ""
    print warna.HEADER + "\t\t##########################################" + warna.ENDC
    print warna.HEADER + "\t\t#     Author  :  D3n0l Ganz              #" + warna.ENDC
    print warna.HEADER + "\t\t#     Team    :  Indonesian Sad Cyber    #" + warna.ENDC
    print warna.HEADER + "\t\t#     Version :  V.1                     #" + warna.ENDC
    print warna.HEADER + "\t\t#     Date    :  27/09/2018              #" + warna.ENDC
    print warna.HEADER + "\t\t##########################################" + warna.ENDC
    print ""
    print warna.YELLOW + "\t\t[01] CBT-E" + warna.RED
    print warna.BLUE + "\t\t[02] SDCreator" + warna.RED
    print ""
oit = raw_input(warna.GREEN + "Pilih >> " + warna.ENDC)
if oit == "01" or oit == "1":
    os.system("""
    clear
    cd
    rm -rf CBT-E
    pkg install git python2
    git clone https://github.com/Budjank/CBT-E
    cd
    cd CBT-E
    python2 cbt.py
    """)
elif oit == "02" or oit == "2":
    os.system("""
    clear
    cd
    rm -rf SDCreator
    pkg install git python2
    git clone https://github.com/Budjank/SDCreator
    cd
    cd SDCreator
    python2 sdc.py
    """)
else:
    print warna.RED + "Pilih yg bnr gblk" + warna.ENDC
    time.sleep(2)
    restart_program()
