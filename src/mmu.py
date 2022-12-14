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
        titulo = ' Distribución de particiones'
        print(titulo)
        print(' ' + '-'*len(titulo)+'-'*14)
        print(' ID\tDir\tTam(KB)\tPID\tFrag')
        for part in self.particiones():
            if part.procAsignado() is None:
                procAsignado = '-'
            else:
                procAsignado = part.procAsignado().id()

            print(f' {part.id()}\t{part.dirInicio()}\t{part.tam()}\t{procAsignado}\t{part.fragmentacion()}')

    def ubicar(self, proceso):
        # Ubica un proceso en la partición libre
        # de mayor tamaño sin otras consideración
        self.memoria().partLibreMayor().asignar(proceso)

        
    def asignar(self, lista_procesos):
        # Controla la asignación de procesos a memoria
        # por criterio worst-fit
        for proceso in lista_procesos:
            if proceso.estado() != 'L' and proceso.estado() != 'E':
                if self.__memoria.memoriaLibre() and self.__memoria.worstfit(proceso):
                    proceso.setestado('L')  # Listo
                else:
                    proceso.setestado('L/S')    # Listo/Suspendido

    def liberar(self, proceso):
        # Invoca método para liberar proceso de memoria
        self.__memoria.liberar(proceso)

    def cabe(self, p, q=None):
        # Verifica que el proceso p quepa en la
        # partición donde está asignado el proceso q
        if q is None:
            particion = self.memoria().partLibreMayor()
        elif q.partId() is None:
            particion = self.memoria().partLibreMayor()
        else:
            particion = self.memoria().particionId(q.partId())
        
        if not particion is None:
            return p.tam() <= particion.tam()
        else:
            return False