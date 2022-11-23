import os, sys
from time import sleep
from .interfaz import Consola
from .mmu import MMU
from .PLP import LargoPlazo
from .PCP import CortoPlazo
from .PMP import MedioPlazo



class Simulador(object):
    def __init__(self, particiones, lista_procesos):
        self.__reloj = 0
        self.__consola = None
        self.__mmu = MMU(particiones)  # El MMU se encarga de inicializar la memoria
        self.__plp = LargoPlazo(lista_procesos)
        self.__pcp = CortoPlazo()
        self.__pmp = MedioPlazo(self.__mmu)
        self.__terminados = list()
    
    def reloj(self):
        return self.__reloj

    def mmu(self):
        return self.__mmu

    def plp(self):
        return self.__plp

    def pcp(self):
        return self.__pcp

    def pmp(self):
        return self.__pmp  
    
    def incrementar(self):
        self.__reloj += 1

    def liberarRecursos(self):
        proceso = self.__pcp.cpu().procAsignado()
        proceso.setestado('T')
        self.__pcp.liberar()
        self.__mmu.liberar(proceso)
        self.__plp.terminarProceso(proceso)
        self.__pmp.ejecutar(self.admitidos())
        self.__terminados.append(proceso)

    def nuevos(self, cant=None):
        if cant is None:
            return self.__plp.nuevos()
        else:
            return self.__plp.nuevos()[0:3]


    def admitidos(self):
        return self.__plp.admitidos()

    def terminados(self):
        return self.__terminados
    
    def consola(self):
        return self.__consola

    def mostrar(self, titulo, lista_procesos):
        # Muestra una tabla con título personalizado
        # encabezados PID, TA, TI, TAM, EST
        # en mismo orden los atributos de cada proceso
        print(' ' + '-'*42)
        print(f'\n{titulo}')
        print(' ' + '-'*42)
        print(f' PID\tTA\tTI\tTAM\tEST')
        for proceso in lista_procesos:    
            print(f' {proceso.id()}\t{proceso.ta()}\t{proceso.ti()}\t{proceso.tam()}\t{proceso.estado()}')       


    def admitir(self):
        # Engloba la admisión de procesos pendientes en el PLP
        # y actualiza cola de listos en el PCP
        self.plp().admitir(self.mmu(), self.reloj())
        self.pmp().ejecutar(self.admitidos())
        self.pcp().setProcListos(self.plp().getListos())
        

    def iniciarConsola(self):
        titulo = 'SIMULADOR'
        self.__consola = Consola(titulo)
        self.__consola.formatTerm(44,40)

    def nofin(self):
        return self.nuevos() or self.admitidos()
        
    def iniciar(self):
        # Inicia el simulador
        self.iniciarConsola()
        self.mainloop()
        print('\n\nFIN DE LA SIMULACIÓN\n')

    def mainloop(self):
        # Ejecuta el bucle del programa principal
        bandera = True
        x = self.consola()
        #fin = self.__plp.tiTotal()+1  #  Bandera de fin de ejecución
        while self.nofin():
            x.limpiar()
            
            self.admitir()

            if bandera and self.plp().getListos():
                #self.pmp().ejecutar(self.admitidos())
                self.pcp().dispatcher()
                bandera = False
                
            


            if self.__pcp.cpu().reloj() == 0:
                self.liberarRecursos()
                self.admitir()
                self.pcp().dispatcher()

            if not self.plp().getListos():
                bandera = True
                #self.pmp().ejecutar(self.admitidos())
                
            self.pcp().ejectuar()

            print(' ' + '-'*42)
            print(f' Reloj = {self.reloj()}\t', end='')
            if not self.pcp().cpu().procAsignado() is None:
                print(f'\tEjecutando: PID={self.pcp().cpu().procAsignado().id()}')
            else:
                print(f'\tEjecutando: PID=[]')
            print(' ' + '-'*42 + '\n')

            # Muestra la distribución de particiones
            # procesos asignados y fragmentación
            self.mmu().distribucion()

            # Se muestra en pantalla los estados
            self.mostrar(' Monitor de procesos', self.admitidos())
            self.mostrar(' Procesos pendientes (3 primeros en cola)', self.nuevos(10))
            self.mostrar(' Procesos terminados', self.terminados())
            
            
            self.incrementar()   # Incrementa el reloj
            x.esperar()