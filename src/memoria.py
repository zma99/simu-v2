
class Memoria(object):
    def __init__(self, datos_part):
        self.__particiones = list()
        self.crearParticiones(datos_part)
        
    def __str__(self):
        return str(self.__particiones)

    def __repr__(self):
        return str(self.__particiones)

    def particiones(self):
        return self.__particiones

    def particionId(self, id):
        for part in self.particiones():
            if part.id() == id:
                return part


    def crearParticiones(self, datos_part):
        # Recibe lista con valores enteros = tamaño de partición
        # Cada elemento de la lista cuenta como una partición
        # Ejemplo: [tamP1, tamP2, ..., tamPn]
        # tam = tamaño / Pi = partición i-ésima
        ultima_dir = 0
        for i in range(0, len(datos_part)):
            part = Particion(i+1, ultima_dir, datos_part[i], None)
            ultima_dir += part.tam()
            self.__particiones.append(part)

    def memoriaLibre(self):
        # Retorna True si hay memoria disponible
        # o False en caso contrario
        libres = list()
        for part in self.__particiones:
            libres.append(part.libre())
        return libres.count(True) > 0


    def partLibreMayor(self):
        # Busca en memoria la partición de mayor tamaño
        # que está disponible (sin proceso asignado)
        # retorna un objeto Particion()
        mayor = 0
        partMayor = None
        for part in self.__particiones:
            if part.libre() and part.tam() > mayor:
                partMayor = part
                mayor = part.tam()

        return partMayor

    def worstfit(self, proceso):
        # Realiza la asignación de proceso en memoria
        # por criterio worst-fit (donde mayor frag. se genera)
        # Si se asigna un proceso devuelve True o contrario False 
        part = self.partLibreMayor()
        if not part is None and proceso.tam() <= part.tam():
            part.asignar(proceso)
            return True
        
        return False
        
    def liberar(self, proceso):
        # Libera una partición del proceso asignado
        for part in self.__particiones:
            if part.id() != 0 and not part.procAsignado() is None and proceso.id() == part.procAsignado().id():
                part.liberar()
                proceso.setpart(None)





class Particion(object):
    def __init__(self, id, dirInicio, tam, procAsginado):
        self.__id = id
        self.__dirInicio = dirInicio
        self.__tam = tam
        self.__procAsignado = procAsginado

    def __str__(self):
        return f'id={self.__id}'
    
    def __repr__(self):
        return f'[id={self.__id},Tam={self.__tam}]'

    def id(self):
        return self.__id

    def dirInicio(self):
        return self.__dirInicio

    def tam(self):
        return self.__tam

    def procAsignado(self):
        return self.__procAsignado



    def asignar(self, proceso):
        self.__procAsignado = proceso
        proceso.setpart(self.id())


    def fragmentacion(self):
        # Calcula la fragmentación interna
        # de la partición
        if self.__procAsignado is None:
            return 0
        
        return self.__tam - self.__procAsignado.tam()


    def libre(self):
        # Retorna True si la partición está disponible
        # de lo contrario False
        if self.__id != 1 and self.__procAsignado is None:
            return True

        return False

    def liberar(self):
        self.__procAsignado = None
