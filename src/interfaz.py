import sys
from time import sleep
from .terminal import Consola
from .gestorArchivos import formatInt

# Controla el límite de procesos para cargar
LIMITE_PROC = 10

# Instancia global de la terminal
x = Consola()



def salir():
    # Simula que se está liberando la consola
    x.setTitulo('')
    print('\nSaliendo...')
    for i in range(0,3):
        sleep(0.3)
        print('.')
    x.limpiar()
    x.formatTerm()
    sys.exit()

def imprimir(cadena, ancho):
    # Imprime una con texto centrado
    print('|' + cadena.center(ancho,' '), end='|\n')

def panel(lineas, ancho):
    # Imprime un cuadro con informacion centrada
    for cadena in lineas:
        if type(cadena) == list:
            for x in cadena:
                imprimir(x, ancho)
        else:
           imprimir(cadena, ancho)

def acercaDe():
    # Muestra un cuadro con información
    fecha = 'Noviembre 2022'
    uni = 'UNIVERSIDAD TECNOLÓGICA NACIONAL'
    regional = 'Facultad Regional Resistencia'
    carrera = 'Ingeniería en Sistemas de Información'
    asignatura = 'Sistemas Operativos'
    proyecto = 'Simulador de asignación de memoria y planificación de procesos'
    version = 'V2'
    grupo = 'Grupo 2 - TT'
    integrantes = [
        'MASS, Matias',
        'ROMERO, Sebastián',
        'SCHEFER, Mauricio',
        'ZANAZZO, Alan'
    ]
    ancho = len(proyecto)+4

    blanco = ' '
    separacion = '-'*ancho

    lineas = [
        fecha,
        separacion,
        uni, 
        regional, 
        carrera,
        asignatura, 
        separacion,
        blanco,
        proyecto,
        version,
        separacion,
        grupo,
        blanco,
        integrantes
    ]
    
    print('\n+', end='')
    print('-'*ancho, end='+\n')
    panel(lineas, ancho)
    print('+', end='')
    print('-'*ancho, end='+\n')



def mostrar(titulo, lista_procesos):
        # Muestra una tabla con título personalizado
        # encabezados #, TA, TI, TAM(KB)
        # en mismo orden los atributos de cada proceso
        print('-'*40)
        print(f'\n{titulo}')
        print('-'*40)
        print(f'#\tTA\tTI\tTAM(KB)')
        num = 0
        for proceso in lista_procesos:
            num += 1    
            print(f'{num}\t{proceso[0]}\t{proceso[1]}\t{proceso[2]}')

def esEntero(dato):
    # Valida que un dato sea tipo int()
    try:
        int(dato)
        return True
    except ValueError:
        print('\nIntente de nuevo. Debe ingresar un número entero.')
        return False

def pedir(nom_dato):
    # Pide por pantalla ingresar un dato
    # nom_dato es tipo str() se muestra por pantalla
    
    while True:
        dato = input(f'{nom_dato}= ')
        if esEntero(dato):
            dato = int(dato)
            if nom_dato == 'TA' and dato < 0:
                print('TA debe ser mayor o igual a cero')
            elif nom_dato == 'TI' and dato < 1:
                print('TI debe ser mayor o igual a uno')
            elif nom_dato == 'TAM(KB)' and (dato < 1 or dato > 250):
                print('El tamaño mínimo es 1 KB y el máximo es 250 KB')
            else:
                break
        if dato == 'CANCELAR' or dato == 'C':
            return -1
        x.esperar('')
        
    return dato


def formatear(lista):
    # Toma una lista de listas con formato [TA,TI,TAM]
    # cada valor se convierte de str a int
    return formatInt(lista)


def cargaManual():
    # Permite la carga de datos manualmente 
    # incluye validacion de datos tipo int()
    x.setTitulo('Carga manual')
    num = 0
    lista_procesos = list()
    while True:
        x.limpiar()
        num += 1
        print(f'\nIngrese datos del proceso (máximo {LIMITE_PROC}). | "CANCELAR" o "C" (mayúsculas sin comillas) para abortar.\n')
        print('Procesos cargados [TA,TI,TAM]: ', lista_procesos)
        print('-'*40)
        print(f'\nProceso Nro:{num}')
        ta = pedir('TA')
        if ta == -1:
            break
        ti = pedir('TI')
        if ti == -1:
            break
        tam = pedir('TAM(KB)')
        if tam == -1:
            break
        proceso = [ta,ti,tam]
        lista_procesos.append(proceso)
        print('-'*40)
        if len(lista_procesos) == LIMITE_PROC:
            break
        seguir = input('\n¿Seguir? [ENTER=Sí / Otra tecla=No]\n> ')
        if seguir != '':
            x.limpiar()
            mostrar('Procesos cargados', lista_procesos)
            x.esperar()
            lista_procesos = formatear(lista_procesos)
            return lista_procesos
            break

    
    return []
    


