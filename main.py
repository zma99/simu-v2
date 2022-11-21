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
    '4':'Acerca del simulador',
    '5':'Salir'
}

RUTA_ARCHIVO = 'config\datos.txt'
PARTICIONES = [80,250,120,60]
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
        print('-'*len(TITULO))
        print(TITULO)
        print('-'*len(TITULO))
        while True:
            menu.mostrar()
            menu.capturar()
            break
        if menu.eleccion() == 1:
            if cola_nuevos:
                simu = Simulador(PARTICIONES, cola_nuevos)
                simu.iniciar()
                print('\n\nFIN DE LA SIMULACIÓN\n')
            else:
                print('\nPrimero debe cargar información de los procesos. Puede hacerlo desde un archivo o cargar manualmente.')
            
            x.esperar('\nPresione una tecla para volver al menú principal...')

        if menu.eleccion() == 2:
            cola_nuevos = cargar(RUTA_ARCHIVO)

        if menu.eleccion() == 3:
            cola_nuevos = cargaManual()

        if menu.eleccion() == 4:
            x.limpiar()
            info()
            x.esperar('\nPresione una tecla para volver al menú principal...')

        if menu.eleccion() == 5:
            break

    sys.exit('\nSaliendo...')