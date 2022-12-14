
Simulador de asignacion de memoria y planificacion de procesos
Version: 2.0
---------------------------------------------------------------------------------

INFORMACION:

Este programa simula la asignacion de memoria por criterio worst-fit
y planificacion de procesos mediante el algoritmo SJF que prioriza el menor 
tiempo de irrupcion.
---------------------------------------------------------------------------------

ESTRUCTURA:

En la carpeta 'config' se encuentra el archivo 'datos.txt' donde se puede precargar
datos para posterior simulacion de procesos.

La carpera 'src' contiene los diferentes modulos para la interfaz, simulacion, 
gestion de archivo, etc.
---------------------------------------------------------------------------------

FORMATO ARCHIVO:

El archivo 'datos.txt' debe cumplir la siguientes caracteristicas...

- Cada linea representa un proceso.
- Maximo de lineas permitidas: 10
- En cada linea se indica: [ta,ti,tam]
donde:
    ta = tiempo de arribo
    ti = tiempo de irrupcion
    tam = tamaño del proceso
todos valores tipo entero.
- El programa realiza una validacion en caso que existan datos incoherentes
---------------------------------------------------------------------------------

MODO DE EJECUCION:

1) Ejecutar el archivo 'simu.exe'
2) El programa inicia una interfaz interactiva para el usuario con un menu principal.
3) Cargar datos de procesos que participan de la simulacion (manualmente o desde archivo).
4) Iniciar la simulacion.
5) Presione ENTER para avanzar el reloj de ejecucion.
6) El simulador se ejecutara hasta que todos los procesos terminen con 'estado = terminado'
---------------------------------------------------------------------------------

ABORTAR:

Si desea frenar la ejecucion de forma forzada:
1. Presione la combinacion de teclas 'Ctrl + C'
2. Cierre la ventana de su terminal
