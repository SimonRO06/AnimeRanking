from modules.Interfaces import MainMenu
from modules.ScreenController import limpiar,pausar
from modules.DiccionariosListas import listaEmails, cuentas
from modulesFirstMenu.Registrarse import registrarse
from modulesFirstMenu.EliminarCuenta import eliminar_cuenta
from modulesFirstMenu.IniciarSesion import iniciar_sesion

def main_menu():
    while True:
        limpiar()
        print(MainMenu)
        try:
            seleccion = int(input('> '))
        except ValueError:
            print('No es una opcion valida, porfavor escoja una de las opciones...')
        else:
            if seleccion == 1:
                limpiar()
                registrarse()
            if seleccion == 2:
                limpiar()
                iniciar_sesion()
            if seleccion == 3:
                limpiar()
                eliminar_cuenta()
            if seleccion == 4:
                limpiar()
                print('Programa cerrado...')
                break
            else:
                print('Esta no es una opcion valida...')

