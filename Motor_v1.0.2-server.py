
#!/usr/bin/env python

import os
import sys
import socket

#if not os.getegid() == 0:
#    sys.exit('O programa precisar roda com permissao de root')

"""
from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
"""
__author__ = "Ewerton Leandro de Sousa"
__copyright__ = "Copyright 2016"
__credits__ = ["Ewerton Leandro de Sousa"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = __author__
__email__ = "3w3rt0n@gmail.com"

"""
#Definicao das porta que estao ligadas ao motor A
MotorA1 = port.PA7
MotorA2 = port.PA8

#Definicao das porta que estao ligadas ao motor B
MotorB1 = port.PA9
MotorB2 = port.PA10

#Inicializar GPIO
gpio.init()

#Configura as portas como saida
gpio.setcfg(MotorA1, gpio.OUTPUT)
gpio.setcfg(MotorA2, gpio.OUTPUT)

gpio.setcfg(MotorB1, gpio.OUTPUT)
gpio.setcfg(MotorB2, gpio.OUTPUT)

gpio.output(MotorA1, 0)
gpio.output(MotorA2, 0)
gpio.output(MotorB1, 0)
gpio.output(MotorB2, 0)
"""

UDP_IP = "127.0.0.1"
UDP_PORT = 5001
  
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

print "Aguardando conexao!"
 
try:
    print ("Conectado!")
    print ("Pressione CTRL+C para sair!")
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print "Comando recebido:", data
		
        if data == "0": #PARADO
            print "Parado!"
            """gpio.output(MotorA1, 0)
            gpio.output(MotorA2, 0)
            gpio.output(MotorB1, 0)
            gpio.output(MotorB2, 0)"""
            
		
        if data == "1": 
           print "Esquerda!"
        """#ESQUERDA           
           gpio.output(MotorB1, 0)
           gpio.output(MotorB2, 0)
           gpio.output(MotorA2, 0)
           gpio.output(MotorA1, 1)
           """
           
        
        if data == "2": 
           print "Direita!"
        """#DIREITA
           gpio.output(MotorA2, 0)
           gpio.output(MotorA1, 0)
           gpio.output(MotorB2, 0)
           gpio.output(MotorB1, 1)
           """
           
		   
        if data == "3": 
           print "Frente!"
        """#FRENTE
           gpio.output(MotorA2, 0)
           gpio.output(MotorB2, 0)
           gpio.output(MotorA1, 1)
           gpio.output(MotorB1, 1)"""
           
		   
        if data == "4": 
           print "Traz!"
        """#TRAZ
           gpio.output(MotorA1, 0)
           gpio.output(MotorB1, 0)
           gpio.output(MotorA2, 1)
           gpio.output(MotorB2, 1)"""
           
		   
		   
except KeyboardInterrupt:
    print ("Fim!")
