class Proceso(object):
    def __init__(self):
        self.__id = None
        self.__ta = None
        self.__ti = None
        self.__tam = None
        self.__estado = 'N'  # estado = N/L/LS/E/T

    def __repr__(self):
        return f'\n[ID={self.__id}, \tTA={self.__ta}, \tTI={self.__ti}, \tTAM={self.__tam} KB, \tEST={self.__estado}]'

    def id(self):
        return self.__id

    def ta(self):
        return self.__ta

    def ti(self):
        return self.__ti

    def tam(self):
        return self.__tam

    def estado(self):
        return self.__estado


    def setid(self, id):
        self.__id = id

    def setta(self, ta):
        self.__ta = ta

    def setti(self, ti):
        self.__ti = ti

    def settam(self, tam):
        self.__tam = tam
    
    def setestado(self, estado):
        self.__estado = estado

