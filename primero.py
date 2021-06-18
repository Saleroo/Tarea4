# coding=utf-8
import bcrypt
import time
import os
import socket
import sys
import pickle
from mc_core import *

print("=========================Inicio proceso de crackeo==========================")
print("=========================Crackeo archivo 1==========================")
# -a 0: ataque con diccionario
# -m 0: tipo de hash MD5 
os.system('time -p hashcat -a 0 -m 0 -o cracked1.txt archivo_1 diccionario_2.dict')

print("=========================Crackeo archivo 2==========================")
# -a 0: ataque con diccionario
# -m 10: tipo de hash MD5 con salt : md5($pass.$salt)
os.system('time -p hashcat -a 0 -m 10 -o cracked2.txt archivo_2 diccionario_2.dict')

print("=========================Crackeo archivo 3==========================")
# -a 0: ataque con diccionario
# -m 10: tipo de hash MD5 con salt : md5($pass.$salt)
os.system('time -p hashcat -a 0 -m 10 -o cracked3.txt archivo_3 diccionario_2.dict')

print("=========================Crackeo archivo 4==========================")
# -a 0: ataque con diccionario
# -m 1000: tipo de hash NTLM
os.system('time -p hashcat -a 0 -m 1000 -o cracked4.txt archivo_4 diccionario_2.dict')

print("=========================Crackeo archivo 5==========================")
# -a 0: ataque con diccionario
# -m 1800: tipo de hash sha512crypt $6$, SHA512 (Unix)
os.system('time -p hashcat -a 0 -m 1800 -o cracked5.txt archivo_5 diccionario_2.dict')


print("================Inicio de proceso de hasheo de bcrypt==========================")

arreglo1=[]
arreglo2=[]
arreglo3=[]
arreglo4=[]
arreglo5=[]

def cutit(s,n):    
      return s[n:]

while True:
    print("===============================================================================")
    print("Cual archivo desea hasher con bcrypt? ")
    print("archivo 1 (1)")
    print("archivo 2 (2)")
    print("archivo 3 (3)")
    print("archivo 4 (4)")
    print("archivo 5 (5)")
    print("exit(0)")
    opcion = input()
    
    if opcion == '1':
        with open("cracked1.txt") as fname:
            lineas = fname.readlines()
            for linea in lineas:
                arreglo1.append(cutit(linea.strip('\n'),33)) #borrar las primeras 33 lineas del arreglo contraseña y el '\n'
        start = time.time()

       

        for i in range(1000):
            archivo= open('bcryp1.txt', 'a') #crea un nuevo archivo donde se almacenaran las contraseñas hasheadas con bcrypt
            #passwd = bytes(arreglo1[i], encoding = "utf-8")
            passwd=arreglo1[i].encode("utf-8") #transforma las contraseñas de formato string a bytes
            salt = bcrypt.gensalt(rounds=16) #genera el salt
            hashed = bcrypt.hashpw(passwd, salt) #genera el hash
            hashed = hashed.decode(encoding="utf-8") # trandorma las contraseñas de formato bytes a string
            archivo.write(hashed) #escribe en el arechivo el hash
            archivo.write('\n')
            archivo.close()


        end = time.time()
        print('el tiempo que tardo en hacer la operacion fue de : ',end - start,' segundos' )

    elif opcion == '0':
        break

    elif opcion == '2':

        with open("cracked2.txt") as fname:
            lineas = fname.readlines()
            for linea in lineas:
                arreglo2.append(cutit(linea.strip('\n'),50)) #borrar las primeras 50 lineas del arreglo contraseña y el '\n'
        start = time.time()

       

        for i in range(1000):
            archivo= open('bcryp2.txt', 'a') #crea un nuevo archivo donde se almacenaran las contraseñas hasheadas con bcrypt
            #passwd = bytes(arreglo2[i], encoding = "utf-8") #transforma las contraseñas de formato string a bytes
            passwd=arreglo2[i].encode("utf-8") #transforma las contraseñas de formato string a bytes
            salt = bcrypt.gensalt(rounds=16) #genera el salt
            hashed = bcrypt.hashpw(passwd, salt) #genera el hash
            hashed = hashed.decode(encoding="utf-8") # trandorma las contraseñas de formato bytes a string
            archivo.write(hashed) #escribe en el arechivo el hash
            archivo.write('\n')
            archivo.close()


        end = time.time()
        print('el tiempo que tardo en hacer la operacion fue de : ',end - start,' segundos' )

    elif opcion == '3':
        with open("cracked3.txt") as fname:
            lineas = fname.readlines()
            for linea in lineas:
                arreglo3.append(cutit(linea.strip('\n'),50)) #borrar las primeras 50 lineas del arreglo contraseña y el '\n'
        start = time.time()

       

        for i in range(1000):
            archivo= open('bcryp3.txt', 'a') #crea un nuevo archivo donde se almacenaran las contraseñas hasheadas con bcrypt
            #passwd = bytes(arreglo3[i], encoding = "utf-8") #transforma las contraseñas de formato string a bytes
            passwd=arreglo3[i].encode("utf-8") #transforma las contraseñas de formato string a bytes
            salt = bcrypt.gensalt(rounds=16) #genera el salt
            hashed = bcrypt.hashpw(passwd, salt) #genera el hash
            hashed = hashed.decode(encoding="utf-8") # trandorma las contraseñas de formato bytes a string
            archivo.write(hashed) #escribe en el arechivo el hash
            archivo.write('\n')
            archivo.close()


        end = time.time()
        print('el tiempo que tardo en hacer la operacion fue de : ',end - start,' segundos' )        






    elif opcion == '4':

        with open("cracked4.txt") as fname:
            lineas = fname.readlines()
            for linea in lineas:
                arreglo4.append(cutit(linea.strip('\n'),33)) #borrar las primeras 33 lineas del arreglo contraseña y el '\n'
        start = time.time()

       

        for i in range(1000):
            archivo= open('bcryp4.txt', 'a') #crea un nuevo archivo donde se almacenaran las contraseñas hasheadas con bcrypt
            #passwd = bytes(arreglo4[i], encoding = "utf-8") #transforma las contraseñas de formato string a bytes
            passwd=arreglo4[i].encode("utf-8")
            salt = bcrypt.gensalt(rounds=16) #genera el salt
            hashed = bcrypt.hashpw(passwd, salt) #genera el hash
            hashed = hashed.decode(encoding="utf-8") # trandorma las contraseñas de formato bytes a string
            archivo.write(hashed) #escribe en el arechivo el hash
            archivo.write('\n')
            archivo.close()


        end = time.time()
        print('el tiempo que tardo en hacer la operacion fue de : ',end - start,' segundos' )



    elif opcion == '5':

        with open("cracked5.txt") as fname:
            lineas = fname.readlines()
            for linea in lineas:
                arreglo5.append(cutit(linea.strip('\n'),99))             
        start = time.time()

       

        for i in range(20):
            archivo= open('bcryp5.txt', 'a') #crea un nuevo archivo donde se almacenaran las contraseñas hasheadas con bcrypt
            #passwd = bytes(arreglo5[i], encoding = "utf-8") #transforma las contraseñas de formato string a bytes
            passwd=arreglo5[i].encode("utf-8") #transforma las contraseñas de formato string a bytes
            salt = bcrypt.gensalt(rounds=16) #genera el salt
            hashed = bcrypt.hashpw(passwd, salt) #genera el hash
            hashed = hashed.decode(encoding="utf-8") # trandorma las contraseñas de formato bytes a string
            archivo.write(hashed) #escribe en el arechivo el hash
            archivo.write('\n')
            archivo.close()


        end = time.time()
        print('el tiempo que tardo en hacer la operacion fue de : ',end - start,' segundos' )



print("====================INICIA PROCESO DE CONEXION AL SERVIDOR POR MEDIO DE SOCKET ========================")
while True:
    print("===============================================================================")
    print("Cual archivo desea encriptar con McEliece? ")
    print("archivo 1 (1)")
    print("archivo 2 (2)")
    print("archivo 3 (3)")
    print("archivo 4 (4)")
    print("archivo 5 (5)")
    print("exit(0)")
    opcion = input()

    if opcion == '1':
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 10000)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)


        # Send data
        message = b'cliente: necesito la llave publica para el archivo 1'
        print('sending {!r}'.format(message))
        sock.sendall(message)

        data = b""
        # Look for the response

        packet = sock.recv(8000)

        data += packet

        tPub = pickle.loads(data)
        print("llave: ")
        print(tPub)
        print("Encrypting...")
        tPub.encryptFile("bcryp1.txt")
        sock.close()

    elif opcion == '2':
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 10000)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)


        # Send data
        message = b'cliente: necesito la llave publica para el archivo 2'
        print('sending {!r}'.format(message))
        sock.sendall(message)

        data = b""
        # Look for the response

        packet = sock.recv(8000)

        data += packet

        tPub = pickle.loads(data)
        print("llave: ")
        print(tPub)
        print("Encrypting...")
        tPub.encryptFile("bcryp2.txt")
        sock.close()

    elif opcion == '3':
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 10000)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)


        # Send data
        message = b'cliente: necesito la llave publica para el archivo 3'
        print('sending {!r}'.format(message))
        sock.sendall(message)

        data = b""
        # Look for the response

        packet = sock.recv(8000)

        data += packet

        tPub = pickle.loads(data)
        print("llave: ")
        print(tPub)
        print("Encrypting...")
        tPub.encryptFile("bcryp3.txt")
        sock.close()
    
    elif opcion == '4':
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 10000)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)


        # Send data
        message = b'cliente: necesito la llave publica para el archivo 4'
        print('sending {!r}'.format(message))
        sock.sendall(message)

        data = b""
        # Look for the response

        packet = sock.recv(8000)

        data += packet
        tPub = pickle.loads(data)
        print("llave: ")
        print(tPub)
        print("Encrypting...")
        tPub.encryptFile("bcryp4.txt")
        sock.close()

    elif opcion == '5':
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 10000)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)


        # Send data
        message = b'cliente: necesito la llave publica para el archivo 5'
        print('sending {!r}'.format(message))
        sock.sendall(message)

        data = b""
        # Look for the response
        
        packet = sock.recv(8000)

        data += packet
        tPub = pickle.loads(data)
        print("llave: ")
        print(tPub)
        print("Encrypting...")
        tPub.encryptFile("bcryp5.txt")
        sock.close()

    elif opcion == '0':
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 10000)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)

        # Send data
        message = b'cliente desconectado...'
        print('sending {!r}'.format(message))
        sock.sendall(message)
        sock.close()
        break
        
    
print("=================== INICIA PROCESO DE ENVIO CIFRADOS======================")
while True:
    print("===============================================================================")
    print("Cual archivo cifrado desea enviar ? ")
    print("archivo 1 (1)")
    print("archivo 2 (2)")
    print("archivo 3 (3)")
    print("archivo 4 (4)")
    print("archivo 5 (5)")
    print("exit(0)")
    opcion = input()

    if opcion == '1':     
        CHUNK_SIZE = 1024
        FILE = "bcryp1.txt.ctxt"

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('', 50007)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)        
        
        f= open(FILE, 'rb')
        data = f.read(CHUNK_SIZE)
        while data:
            sock.send(data)
            data = f.read(CHUNK_SIZE)
        
        # Cerrar conexión y archivo.
        sock.close()
        f.close()
        print("El archivo 1 ha sido enviado correctamente.")

    if opcion == '2':     
        CHUNK_SIZE = 1024
        FILE = "bcryp2.txt.ctxt"

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('', 50007)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)        
        
        f= open(FILE, 'rb')
        data = f.read(CHUNK_SIZE)
        while data:
            sock.send(data)
            data = f.read(CHUNK_SIZE)
        
        # Cerrar conexión y archivo.
        sock.close()
        f.close()
        print("El archivo 2 ha sido enviado correctamente.")

    if opcion == '3':     
        CHUNK_SIZE = 1024
        FILE = "bcryp3.txt.ctxt"

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('', 50007)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)        
        
        f= open(FILE, 'rb')
        data = f.read(CHUNK_SIZE)
        while data:
            sock.send(data)
            data = f.read(CHUNK_SIZE)
        
        # Cerrar conexión y archivo.
        sock.close()
        f.close()
        print("El archivo 3 ha sido enviado correctamente.")

    if opcion == '4':     
        CHUNK_SIZE = 1024
        FILE = "bcryp4.txt.ctxt"

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('', 50007)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)        
        
        f= open(FILE, 'rb')
        data = f.read(CHUNK_SIZE)
        while data:
            sock.send(data)
            data = f.read(CHUNK_SIZE)
        
        # Cerrar conexión y archivo.
        sock.close()
        f.close()
        print("El archivo 4 ha sido enviado correctamente.")

    if opcion == '5':     
        CHUNK_SIZE = 1024
        FILE = "bcryp5.txt.ctxt"

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('', 50007)
        print('connecting to {} port {}'.format(*server_address))
        sock.connect(server_address)        
        
        f= open(FILE, 'rb')
        data = f.read(CHUNK_SIZE)
        while data:
            sock.send(data)
            data = f.read(CHUNK_SIZE)
        
        # Cerrar conexión y archivo.
        sock.close()
        f.close()
        print("El archivo 5 ha sido enviado correctamente.")
        
            
    elif opcion == '0':
        break



