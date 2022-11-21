from .cpu import CPU

class CortoPlazo(object):
    def __init__(self):
        self.__cpu = CPU()
        self.__procListos = list()

    def cpu(self):
        return self.__cpu

    def procListos(self):
        return self.__procListos

    def setProcListos(self, lista_procesos):
        self.__procListos = lista_procesos

    def SJF(self):
        # Ordena cola de procesos listos
        # por menor tiempo de irrupción (ti)
        self.__procListos.sort(key=lambda x : x.ti())

    def dispatcher(self):
        # Asigna CPU al primer proceso en cola de listos
        if self.__procListos:
            self.SJF()
            self.__cpu.asignar(self.__procListos.pop(0))

    def ejectuar(self):
        self.__cpu.ejecutar()

    def liberar(self):
        self.__cpu.liberar()
