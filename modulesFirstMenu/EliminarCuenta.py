from modules.DiccionariosListas import listaEmails,cuentas
from modules.ScreenController import limpiar,pausar

def eliminar_cuenta():
    email = input('Ingrese el email que desea eliminar: ')
    if email in listaEmails:
        seguro = input('Confirme eliminar (S/N): ').upper()
        if seguro == 'N':
            print('El email no se ha eliminado...')
            pausar()
        if seguro == 'S':
            contraseña = input('Ingrese la contraseña: ')
            if contraseña == cuentas.get(email).get('contraseña'):
                listaEmails.remove(email)
                cuentas.pop(email)
                print(f'La cuenta {email} ha sido eliminada...')
                pausar()
            else:
                print('La contraseña es incorrecta...')
                pausar()
        else:
            print('No es una opcion valida...')
            pausar()
    else:
        print('El email no esta registrado...')
        pausar()
