from .memoria import *

class MMU(object):
    def __init__(self, datos_part):
        self.__memoria = Memoria(datos_part)

    def __str__(self):
        return str(self.__memoria)
    
    def __repr__(self):
        return self.__memoria

    def memoria(self):
        return self.__memoria

    def particiones(self):
        return self.__memoria.particiones()

    def distribucion(self):
        # Muestra en pantalla la distribución de particiones
        # en memoria y sus propiedades
        titulo = 'Distribución de particiones'
        print(titulo)
        print('-'*len(titulo)+'-'*10)
        print('ID\tDir\tTam\tPID\tFrag')
        for part in self.particiones():
            if part.procAsignado() is None:
                procAsignado = None
            else:
                procAsignado = part.procAsignado().id()

            print(f'{part.id()}\t{part.dirInicio()}\t{part.tam()}\t{procAsignado}\t{part.fragmentacion()}')
        print('-'*len(titulo)+'-'*10)

    def ubicar(self, proceso):
        self.memoria().partLibreMayor().asignar(proceso)

        
    def asignar(self, lista_procesos):
        # Controla la asignación de procesos a memoria
        for proceso in lista_procesos:
            if proceso.estado() != 'L' and proceso.estado() != 'E':
                if self.__memoria.memoriaLibre() and self.__memoria.worstfit(proceso):
                    proceso.setestado('L')  # Listo
                else:
                    proceso.setestado('L/S')    # Listo/Suspendido

    def liberar(self, proceso):
        # Invoca método para liberar proceso de memoria
        self.__memoria.liberar(proceso)