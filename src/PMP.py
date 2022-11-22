class MedioPlazo(object):
    def __init__(self, mmu):
        self.__mmu = mmu

    def mmu(self):
        return self.__mmu

    def swap(self, p, q):
        self.mmu().liberar(q)
        q.setestado('L/S')
        self.mmu().ubicar(p)
        p.setestado('L')

    def extraerLS(self, proc):
        temp = list()
        #print('proc = ',proc)

        for p in proc:
           # print('En busca de los L/S: ',p)
            if p.estado() == 'L/S':
                temp.append(proc.pop(proc.index(p)))
                #print('\ntemp = ',temp)
        return temp

    def select(self, lista_procesos):
        aux = lista_procesos[:]
        #print('\naux=',aux)
        ls = self.extraerLS(aux)
        #print('\nls=',ls)
        #print('\naux=',aux)
        
        for p in ls:
            #print(p)
            for q in lista_procesos:
                #print(q)
                if p.ti() < q.ti():
                    self.swap(p, q)
                    lista_procesos[lista_procesos.index(p)].setestado(p.estado())
                    break

        return lista_procesos

    def ejecutar(self, lista_procesos):
        print('\nPLANIFICADOR MEDIANO PLAZO')
        return self.select(lista_procesos)

