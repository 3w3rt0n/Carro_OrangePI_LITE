#!/usr/bin/env python

import socket
import os

from Tkinter import *


#if not os.getegid() == 0:
#    sys.exit('O programa precisar roda com permissao de root')

__author__ = "Ewerton Leandro de Sousa"
__copyright__ = "Copyright 2016"
__credits__ = ["Ewerton Leandro de Sou_version__ = 1.0.0"]
__maintainer__ = __author__
__email__ = "3w3rt0n@gmail.com"


class Janela(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
        
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
        
        self.pr = False
        self.ip = "127.0.0.1"
        self.port = 5002
        
        self.parent.title("Interface básica - v1.0.1")
        self.pack(fill=BOTH, expand=1)        
    
        self.lb_Endereco = Label(self, text="IP:", width=10)
        self.lb_Endereco.place(x=10, y=10)

        self.en_endereco = Entry(self, width=15)
        self.en_endereco.insert(0, "127.0.0.1")
        self.en_endereco.place(x=100, y=10)

        self.lb_porta = Label(self, text="Porta:", width=10)
        self.lb_porta.place(x=10, y=30)

        self.en_porta = Entry(self, width=15)
        self.en_porta.insert(0, "5001")
        self.en_porta.place(x=100, y=30)

        self.bt_conectar = Button(self, command=self.teste, text="conectar", width=15)
        self.bt_conectar.place(x=200, y=15)
        
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP]
        self.ip = self.en_endereco.get()
        self.port = int(self.en_porta.get())
        #self.sock.bind((self.ip, self.port))
        
    def teste(self):
        self.ip = self.en_endereco.get()
        self.port = int(self.en_porta.get())
        self.sock.sendto("0", (self.ip, self.port))
        
    def enviar(self):
        self.ip = self.en_endereco.get()
        self.port = int(self.en_porta.get())
        self.sock.sendto(MESSAGE, (self.ip, self.port))


def main():
    def teclarPressionar(event):
        
        if event.keysym == 'Right' and app.pr == False:
            app.pr = True
            app.ip = app.en_endereco.get()
            app.port = int(app.en_porta.get())
            app.sock.sendto("2", (app.ip, app.port))
        
        elif event.keysym == 'Down' and app.pr == False:
            app.pr = True
            app.ip = app.en_endereco.get()
            app.port = int(app.en_porta.get())
            app.sock.sendto("3", (app.ip, app.port))
        
        elif event.keysym == 'Up' and app.pr == False:
            app.pr = True
            app.ip = app.en_endereco.get()
            app.port = int(app.en_porta.get())
            app.sock.sendto("4", (app.ip, app.port))
        
        elif event.keysym == 'Left' and app.pr == False:
            app.pr = True
            app.ip = app.en_endereco.get()
            app.port = int(app.en_porta.get())
            app.sock.sendto("1", (app.ip, app.port))
        
        elif event.keysym == 'Escape' or event.keysym == 'Control_L' or event.keysym == 'Shift_L' or event.keysym == 'Alt_L' :
            app.ip = app.en_endereco.get()
            app.port = int(app.en_porta.get())
            app.sock.sendto("0", (app.ip, app.port))   
    
    def teclarSoltar(event):
        if event.keysym == 'Right' or event.keysym == 'Down' or event.keysym == 'Up' or event.keysym == 'Left' or event.keysym == 'Escape' or event.keysym == 'Control_L' or event.keysym == 'Shift_L' or event.keysym == 'Alt_L':
            app.pr = False
            app.ip = app.en_endereco.get()
            app.port = int(app.en_porta.get())
            app.sock.sendto("0", (app.ip, app.port))  
            
        
    #Inicializar Janela     
    root = Tk()
    root.geometry("500x420")
    app = Janela(root)
    app.bind_all("<KeyPress>", teclarPressionar)
    app.bind_all("<KeyRelease>", teclarSoltar)
    root.mainloop()     

if __name__ == '__main__':
    main()

