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
            return self.__plp.nuevos()


    def admitidos(self):
        return self.__plp.admitidos()

    def terminados(self):
        return self.__terminados
    
    def consola(self):
        return self.__consola

    def mostrar(self):
        # Muestra información para el usuario


        # Se muestra encabezados: Reloj y Proceso en ejecición
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

        # Se muestra en pantalla los estados de colas
        self.mostrarCola(' Cola de admitidos', self.admitidos())
        self.mostrarCola(' Cola de nuevos', self.nuevos(10))
        self.mostrarCola(' Procesos terminados', self.terminados())

        
    def mostrarCola(self, titulo, lista_procesos):
        # Muestra una tabla con título personalizado
        # encabezados PID, TA, TI, TAM, EST
        # en mismo orden los atributos de cada proceso
        print(' ' + '-'*42)
        print(f'\n{titulo}')
        print(' ' + '-'*42)
        print(f' PID\tTA\tTI\tTAM(KB)\tEST')
        for proceso in lista_procesos:    
            print(f' {proceso.id()}\t{proceso.ta()}\t{proceso.ti()}\t{proceso.tam()}\t{proceso.estado()}')       


    def admitir(self):
        # Engloba la admisión de procesos pendientes en el PLP
        # y actualiza cola de listos en el PCP
        self.plp().admitir(self.mmu(), self.reloj())
        self.pmp().ejecutar(self.admitidos())
        self.pcp().setProcListos(self.plp().getListos())
        

    def iniciarConsola(self):
        # Instancia un objeto para controlar la terminal
        titulo = 'SIMULADOR'
        self.__consola = Consola(titulo)
        self.__consola.formatTerm(44,45)

    def nofin(self):
        # Valida condición de fin para mainloop
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
        while self.nofin():
            x.limpiar()
            self.admitir()

            # Para primer vuelta y cuando arriban tarde los procesos
            if bandera and self.plp().getListos():
                self.pcp().dispatcher()
                bandera = False

            # Termina ejecición de un proceso
            if self.pcp().cpu().reloj() == 0:
                self.liberarRecursos()
                self.admitir()
                self.pcp().dispatcher()

            # Si cola de listos no está vacía setea en True
            # sirve para el primer if
            if not self.plp().getListos():
                bandera = True
            
            # Ejecución
            self.pcp().ejectuar()  
            self.mostrar()
            self.incrementar()   # Incrementa el reloj
            x.esperar()