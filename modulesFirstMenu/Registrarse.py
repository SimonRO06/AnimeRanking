from modules.DiccionariosListas import listaEmails,cuentas
from modules.ScreenController import limpiar,pausar

def registrarse():
    email = input('Ingrese un email: ')
    if email in listaEmails:
        print('El email ya se encuentra en uso...')
        pausar()
    else:
        listaEmails.append(email)
        contraseña = input('Ingrese una contraseña: ')
        confirmar = input('Ingrese la contraseña de nuevo para confirmar: ')
        if contraseña == confirmar:
            nombre = input('Ingrese su nombre: ')
            cuentas.update[email] = {
                'contraseña': contraseña,
                'nombre': nombre
            }
        else:
            print('La contraseña no es la misma...')
            pausar()