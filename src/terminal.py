from sys import platform
from os import system

class Consola(object):
    def __init__(self, titulo=''):
        # titulo sólo funciona para windows
        if platform == 'win32':
            if titulo != '':
                system(f'TITLE {titulo}')
        else:
            pass

    def setTitulo(self, titulo):
        if platform == 'win32':
            system(f'TITLE {titulo}')
        else:
            pass

    def limpiar(self):
        # Limpia la terminal
        if platform == 'win32':
            system('cls')
        elif platform == 'linux':
            system('tput reset')
        else:
            pass

    def esperar(self, mensaje='\n Presione una tecla para continuar...'):
        # A modo general utiliza la función input()
        # para simular la detención de la terminal
        input(mensaje)

    def formatTerm(self, columnas=100, lineas=25):
        # Cambia el tamaño de la ventana de la terminal en uso
        # según plataforma
        if platform == 'win32':
            system(f'MODE con:cols={columnas} lines={lineas}')
        elif platform == 'linux':
            system(f'printf "\033[8;{lineas};{columnas}t"')
        else:
            pass