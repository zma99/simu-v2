import sys
from time import sleep
from .terminal import Consola
from .gestorArchivos import formatInt

x = Consola()



def salir():
    # Simula que se está liberando la consola
    x.setTitulo('')
    print('\nSaliendo...')
    for i in range(0,3):
        sleep(0.3)
        print('.')
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
    try:
        int(dato)
        return True
    except ValueError:
        print('\nIntente de nuevo. Debe ingresar un número entero.')
        return False

def pedir(nom_dato):
    while True:
        dato = input(f'{nom_dato}= ')
        if esEntero(dato):
            break
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
        print('\nIngrese datos del proceso.\n')
        print('Procesos cargados [TA,TI,TAM]: ', lista_procesos)
        print('-'*40)
        print(f'\nProceso Nro:{num}')
        ta = pedir('TA')
        ti = pedir('TI')
        tam = pedir('TAM(KB)')
        proceso = [ta,ti,tam]
        lista_procesos.append(proceso)
        print('-'*40)
        seguir = input('\n¿Seguir? [ENTER=Sí / Cualquiera=No]\n> ')
        if seguir != '':
            break

    x.limpiar()
    mostrar('Procesos cargados', lista_procesos)
    x.esperar()

    lista_procesos = formatear(lista_procesos)

    return lista_procesos


