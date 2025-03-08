from modules.DiccionariosListas import cuentas

def rank_personal(email):
    print('Tus animes registrados son:')
    for anime, datosdelanime in cuentas[email].items():
        if anime != 'contraseña' and anime != 'nombre':
            print(f'\nAnime: {anime}')
            print(f'  Calificación: {datosdelanime["calificacion"]}/5')
            print(f'  Episodios: {datosdelanime["episodios"]}')
            print(f'  Comentario: {datosdelanime["comentario"]}')
            print('-' * 40)