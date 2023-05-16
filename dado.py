import random

"""
# Esta es la clase dado
Y lo que hace es crear un dado con el numero de caras que le pasas, 
y tambien te comprueba si ese numero de caras esta permitido.
Hay un metodo que sirve para lanzar ese dado.
---
"""


class Dado:
    __caras = 6

    def __init__(self, numCaras):
        """
       **Este es el constructor de dicha clase dado,
        que recibe un parametro de entrada que es el numero de caras,
        y lo envia al metodo set para comprobar ese numero.**
        :param numCaras: INT
        """
        self.setCaras(numCaras)  # Esta es la llamada al metodo que le pasas el numero de caras

    def lanzar(self):
        """
        **Este es el metodo lanzar, y lo que hace es lanzar el dado,
        y te devuelve un int aleatorio entre 1 y el numero maximo de caras.**
        :return: Int Random de las caras del dado
        """
        return random.randint(1, self.__caras)

    def getCaras(self):
        """
        **Este es el metodo get y sirve para poder mostrar
         el numero maximo de caras.**
        :return: Int de las caras
        """
        return self.__caras

    def setCaras(self, numCaras):
        """
        **Este es el metodo que te comprueba que el numero dado es correcto
        tiene que estar en ese vector de int.**
        :param numCaras: Int del numero de caras seleccionadas por el usuario
        :return:Asigna el numero de caras.
        """
        caras_permitidas = [4, 6, 8, 10, 12, 20, 120, 200, 300]  # Vector con los numero permitidos de caras.
        if numCaras in caras_permitidas:  # este for recorre el vector anterior y comprueba si esta.
            self.__caras = numCaras
        else:
            raise Exception("Nombre de cares incorrectes")  # si no esta lanza esta excepcion
