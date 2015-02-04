#-------------------------------------------------------------------------------
# Name:        Basic Scanner
# Purpose:     Understand how to scan a networl.
#
# Author:      Vasanth
#
# Created:     03/02/2015
#-------------------------------------------------------------------------------

import socket, subprocess

#----------------Scanning Methods----------------#

def fullNetworkScan():  # scans for all of the computers with responding ICMP replies
    ipNetworkMask = processNetworkMask(socket.gethostbyname(socket.gethostname()))
    upComputers = []
    for i in range(13):
        if checkIfUp(ipNetworkMask+str(i)):
            print "[+] Checking computers by using a ping request/response"
            upComputers.append(ipNetworkMask+str(i))
    for i in range(len(upComputers)):
        for j in range(1):
            print "[+] Checking first 1 ports on host "+upComputers[i]
            connectScan(upComputers[i],80)

def connectScan(host, port):    # simple 1 host scan

    if not checkIfUp(host): # check if host is up by using ping requests
        print "[-] Host is not replying to ping requests"
        yesorno = raw_input("[*] Do you want to continue?")
        if not("y" in yesorno or "Y" in yesorno):
            return;

    else:
        print "[+] Host is replying to ping requests"
    try:
        socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketObject.connect((host,port))
        print "[+] Port " + str(port) + " open on " + host
        socketObject.close()
    except:
        print "[-] Port " + str(port) + " not open on " + host

def rangeScan(ip1,ip2): # range of ip's to scan
    first = processIpAddress(ip1)
    second = processIpAddress(ip2)
    ipNetworkMask = processNetworkMask(socket.gethostbyname(socket.gethostname()))
    upComputers = []
    print "[+] Checking computers by using a ping request/response"
    for a in range(second-first):
        if checkIfUp(ipNetworkMask+str(first + a)):

            upComputers.append(ipNetworkMask+str(first + a))
    for i in range(len(upComputers)):
        for j in range(100):
            print "[+] Checking first 100 ports on host "+upComputers[i]
            connectScan(upComputers[i],j)

#----------------Different Helper Methods----------------#
def checkIfUp(host):    # check if a host is up by using a ping/ICMP request
    ping = subprocess.Popen(
        ["ping", "-n" ,host],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )

    out, error = ping.communicate()
    print out
    if ("(0% loss" in out):
        return True
    elif ("Request" in out):
        return False
    else:
        return True

def processNetworkMask(ipaddress): # process a network mask ie: pass --> 10.0.0.24 return --> 10.0.0.
    networkmasklist = ipaddress.split(".")
    networkmasklist.pop(len(networkmasklist)-1)
    networkmask = ".".join(networkmasklist)+"."
    return networkmask

def processIpAddress(a): # give an int and it will return an ip address ie: pass --> 10.0.0.32 return --> 32
    networkmasklist = a.split(".")
    networkmasklist.pop(0)
    networkmasklist.pop(0)
    networkmasklist.pop(0)
    last =int(networkmasklist[0])
    return last

#----------------Main Method----------------#

def main():
    print "Welcome to Network Mapping tool!"
    print "1 - Specific CPU Network Scan"
    print "2 - Full Network Scan"
#    print "3 - Range Network Scan"
    print "4 - Check Computer Ping Response"
    inputfromuser = int(raw_input("Please enter option: ")) #ask for user's input
    if (inputfromuser == 1):
        host = raw_input("Please give me host ip: ")
        port = int(raw_input("Please give me port or leave empty for wide range: "))
        connectScan(host,port)


    if (inputfromuser == 2):
        fullNetworkScan()

    if (inputfromuser == 3):
        range1= int(raw_input("Give me the first ip address in range: "))
        range2= int(raw_input("Give me the second ip address in range: "))





    if (inputfromuser == 4):
        host = raw_input("Please give me host ip: ")
        checkIfUp(host)
if __name__ == '__main__':
    main()
