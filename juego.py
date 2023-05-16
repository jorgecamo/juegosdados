import dado


class Juego:
    __nombreJugador1 = ""
    __nombreJugador2 = ""
    __nombreJugador3 = ""
    __lanzamientos = 0

    def __init__(self, NombreJugador1, NombreJugador2, NombreJugador3, CarasDado1, CarasDado2, CarasDado3, CarasDado4,
                 NumLanzamientos, VerIntermedios):
        self.set_jugador1(NombreJugador1)
        self.set_jugador2(NombreJugador2)
        self.set_jugador3(NombreJugador3)
        self.set_lanzamientos(NumLanzamientos)
        self.dado1 = dado.Dado(CarasDado1)
        if CarasDado1 == CarasDado2 or CarasDado1 == CarasDado3 or CarasDado1 == CarasDado4:
            raise Exception("No pueden haber dos dados con caras iguales.")
        self.dado2 = dado.Dado(CarasDado2)
        if CarasDado2 == CarasDado3 or CarasDado2 == CarasDado4:
            raise Exception("No pueden haber dos dados con caras iguales.")
        self.dado3 = dado.Dado(CarasDado3)
        if CarasDado3 == CarasDado4:
            raise Exception("No pueden haber dos dados con caras iguales.")
        self.dado4 = dado.Dado(CarasDado4)
        # Me guardo en un atributo booelano si necesito o no ver los datos intermedios
        self.__intermedios = (VerIntermedios in ("S", "s"))
        self.totalResultadosJugador1 = 0
        self.totalResultadosJugador2 = 0
        self.totalResultadosJugador3 = 0

    def set_jugador1(self, nombreJugador1):
        if len(nombreJugador1) > 20:
            raise Exception("La longitud del nombre del jugador 1 no puede ser mayor de 20")
        else:
            self.__nombreJugador1 = nombreJugador1

    def set_jugador2(self, nombreJugador2):
        if len(nombreJugador2) > 20:
            raise Exception("La longitud del nombre del jugador 2 no puede ser mayor de 20")
        else:
            self.__nombreJugador2 = nombreJugador2

    def set_jugador3(self, nombreJugador3):
        if len(nombreJugador3) > 20:
            raise Exception("La longitud del nombre del jugador 2 no puede ser mayor de 20")
        else:
            self.__nombreJugador3 = nombreJugador3

    def set_lanzamientos(self, numLanzamientos):
        if not 2 < numLanzamientos <= 1000:
            raise Exception("El número de lanzamientos debe de estar entre 2 y 1000")
        else:
            self.__lanzamientos = numLanzamientos

    def jugar(self):
        self.totalResultadosJugador1 = 0
        self.totalResultadosJugador2 = 0
        self.totalResultadosJugador3 = 0
        for lanzamientoActual in range(self.__lanzamientos):
            # jugador1
            resultadoDado1 = self.dado1.lanzar()
            resultadoDado2 = self.dado2.lanzar()
            resultadoDado3 = self.dado3.lanzar()
            resultadoDado4 = self.dado4.lanzar()
            self.totalResultadosJugador1 += (resultadoDado1 + resultadoDado2 + resultadoDado3 + resultadoDado4)

            if self.__intermedios:
                print(f"Lanzamiento {lanzamientoActual + 1}:")
                print(
                    f"{self.__nombreJugador1}: {resultadoDado1} {resultadoDado2} "
                    f"{resultadoDado3} {resultadoDado4} ({self.totalResultadosJugador1})")

            # jugador2
            resultadoDado1 = self.dado1.lanzar()
            resultadoDado2 = self.dado2.lanzar()
            resultadoDado3 = self.dado3.lanzar()
            resultadoDado4 = self.dado4.lanzar()
            self.totalResultadosJugador2 += (resultadoDado1 + resultadoDado2 + resultadoDado3)

            if self.__intermedios:
                print(
                    f"{self.__nombreJugador2}: {resultadoDado1} {resultadoDado2} "
                    f"{resultadoDado3} ({self.totalResultadosJugador2})")

            # jugador3
            resultadoDado1 = self.dado1.lanzar()
            resultadoDado2 = self.dado2.lanzar()
            resultadoDado3 = self.dado3.lanzar()
            self.totalResultadosJugador3 += (resultadoDado1 + resultadoDado2 + resultadoDado3 + resultadoDado4)

            if self.__intermedios:
                print(
                    f"{self.__nombreJugador2}: {resultadoDado1} {resultadoDado2} "
                    f"{resultadoDado3} {resultadoDado4} {resultadoDado3} ({self.totalResultadosJugador3})")
                print("")

    def mostrar(self):
        print("Resultados:")
        print(f"Jugador 1: {self.__nombreJugador1}")
        print(f"Jugador 2: {self.__nombreJugador2}")
        print(f"Jugador 3: {self.__nombreJugador3}")
        print(f"Numero de lanzamientos: {self.__lanzamientos}")
        print(f"Dados: {self.dado1.getCaras()},{self.dado2.getCaras()} , {self.dado3.getCaras()} "
              f"y {self.dado4.getCaras()} ")
        print(f"Puntos jugador 1: {self.totalResultadosJugador1}")
        print(f"Puntos jugador 2: {self.totalResultadosJugador2}")
        print(f"Puntos jugador 3: {self.totalResultadosJugador3}")
        if self.totalResultadosJugador1 > self.totalResultadosJugador2 and \
                self.totalResultadosJugador1 > self.totalResultadosJugador3:
            print(f"El GANADOR es {self.__nombreJugador1} con {self.totalResultadosJugador1} puntos")
        elif self.totalResultadosJugador1 == self.totalResultadosJugador2 and \
                self.totalResultadosJugador1 == self.totalResultadosJugador3:
            print("Ha habido un EMPATE")
        elif self.totalResultadosJugador2 > self.totalResultadosJugador1 and \
                self.totalResultadosJugador2 > self.totalResultadosJugador3:
            print(f"El GANADOR es {self.__nombreJugador2} con {self.totalResultadosJugador2} puntos")
        else:
            print(f"El GANADOR es {self.__nombreJugador3} con {self.totalResultadosJugador3} puntos")
