from modules.ScreenController import limpiar,pausar
from modules.DiccionariosListas import cuentas

def registrar_animes(email):
    listaAnimes = []
    for i in range(5):
        if i > 4:
            break
        else:
            anime = input('Ingrese un anime: ').lower().replace(" ", "-")
            if anime in listaAnimes:
                print('El anime ya se encuentra en la lista...')
                pausar()
            else:
                try:
                    episodios = int(input('Ingrese la cantidad de episodios: '))
                except ValueError:
                    print('La cantidad de episodios debe ser numerica...')
                else:
                    try:
                        valoracion = float(input('Ingrese la valoracion del anime: '))
                    except ValueError:
                        print('La valoracion debe ser numerica...')
                    else:
                        comentario = input('Escriba su opinion acerca del anime: ')
                        anime = {
                            'episodios': episodios,
                            'valoracion': valoracion,
                            'comentario': comentario
                        }
                        cuentas.update(email[anime])
                        
                        


