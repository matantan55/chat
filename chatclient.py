from tkinter import *
import socket
import os
str_ip = ""
file_name = "admin_ip"
the_path = os.path.abspath(file_name)
ip = open(file_name, "r")
for i in ip:
    str_ip += i
int_port = 0
port_name = "admin_port"
port_path = os.path.abspath(port_name)
port = open(port_path, "r")
for i in port:
    int_port = i
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((str_ip, int(int_port)))
clientSocket.send("connect".encode())
dataFromServer = clientSocket.recv(1024)
x = dataFromServer.decode()
window = Tk()
window.title("client chat")
window.geometry('900x450')
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
mas = txt.get()
clientSocket.send(mas.encode())
lbl = Label(window, text="your message: " + mas)
lbl.grid(column=0, row=1)
lbl2 = Label(window, text="admin message: " + x)
lbl2.grid(column=0, row=2)


def clicked():
    res = txt.get()
    clientSocket.send(res.encode())
    data_from_server2 = clientSocket.recv(1024)
    x2 = data_from_server2.decode()
    lbl.configure(text="your message: " + res)
    lbl2.configure(text="admin message: " + x2)


btn = Button(window, text='Click here to send:', command=clicked)
btn.grid(column=0, row=0)
window.mainloop()

