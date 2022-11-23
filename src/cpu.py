class CPU(object):
    def __init__(self):
        self.__procAsignado = None
        self.__reloj = None

    def procAsignado(self):
        return self.__procAsignado

    def reloj(self):
        return self.__reloj

    def asignar(self, proceso):
        if self.procAsignado() is None:
            self.__procAsignado = proceso
            self.__procAsignado.setestado('E')
            self.__reloj = proceso.ti()

    def ejecutar(self):
        if not self.reloj() is None:
            self.__reloj -= 1

    def liberar(self):
        self.__procAsignado = None
        self.__reloj = None
