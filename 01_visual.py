from mc_core import *
import sys

print("Genera llave privada...")
tPriv = privateKeyH84()
print(tPriv)
print("Genera llave publica...")
tPub = publicKeyH84(tPriv.makeGPrime())
print(tPub)
print("Encrypting...")
tPub.encryptFile("bcryp5.txt")
print("Decrypting...")
tPriv.decryptFile("bcryp5.txt.ctxt")