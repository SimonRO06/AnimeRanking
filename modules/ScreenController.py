import os
import sys

def limpiar():
    if sys.platform == 'linux' or sys.platform == 'darwin':
        os.system('clear')
    else:
        os.system('cls')

def pausar():
    if sys.platform == 'linux' or sys.platform == 'darwin':
        x = input('Presione enter para continuar...')
    else:
        os.system('pause')