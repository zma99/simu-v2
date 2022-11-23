import os, sys
from src.gestorArchivos import *
from src.menu import Menu
from src.interfaz import Consola, cargaManual, info
from src.simulador import Simulador

# CONFIGURACION

OPCIONES_MENU ={
    '1':'Iniciar simulación',
    '2':'Cargar procesos desde archivo',
    '3':'Cargar procesos manualmente',
    '4':'Información',
    '5':'Acerca del simulador',
    '6':'Salir'
}

ARCH_PROC = 'config\datos.txt'
ARCH_INSTUC = 'README.txt'
PARTICIONES = [100,250,120,60]
TITULO='SIMULADOR DE ASIGNACION DE MEMORIA Y PLANIFICACION DE PROCESOS'

# PROGRAMA
if __name__ == '__main__':
    x = Consola('Menu')
    x.limpiar()
    reloj = 0   # Reloj de ejecución
    cola_nuevos = list()    # Procesos nuevos en espera de ser admitidos
    menu = Menu(OPCIONES_MENU)
    while True:
        x.limpiar()
        x.setTitulo('Menu')
        x.formatTerm(len(TITULO)+2, 20)
        print('-'*len(TITULO))
        print(TITULO)
        print('-'*len(TITULO))
        while True:
            menu.mostrar()
            menu.capturar()
            break
        
        x.limpiar()
        if menu.eleccion() == 1:
            if cola_nuevos:
                simu = Simulador(PARTICIONES, cola_nuevos)
                simu.iniciar()
            else:
                print('\nPrimero debe cargar información de los procesos. Puede hacerlo desde un archivo o cargar manualmente.')
            
            x.esperar('\nPresione una tecla para volver al menú...')

        if menu.eleccion() == 2:
            x.formatTerm(140,30)
            cola_nuevos = cargar(ARCH_PROC)
        
        if menu.eleccion() == 3:
            x.formatTerm(140,30)
            cola_nuevos = cargaManual()
            
        if menu.eleccion() == 4:
            x.formatTerm(100,40)
            cargar(ARCH_INSTUC, 1)
            x.esperar()

        if menu.eleccion() == 5:
            x.formatTerm(80,30)
            info()
            x.esperar('\nPresione una tecla para volver al menú principal...')

        if menu.eleccion() == 6:
            break

    sys.exit('\nSaliendo...')