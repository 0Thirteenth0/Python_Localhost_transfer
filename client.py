import socket
s = socket.socket()
#macbook ("Jiahuis-MacBook-Pro-2.local")
host = input("Enter hosts ip address: ")
port = 8888
s.connect((host,port))
print("Connected...")

