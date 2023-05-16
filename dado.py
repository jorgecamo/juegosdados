import random


class Dado:
    __caras = 6

    def __init__(self, numCaras):
        self.setCaras(numCaras)

    def lanzar(self):
        return random.randint(1, self.__caras)

    def getCaras(self):
        return self.__caras

    def setCaras(self, numCaras):
        caras_permitidas = [4, 6, 8, 10, 12, 20, 120]
        if numCaras in caras_permitidas:
            self.__caras = numCaras
        else:
            raise Exception("Numero de caras incorrecto")
