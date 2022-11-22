from .proceso import Proceso

class LargoPlazo(object):
    def __init__(self, lista_procesos):
        self.__multiprog = 5
        self.__nuevosProc = list()
        self.__admitidos = list()
        for datos in lista_procesos:
            self.__nuevosProc.append(self.crearProceso(datos))
        self.__nuevosProc.sort(key=lambda x : x.ta())
        
    def nuevos(self):
        return self.__nuevosProc

    def admitidos(self):
        return self.__admitidos
    
    def setAdmitidos(self, lista_procesos):
        self.__admitidos = lista_procesos

    def cantAdmitidos(self):
        return len(self.__admitidos)

    def ingresando(self):
        return len(self.__nuevosProc) > 0

    def crearProceso(self, datos):
        p = Proceso()
        p.setid(len(self.__nuevosProc) + 1)
        p.setta(datos[0])
        p.setti(datos[1])
        p.settam(datos[2])
        return p

    def tiTotal(self):
        # Calcula y retorna el TI total
        total = 0
        for p in self.__nuevosProc:
            total += p.ti()

        return total

    def admitir(self, mmu, reloj):
        # Control de multiprogramación
        # Verifica si hay nuevos procesos y controla la admisión
        ingresaron = False
        while self.ingresando() and self.cantAdmitidos() < self.__multiprog:
            ingresaron = True
            proceso = self.__nuevosProc[0]
            if proceso.ta() <= reloj:
                self.__admitidos.append(proceso)
                self.__nuevosProc.pop(0)
            else:
                break
        if ingresaron or not self.ingresando():
            mmu.asignar(self.__admitidos)

    def getListos(self):
        # Devuelve lista de porcesos con estado=L
        listos = list()
        for proceso in self.__admitidos:
            if proceso.estado() == 'L':
                listos.append(proceso)

        return listos


    def terminarProceso(self, proceso):
        # Remueve procesos con estado=T
        # de la cola de admitidos
        if self.cantAdmitidos() > 0:
            self.__admitidos.remove(proceso)