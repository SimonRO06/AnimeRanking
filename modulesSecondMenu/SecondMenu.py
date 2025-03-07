from modules.ScreenController import limpiar,pausar
from modules.Interfaces import FunctionsMenu
from modulesSecondMenu.RegistrarAnimes import registrar_animes

def second_menu(email):
    while True:
        limpiar()
        print(FunctionsMenu)
        try:
            seleccion = int(input('> '))
        except ValueError:
            print('Ingrese un valor numerico')
            pausar()
        else:
            if seleccion == 1:
                limpiar()
                registrar_animes(email)
            elif seleccion == 2:
                limpiar()
                pass
            elif seleccion == 3:
                limpiar()
                pass
            elif seleccion == 4:
                limpiar()
                pass
            elif seleccion == 5:
                break
            else:
                print('Ingrese una opcion valida')
                pausar()