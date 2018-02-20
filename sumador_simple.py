#!/usr/bin/python3
"""
Simple HTTP Server version 2: reuses the port, so it can be
restarted right after it has been killed. Accepts connects from
the outside world, by binding to the primary interface of the host.

Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import calculadora

# Create a TCP objet socket and bind it to a port
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Let the port be reused if no process is actually using it
#Añadimos cosas adicionales
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostname(), 1236))

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')

        bytes_received = recvSocket.recv(2048)
        request = str(bytes_received,'utf-8')
        print('TROCEO PARA OBTENER LOS OPERANDOS')
        resource = request.split()[1]

        if resource != '/favicon.ico':

            op1 = resource.split('/')[1]
            operacion = resource.split('/')[2]
            op2 = resource.split('/')[3]

            if operacion == 'suma':
                resultado = calculadora.suma(op1,op2)

            elif operacion == 'resta':
                resultado = calculadora.resta(op1,op2)

            elif operacion == 'multiplicacion':
                resultado = calculadora.multiplicacion(op1,op2)

            elif operacion == 'division':
                resultado = calculadora.division(op1,op2)

            else:
                resultado = "NO SE CONOCE ESA OPERACION"

        else:
            print('FAVICON: NO HAGO NADA: continuo-----------------------------------')

        print('Answering back...')

        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + "EL resultado es: " + str(resultado), "utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
