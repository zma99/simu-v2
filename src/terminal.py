from sys import platform
from os import system

class Consola(object):
    def __init__(self, titulo=''):
        if platform == 'win32':
            if titulo != '':
                system(f'TITLE {titulo}')
        #elif platform == 'linux':
        else:
            pass

    def setTitulo(self, titulo):
        if platform == 'win32':
            system(f'TITLE {titulo}')
        else:
            pass

    def limpiar(self):
        if platform == 'win32':
            system('cls')
        elif platform == 'linux':
            system('clear')
        else:
            pass

    def esperar(self, mensaje='\n Presione una tecla para continuar...'):
        input(mensaje)

    def formatTerm(self, columnas=False, lineas=False):
        # Cambia el tamaño de la ventana de la terminal en uso
        if platform == 'win32':
            if not (columnas or lineas):
                system('MODE con:cols=100 lines=25')
            elif columnas and lineas:
                system(f'MODE con:cols={columnas} lines={lineas}')
            elif columnas:
                system(f'MODE con:cols={columnas}')
            elif lineas:
                system(f'MODE con:lines={lineas}')
        elif platform == 'linux':
            if not (columnas or lineas):
                system(f'printf "\033[8;25;100t"')
            elif columnas and lineas:
                system(f'printf "\033[8;{lineas};{columnas}t"')
            elif columnas:
                system(f'printf "\033[8;25;{columnas}t"')
            elif lineas:
                system(f'printf "\033[8;{lineas};100t"')
        else:
            pass