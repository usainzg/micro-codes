from random import choice
import sys
import os
from string import ascii_letters , digits

pl = sys.platform
if pl == "linux" or pl  == "linux2" or pl == "darwin":
    os.system('clear')
elif pl == "win32":
    os.system('cls')

print ("""
1-python3 generador_JAZZTEL_XX.py
""")
nombre = str(input("Escribe la extencion que deseas para el diccionario , 'lts' o 'txt':"))
numero = int(input("Longitud de contraseña: "))
caracteres = ascii_letters + digits
mayus = caracteres.upper()
def generator(subir):
    file = open("diccionario."+nombre,'w')
    for i in range(1000):
        final = ''.join([choice (subir) for i in range(numero)])
        file.writelines(final)
        file.write("\n")
        print (final)
    file.close()
generator(mayus)
