class MedioPlazo(object):
    def __init__(self, mmu):
        self.__mmu = mmu

    def mmu(self):
        return self.__mmu

    def swap(self, p, q):
        # Intercambia el proceso q por
        # el proceso p
        self.mmu().liberar(q)
        q.setestado('L/S')
        self.mmu().ubicar(p)
        p.setestado('L')

    def extraer(self, proc, est):
        # Toma una lista de procesos admitidos y
        # extrae aquellos con estado = L/S 
        # retornandolos como una lista nueva
        aux = proc[:]
        temp = list()
        for p in proc:
            if p.estado() == est:
                temp.append(aux.pop(aux.index(p)))
        return temp

    def select(self, lista_procesos):
        # Compara los proceos  L/S con los L
        # Si los L/S tienen menor TI intercambia
        # con el proceso estado=L
        # sólo si cabe en la misma partición
        aux = lista_procesos[:]
        ls = self.extraer(aux, 'L/S')
        for p in ls:
            for q in lista_procesos:
                if self.mmu().cabe(p,q) and p.ti() < q.ti():
                    self.swap(p, q)
                    lista_procesos[lista_procesos.index(p)].setestado(p.estado())
                    break

        aux = lista_procesos[:]
        ls = self.extraer(aux, 'L/S')
        for p in ls:
            for q in lista_procesos:
                if len(self.extraer(aux, 'L')) < 3 and self.mmu().cabe(p,q):
                    self.swap(p, q)
                    lista_procesos[lista_procesos.index(p)].setestado(p.estado())
                    break  
    
        aux = lista_procesos[:]
        ls = self.extraer(aux, 'L/S')
        for p in ls:
            if self.mmu().cabe(p):
                self.mmu().ubicar(p)
                lista_procesos[lista_procesos.index(p)].setestado('L')

        return lista_procesos

    def ejecutar(self, lista_procesos):
        return self.select(lista_procesos)

