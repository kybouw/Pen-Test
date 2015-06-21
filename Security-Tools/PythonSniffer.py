import socket
import os
import thread

# A list of ip protocols that are associated wih their
#number, in this case, the index number
protocols = ["HOPOPT","ICMP","IGMP","GGP","IP-in-IP","ST","TCP ","CBT ","EGP ","IGP ","BBN-RCC-MON ","NVP-II ","PUP ","ARGUS ","EMCON ","XNET ","CHAOS ","UDP ","MUX ","DCN-MEAS ","HMP ","PRM ","XNS-IDP","TRUNK-1 ","TRUNK-2 ","LEAF-1 ","LEAF-2 ","RDP ","IRTP ","ISO-TP4 ","NETBLT ","MFE-NSP ","MERIT-INP ","DCCP ","3PC ","IDPR ","XTP ","DDP ","IDPR-CMTP ","TP++ ","IL ","IPv6 ","SDRP ","IPv6-Route ","IPv6-Frag ","IDRP ","RSVP ","GRE ","MHRP ","BNA ","ESP ","AH ","I-NLSP ","SWIPE ","NARP ","MOBILE ","TLSP ","SKIP ","IPv6-ICMP ","IPv6-NoNxt ","IPv6-Opts "," ","CFTP ","","SAT-EXPAK ","KRYPTOLAN ","RVD ","IPPC ","","SAT-MON ","VISA ","IPCU ","CPNX ","CPHB ","WSN ","PVP ","BR-SAT-MON ","SUN-ND ","WB-MON ","WB-EXPAK ","ISO-IP ","VMTP ","SECURE-VMTP ","VINES ","TTP ","NSFNET-IGP ","DGP ","TCF TCF ","EIGRP ","OSPF ","Sprite-RPC ","LARP ","MTP ","AX.25 ","IPIP ","MICP ","SCC-SP ","ETHERIP ","ENCAP "," ","GMTP","IFMP ","PNNI ","PIM ","ARIS ","SCPS ","QNX ","A/N ","IPComp ","SNP ","Compaq-Peer ","IPX-in-IP ","VRRP ","PGM "," ","L2TP ","DDX ","IATP ","STP ","SRP ","UTI ","SMP ","SM ","PTP ","IS-IS ","FIRE ","CRTP ","CRUDP ","SSCOPMCE ","IPLT ","SPS ","PIPE ","SCTP ","FC ","RSVP-E2E-IGNORE ","Mobility ","UDPLite","MPLS-in-IP","manet","HIP","Shim6","WESP","ROHC "]
def threaded_main(socket_object):
    
    counter = True
    while 1:
	escape = False
        print "Listening..."
        data = socket_object.recvfrom(65565)[0]

		
        print("")
        print "[+] Packet Captured!!"
        if counter:
            print "-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-"
        else:
            print "#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#"
        counter = not(counter)
        list_of_hex = []
        for i in range(len(data)):
            if not("x" in repr(data[i])):
                list_of_hex.append("0x" + data[i].encode("hex"))
            else:
                list_of_hex.append("0x" + repr(data[i])[-3:-1])
        if "nt" in os.name:
            sniffer_socket_object.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

	'''while not(escape):
		try:
			for t in range(20):
				print (copied_list_of_hex.pop(0)),
			print
		except:
			escape = True'''
	print list_of_hex

        # Horrible coding. Just the worst, but it works. :/

        # Basically, this is a dictionary, and the values are little
        # python commands that print out the IP data from a packet.
        IPSTRUCTURE ={
            "version": "print int((str(bin(" + list_of_hex[0] + "))[:5]).replace(\"b\",\"\"), 2)",
            "HDRLength": "print int(str(bin(" + list_of_hex[0] + "))[-4:], 2)*4",
            "service": "print list_of_hex[1]",
            "total_length": "print (str(bin(" + list_of_hex[2] + "))).replace(\"b\",\"\")" +
            " + str(eval(bin(" + list_of_hex[3] + ")))",
            "identification": "print (list_of_hex[4] + list_of_hex[5][2:])",
            "flags": "print(list_of_hex[6])",
            "fragmentoffset": "print(list_of_hex[7])",
            "ttl": "print(str(int(\"" + list_of_hex[8] + "\", 16)))",
            "protocol": "print((str(int(\"" + list_of_hex[9] + "\", 16))) + \" : \" + protocols[int(\"" + list_of_hex[9] + "\", 16)])",
            "checksum": "print(list_of_hex[10]+list_of_hex[11][2:])",
            "ip_src": "print((str(int(\"" + list_of_hex[12] + "\", 16))) + \".\" + (str(int(\"" + list_of_hex[13] + "\", 16))) + \".\" + (str(int(\"" + list_of_hex[14] + "\", 16)))+ \".\" + (str(int(\"" + list_of_hex[15] + "\", 16))))",
            "ip_dest": "print((str(int(\"" + list_of_hex[16] + "\", 16))) + \".\" + (str(int(\"" + list_of_hex[17] + "\", 16))) + \".\" + (str(int(\"" + list_of_hex[18] + "\", 16)))+ \".\" + (str(int(\"" + list_of_hex[19] + "\", 16))))"
            }

        print("")


        # Here, I call each value with a given key in the dictionary above, and execute
        # different commands listed.

        print "Version: \t\t",
        exec(IPSTRUCTURE["version"])

        print "Header Length: \t\t",
        exec(IPSTRUCTURE["HDRLength"])

        print "Service: \t\t",
        exec(IPSTRUCTURE["service"])

        print "Total Length: \t\t",
        exec(IPSTRUCTURE["total_length"])

        print "Identification: \t",
        exec(IPSTRUCTURE["identification"])

        print "Flags: \t\t\t",
        exec(IPSTRUCTURE["flags"])

        print "Fragment Offset: \t",
        exec(IPSTRUCTURE["fragmentoffset"])

        print "Time To Live: \t\t",
        exec(IPSTRUCTURE["ttl"])

        print "Protocol: \t\t",
        exec(IPSTRUCTURE["protocol"])

        print "Checksum: \t\t",
        exec(IPSTRUCTURE["checksum"])

        print "IP Source: \t\t",
        exec(IPSTRUCTURE["ip_src"])

        print "IP Destination: \t",
        exec(IPSTRUCTURE["ip_dest"])

host = str(raw_input("[?] What is the ip address of this computer: "))

if "nt" in os.name:
    socket_protocol = socket.IPPROTO_IP
    sniffer_socket_object = socket.socket(
        socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer_socket_object.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    sniffer_socket_object.bind((host, 0))
    sniffer_socket_object.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    thread.start_new_thread(threaded_main, (sniffer_socket_object, ))

else:
    socket_protocol_icmp = socket.IPPROTO_ICMP
    socket_protocol_tcp = socket.IPPROTO_TCP
    socket_protocol_udp = socket.IPPROTO_UDP

    sniffer_socket_object_tcp = socket.socket(
        socket.AF_INET, socket.SOCK_RAW, socket_protocol_tcp)
    sniffer_socket_object_udp = socket.socket(
        socket.AF_INET, socket.SOCK_RAW, socket_protocol_udp)
    sniffer_socket_object_icmp = socket.socket(
        socket.AF_INET, socket.SOCK_RAW, socket_protocol_icmp)

    sniffer_socket_object_icmp.bind((host, 0))
    sniffer_socket_object_tcp.bind((host, 0))
    sniffer_socket_object_udp.bind((host, 0))
    thread.start_new_thread(threaded_main, (sniffer_socket_object_tcp, ))
    thread.start_new_thread(threaded_main, (sniffer_socket_object_udp, ))
    thread.start_new_thread(threaded_main, (sniffer_socket_object_icmp, ))



while 1:
    pass