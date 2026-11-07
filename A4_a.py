# Course: IT3883/Section 01
# Student Name:Ria Reddy
# Assignment 4
# Due Date: 11/6/26
# Purpose: A asks user for string, B makes uppercase. B sends it back to A, A prints it.

import socket

#hardwired
host = "127.0.0.1"
port = 45000

#Ask user input
message = input("Enter a message: ")

#Connect A-B
with socket.create_connection((host, port)) as client:
    # new line marks end
    client.sendall((message + "\n").encode("utf-8"))

#Read B
    with client.makefile("r", encoding="utf-8") as reply_file:
        reply = reply_file.readline()

#Print B
print("Reply from Program B:", reply.rstrip("\n"))