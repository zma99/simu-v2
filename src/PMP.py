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

    def extraerLS(self, proc):
        # Toma una lista de procesos admitidos y
        # extrae aquellos con estado = L/S 
        # retornandolos como una lista nueva
        aux = proc[:]
        temp = list()
        for p in proc:
            if p.estado() == 'L/S':
                temp.append(aux.pop(aux.index(p)))
        return temp

    def select(self, lista_procesos):
        # Compara los proceos  L/S con los L
        # Si los L/S tienen menor TI intercambia
        # con el proceso estado=L
        # sólo si cabe en la misma partición
        aux = lista_procesos[:]
        ls = self.extraerLS(aux)
        for p in ls:
            for q in lista_procesos:
                if p.ti() < q.ti() and self.mmu().cabe(p,q):
                    self.swap(p, q)
                    lista_procesos[lista_procesos.index(p)].setestado(p.estado())
                    break

        return lista_procesos

    def ejecutar(self, lista_procesos):
        return self.select(lista_procesos)

