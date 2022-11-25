import os
from .terminal import Consola
from time import sleep
from os.path import exists


# Controla el límite de procesos para cargar
LIMITE_PROC = 10

# Instancia global de la terminal
x = Consola()

def formatLista(lista_str):
    # Recibe una lista de strings y devuelve lista de listas
    resultado = list()
    for cadena in lista_str:
        # Quita corchetes de la cadena
        temp = cadena.replace('[','').replace(']','')
        # Convierte la cadena en lista y agrega a otra lista
        resultado.append(temp.split(','))

    return resultado

def formatInt(lista_lista):
    # Recibe una lista de listas a cuyos elementos convierte en enteros
    # luego devuelve una lista de listas con elementos de tipo int()
    resultado = list()
    for lista in lista_lista:
        aux = list()
        for elem in lista:
            try:
                #if lista.index(elem) == 0 and int(elem) >= 0:
                aux.append(abs(int(elem)))
                #elif int(elem) >= 1:
                #    aux.append(int(elem))
                #print(aux)
            except ValueError:
                print(f'\nERROR: No se pudo formatear los datos del archivo a valores int(). Revise el arhivo y corrija los errores.')
                print(f'\nLínea con error: {lista} - Dato no válido: [ {elem} ] (debe ser número entero)\n')
                x.esperar()
                return 0
        resultado.append(aux)

    return resultado

def validar(lista):
    # Limpia blancos y datos con formato no válido
    print('\nValidando contenido...')
    print('Limpiando líneas vacías...')
    sleep(0.5)
    while lista.count('') > 0:
        lista.remove('')

    aux = lista[:]
    print('Limpiando líneas incoherentes...')
    sleep(0.5)
    for elem in aux:
        temp = elem.replace('[','').replace(']','').split(',')[:]
        if len(temp) != 3:
            lista.remove(elem)
    return lista


def formatear(lista_str):
    # Recibe lista de string listas de string: 
    # ['['ta', 'ti', 'tam'], ['ta', 'ti', 'tam'],..., ['ta', 'ti', 'tam']']
    # da formato y devuelve lista de listas de enteros:
    # [[ta, ti, tam], [ta, ti, tam],..., [ta, ti, tam]]
    # donde ta, ti y tam son tipo int()

    lista_str = validar(lista_str)
    print('Dando formato...')
    sleep(0.5)
    resultado = formatLista(lista_str)
    resultado = formatInt(resultado)
    return resultado

def valido(lista):
    # Controla tamaño del proceso
    errores = 0
    for elem in lista:
        if elem[2] > 250:
            errores += 1

    if errores > 0:
        error = f'\nERROR: Hay {errores} procesos en el archivo que tienen un tamaño que excede la capacidad del simulador.'
        print('\n'+'#'*len(error))
        print(error)
        print('\n'+'#'*len(error))
        x.esperar()
        return False

    return True

def cargar(ruta_archivo, modo=0):
    # Permite cargar un archivo .txt
    # modo=0 para archivo de proceos
    # modo=1 para archivo readme
    x.limpiar()
    if exists(ruta_archivo):
        print('\nLeyendo archivo...')
        with open(ruta_archivo, 'r') as archivo:
            if modo == 0:
                with open(ruta_archivo, 'r') as archivo:
                    contenido = archivo.read().split('\n')
                    print('\nContenido del archivo:\n')
                    print(contenido)
                    contenido = formatear(contenido)
                    print('\nContenido validado:\n')
                    print(contenido)
                    if contenido != 0 and valido(contenido):
                        sleep(0.5)
                        if len(contenido) > LIMITE_PROC:
                            x.limpiar()
                            print(f'\nSólo se permite cargar un máximo de {LIMITE_PROC} procesos.')
                            x.esperar()
                            return []
                        else:
                            print('\nListo!')
                            input('\nPresione una tecla para continuar...')
                            return contenido
            elif modo == 1:
                x.limpiar()
                contenido = archivo.readline()
                while contenido != '':
                    print(contenido)
                    if contenido.count('-') > 2:
                        x.esperar('')
                        x.limpiar()
                    contenido = archivo.readline()
            else:
                pass
    else:
        print('NO SE ENCUENTRA EL ARHCIVO ESPECIFICADO')
        x.esperar()



def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)

