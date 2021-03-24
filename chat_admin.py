from tkinter import *
import socket
import os
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
file_name = "admin_ip"
the_path = os.path.abspath(file_name)
ip = open(file_name, "w+")
ip.readline()
ip.write(IP)
ip.close()
the_port = 0
for port in range(65535):
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        the_port = port
    except:
        print('[OPEN] Port open :', port)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port_name = "admin_port"
port_path = os.path.abspath(port_name)
port = open(port_path, "w+")
port.readline()
port.write(str(the_port))
port.close()
serverSocket.bind((IP, the_port))
serverSocket.listen()
(clientConnected, clientAddress) = serverSocket.accept()
print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))
dataFromClient = clientConnected.recv(1024)
x = dataFromClient.decode()

window = Tk()
window.title("admin chat")
window.geometry('900x450')
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
mas = txt.get()
clientConnected.send(mas.encode())
lbl = Label(window, text="your message: " + mas)
lbl.grid(column=0, row=1)
lbl2 = Label(window, text="client message: " + x)
lbl2.grid(column=0, row=2)


def clicked():
    res = txt.get()
    clientConnected.send(res.encode())
    data_from_client2 = clientConnected.recv(1024)
    x2 = data_from_client2.decode()
    lbl.configure(text="your message: " + res)
    lbl2.configure(text="client message: " + x2)


btn = Button(window, text='Click here to send:', command=clicked)
btn.grid(column=0, row=0)
window.mainloop()

