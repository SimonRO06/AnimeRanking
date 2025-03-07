from modules.DiccionariosListas import listaEmails,cuentas
from modules.ScreenController import limpiar,pausar

def registrarse():
    email = input('Ingrese un email: ')
    if email in listaEmails:
        print('El email ya se encuentra en uso...')
        pausar()
    elif not email.endswith('@gmail.com'):
        print('No es un email valido')
        pausar()
    else:
        contraseña = input('Ingrese una contraseña: ')
        confirmar = input('Ingrese la contraseña de nuevo para confirmar: ')
        if contraseña == confirmar:
            nombre = input('Ingrese su nombre: ')
            listaEmails.append(email)
            cuentas[email] = {
                'contraseña': contraseña,
                'nombre': nombre
            }
        else:
            print('La contraseña no es la misma...')
            pausar()