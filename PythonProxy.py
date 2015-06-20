import thread
import socket
import time

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TARGET_HOST = str(raw_input("[?] Type target IP Address: "))
TARGET_PORT = int(raw_input("[?] Type target port: "))


def process_data(data):
    data = list(map(''.join, list(zip(* [iter(data)] * 2))))
    return_data = ""
    while 1:
        temp_list = []
        for i in range(0, 8):
            if(len(data) == 0):
                break
            character = data.pop(0)
            return_data += character
            temp_list.append(character)
        return_data += "\t\t"
        for characters in temp_list:
            return_data += characters.decode("hex")
        return_data += "\n"
        if len(data) == 0:
            break
    return return_data


def recieve_send_data_thread(socket_object_reciever, socket_object_sender):
    while 1:
        recieved_data = socket_object_reciever.recv(6000)
        if(recieved_data):
            print(("[*] Recieved data from " +
                socket_object_reciever.getpeername()[0] + ":"))
            print((process_data(recieved_data.encode("hex"))))
            print(("[*] Sending data to " + socket_object_sender.getpeername()[0]))
            socket_object_sender.send(recieved_data)

try:
    socket_client.connect((TARGET_HOST, TARGET_PORT))
    print("[+] Successfully connected to target host")
except socket.error as msg:
    print(("[-] Error connecting to target host: " + msg))
try:
    socket_server.bind(("", 12345))
    print("[+] Successfully created a server socket")
except socket.error as msg:
    print(("[-] Server error: " + msg[1]))

socket_server.listen(1)
print("[*] Listening on port 12345")

connection_to_client, address_of_client = socket_server.accept()
print(("[+] Connected with " + address_of_client[0] + str(
    address_of_client[1])))



thread.start_new_thread(recieve_send_data_thread,
    (socket_client, connection_to_client, ))
thread.start_new_thread(recieve_send_data_thread,
    (connection_to_client, socket_client, ))
while 1:
    pass

