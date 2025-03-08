from modules.ScreenController import limpiar,pausar
from modules.DiccionariosListas import cuentas,listaAnimes,animes

def registrar_animes(email):
    anime = input('Ingrese el nombre del anime: ').replace(' ','-').lower()
    try:
        calificacion = float(input('Ingrese la calificacion del anime (1.0 - 5.0): '))
    except ValueError:
        print('Solo se pueden ingresar valores numericos...')
        pausar()
    else:
        if calificacion < 1 or calificacion > 5:
            print('La calificacion debe ser entre 1.0 y 5.0')
            pausar()
        else:
            try:
                episodios = int(input('Ingrese la cantidad de episodios: '))
            except ValueError:
                print('Solo se pueden ingresar valores numericos...')
                pausar()
            else:
                comentario = input('Ingrese un comentario: ')
                if anime in listaAnimes:
                    cuentas[email][anime] = {'calificacion':calificacion,'episodios':episodios,'comentario':comentario}
                else:
                    listaAnimes.append(anime)
                    cuentas[email][anime] = {'calificacion':calificacion,'episodios':episodios,'comentario':comentario}
                    animes[anime] = {'calificacion': calificacion,'episodios':episodios}