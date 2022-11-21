import os
from .interfaz import Consola

class Menu(object):
    def __init__(self, diccionario):
        self.__opciones = diccionario
        self.__eleccion = None
        self.__consola = Consola()

    def eleccion(self):
        return self.__eleccion

    def mostrar(self):
        print('\nMenú\n')
        for item in self.__opciones:
            print(f'{item}) {self.__opciones[item]}')

    def capturar(self):  
        self.__eleccion = input('\n> ')
        if not self.valido():
            self.__consola.esperar('\nIngrese una opción válida...')
        
    def valido(self):
        try:
            self.__eleccion = int(self.__eleccion)
            if str(self.__eleccion) in self.__opciones:
                return True
            return False
        except ValueError:
            return False