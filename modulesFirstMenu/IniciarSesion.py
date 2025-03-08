from modules.DiccionariosListas import listaEmails,cuentas
from modulesSecondMenu.SecondMenu import second_menu
from modules.ScreenController import limpiar,pausar

def iniciar_sesion():
    email = input('Ingrese el email: ')
    if email in listaEmails:
        contraseña = input('Ingrese la contraseña: ')
        if contraseña == cuentas.get(email).get('contraseña'):
            second_menu(email)
        else:
            print('La contraseña no es la misma...')
            pausar()
    else:
        print('El email no existe...')
        pausar()