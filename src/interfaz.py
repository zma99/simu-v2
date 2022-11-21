from .terminal import Consola
from .gestorArchivos import formatear


def imprimir(cadena, ancho):
    print('|' + cadena.center(ancho,' '), end='|\n')

def panel(lineas, ancho):
    for cadena in lineas:
        if type(cadena) == list:
            for x in cadena:
                imprimir(x, ancho)
        else:
           imprimir(cadena, ancho)

def info():
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

def validar(dato):
    try:
        int(dato)
        return True
    except ValueError:
        print('\nIntente de nuevo. Debe ingresar un número entero.')
        return False

def pedir(nom_dato):
    x = Consola()
    while True:
        dato = input(f'{nom_dato}= ')
        if validar(dato):
            break
        x.esperar('')
        

    return dato

def cargaManual():
    x = Consola('Carga manual')
    num = 0
    lista_procesos = list()
    while True:
        x.limpiar()
        num += 1
        print('\nIngrese datos del proceso.\n')
        print('Procesos cargados: ', lista_procesos)
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


