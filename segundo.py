from mc_core import *
import socket
import sys
import pickle


print("===============INICIA EL PROCESO DE GENERAR LLAVES===================")
print("Genera llave privada...")
tPriv = privateKeyH84()
print("Genera llave publica...")
tPub = publicKeyH84(tPriv.makeGPrime())


print("===============INICIA EL PROCESO DE ENVIO DE LLAVES PUBLICAS===================")


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)
x=0
while True:
    if x != 2:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        print('connection from', client_address)

    else:
        break

    while True:
        print("quiere seguir conectado?")
        print("si (si se desea seguir enviado llaves publicas) (1)")
        print("no (si ya se desconecto el cliente) (2)")
        x = input()
        if x==1:
            # Receive the data in small chunks and retransmit it
            data = connection.recv(80)
            print('received {!r}'.format(data))
            if data:
                print('enviado llave publica al cliente...')
                llave=pickle.dumps(tPub, pickle.HIGHEST_PROTOCOL) #transforma la llave (que es un objeto) a bytes
                connection.sendall(llave)
                break

            else:
                print('no data from', client_address)
                sock.close()
                break

        elif x==2:
            sock.close()
            break

print("=================== INICIA PROCESO DE RECIBO DE ARCHIVOS CIFRADOS Y DECIFRADO======================")

CHUNK_SIZE = 10 * 1024
FILE = "Encriptado1.txt.ctxt"
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('', 50007)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)
b=0
while True:
    if b != 2:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        print('connection from', client_address)
    
    else:
        break

    while True:
        print("quiere seguir conectado?")
        print("si (si se desea seguir recibiendo archivos encriptados ) (1)")
        print("no (si ya se desconecto el cliente) (2)")
        b = input()
        if b==1:
            f=open(FILE, "ab") 
            chunk = sock.recv(CHUNK_SIZE)
            while chunk:
                f.write(chunk)
                chunk = sock.recv(CHUNK_SIZE)
            tPriv.decryptFile("Encriptado1.txt.ctxt")


        elif b==2:
            sock.close()
            break





    

