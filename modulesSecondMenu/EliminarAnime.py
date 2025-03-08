from modules.DiccionariosListas import cuentas, listaAnimes, animes
from modules.ScreenController import pausar

def eliminar_anime(email):
    buscar = input("Escribe el anime que deseas eliminar: ")
    if buscar in cuentas[email]:
        confirmacion = input("¿Estás seguro? (S/N): ").strip().lower()
        if confirmacion == 's':
            del cuentas[email][buscar]
            animechao = any(buscar in cuentas[usr] for usr in cuentas if usr != 'contraseña' and usr != 'nombre')
            
            if not animechao:
                listaAnimes.remove(buscar)
                del animes[buscar]   
            print("El anime ha sido eliminado de tu ranking personal.")
        else:
            print("cancelando...")
    else:
        print("El anime no está en tu ranking personal.")