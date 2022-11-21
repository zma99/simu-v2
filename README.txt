Simulador de asignación de memoria y planificación de procesos

Versión: 2.0

---------------------------------------------------------------------------------
INFORMACION:

El programa simula la asignación de memoria por criterio worst-fit
y planificación de procesos mediante el algoritmo SJF que prioriza el menor 
tiempo de irrupción

---------------------------------------------------------------------------------
ESTRUCTURA:

En la carpeta 'config' se encuentra el archivo 'datos.txt' donde se puede precargar
datos para posterior simulación de procesos.

La carpera 'src' contiene los diferentes módulos para la interfaz, simulación, 
gestión de archivo, etc.

---------------------------------------------------------------------------------
FORMATO ARCHIVO:

- Cada línea representa un proceso.
- En cada línea se indica: [ta,ti,tam]
    donde:
        ta = tiempo de arribo
        ti = tiempo de irrupción
        tam = tamaño del proceso
    todos valores tipo entero.
- El programa realiza una validación en caso que existan datos incoherentes

---------------------------------------------------------------------------------
MODO DE EJECUCIÓN:

1) Ejecutar el archivo 'main.py'
2) El programa inicia una interfaz interactiva para el usuario con un menú principal.
3) Cargar datos de procesos que participan de la simulación (manual o desde archivo).
4) Iniciar la simulación
5) El simulador se ejecutará hasta que todos los procesos terminen con 'estado = terminado'


---------------------------------------------------------------------------------
ABORTAR:

Si desea frenar la ejecución de forma forzado::
1. Presione la combinación de teclas 'Ctrl + C'
2. Cierre la ventana de su terminal
