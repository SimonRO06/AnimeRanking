from modules.ScreenController import limpiar,pausar
from modules.Interfaces import FunctionsMenu
from modulesSecondMenu.RegistrarAnimes import registrar_animes
from modulesSecondMenu.RankingGeneral import rank_general
from modulesSecondMenu.RankingPersonal import rank_personal
from modules.DiccionariosListas import cuentas

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
                pausar()
            elif seleccion == 2:
                limpiar()
                rank_general()
                pausar()
            elif seleccion == 3:
                limpiar()
                rank_personal(email)
                pausar()
            elif seleccion == 4:
                limpiar()
                pass
                pausar()
            elif seleccion == 5:
                break
            else:
                print('Ingrese una opcion valida')
                pausar()