from sys import platform
from os import system

class Consola(object):
    def __init__(self, titulo='', nueva_ventan=False):
        if platform == 'win32':
            if titulo != '':
                system(f'TITLE {titulo}')
            if nueva_ventan:
                system('START')
            
        elif platform == 'linux':
            pass
        else:
            pass

    def setTitulo(self, titulo):
        system(f'TITLE {titulo}')

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
            system('printf "\033[8;10;42t"')
        else:
            pass