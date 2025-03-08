from modules.DiccionariosListas import cuentas, listaAnimes, animes, listaEmails, animesRank
from modules.ScreenController import limpiar, pausar

def rank_general():
    while True:
        limpiar()
        nombre = input("Ingresa el nombre del anime: ")
        
        if nombre in listaAnimes or cuentas or animes:
            try:
                calificacion = float(input('Ingrese la calificacion del anime (1.0 - 5.0): '))
            except ValueError:
                print('Solo se pueden ingresar valores numericos...')
                pausar()
                continue

            if calificacion < 1 or calificacion > 5:
                print('La calificacion debe ser entre 1.0 y 5.0')
                pausar()
                continue

            episodios = input("Ingresa el número de episodios: ")

            for anime in animesRank:
                if anime['nombre'] == nombre:
                    anime['calificacion'] = (anime['calificacion'] * anime.get('num_calificaciones', 1) + calificacion) / (anime.get('num_calificaciones', 1) + 1)
                    anime['num_calificaciones'] = anime.get('num_calificaciones', 1) + 1
                    break
            else:
                animesRank.append({
                    'nombre': nombre,
                    'calificacion': calificacion,
                    'episodios': episodios,
                    'num_calificaciones': 1 
                })

            animesRank.sort(key=lambda x: x['calificacion'])

            print("\n--- Ranking General de Animes ---")
            for index, anime in enumerate(animesRank):
                print(f"Ranking: {index + 1}, Nombre: {anime['nombre']}, Calificación: {anime['calificacion']:.2f}, Episodios: {anime['episodios']}")

            print(f"Total de animes en el ranking: {len(animesRank)}")
            pausar()

            continuar = input("¿Deseas agregar otro anime? (s/n): ")
            if continuar.lower() != 's':
                break

        else:
            print("El anime no existe en la lista...")
            return