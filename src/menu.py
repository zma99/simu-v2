from .interfaz import Consola

class Menu(object):
    def __init__(self, diccionario):
        self.__opciones = diccionario
        self.__eleccion = None
        self.__consola = Consola()

    def eleccion(self):
        return self.__eleccion

    def mostrar(self):
        # imprime en pantalla las opciones de menú
        # que se encuentren en el attr: opciones
        print('\nMenú\n')
        for item in self.__opciones:
            print(f'{item}) {self.__opciones[item]}')

    def capturar(self):  
        # Captura entrada por teclado del usuario
        self.__eleccion = input('\n> ')
        if not self.valido():
            self.__consola.esperar('\nIngrese una opción válida...')
        
    def valido(self):
        # Valida que un dato está entre las
        # opciones que dispone el menú
        try:
            self.__eleccion = int(self.__eleccion)
            if str(self.__eleccion) in self.__opciones:
                return True
            return False
        except ValueError:
            return False