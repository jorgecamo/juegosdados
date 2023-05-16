import dado


class Juego:
    __nombreJugador1 = ""
    __nombreJugador2 = ""
    __lanzamientos = 0

    def __init__(self, NombreJugador1, NombreJugador2, CarasDado1, CarasDado2, CarasDado3,
                 NumLanzamientos, VerIntermedios):
        self.set_jugador1(NombreJugador1)
        self.set_jugador2(NombreJugador2)
        self.set_lanzamientos(NumLanzamientos)
        self.dado1 = dado.Dado(CarasDado1)
        self.dado2 = dado.Dado(CarasDado2)
        self.dado3 = dado.Dado(CarasDado3)
        # Me guardo en un atributo booelano si necesito o no ver los datos intermedios
        self.__intermedios = (VerIntermedios in ("S", "s"))
        self.totalResultadosJugador1 = 0
        self.totalResultadoJugador2 = 0

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

    def set_lanzamientos(self, numLanzamientos):
        if not 2 < numLanzamientos < 100:
            raise Exception("El número de lanzamientos debe de estar entre 2 y 100")
        else:
            self.__lanzamientos = numLanzamientos

    def jugar(self):
        self.totalResultadosJugador1 = 0
        self.totalResultadoJugador2 = 0
        for lanzamientoActual in range(self.__lanzamientos):
            # jugador1
            resultadoDado1 = self.dado1.lanzar()
            resultadoDado2 = self.dado2.lanzar()
            resultadoDado3 = self.dado3.lanzar()
            self.totalResultadosJugador1 += (resultadoDado1 + resultadoDado2 + resultadoDado3)

            if self.__intermedios:
                print(f"Lanzamiento {lanzamientoActual + 1}:")
                print(
                    f"{self.__nombreJugador1}: {resultadoDado1} {resultadoDado2} "
                    f"{resultadoDado3} ({self.totalResultadosJugador1})")

            # jugador2
            resultadoDado1 = self.dado1.lanzar()
            resultadoDado2 = self.dado2.lanzar()
            resultadoDado3 = self.dado3.lanzar()
            self.totalResultadoJugador2 += (resultadoDado1 + resultadoDado2 + resultadoDado3)

            if self.__intermedios:
                print(
                    f"{self.__nombreJugador2}: {resultadoDado1} {resultadoDado2} "
                    f"{resultadoDado3} ({self.totalResultadoJugador2})")
                print("")

    def mostrar(self):
        print("Resultados:")
        print(f"Jugador 1: {self.__nombreJugador1}")
        print(f"Jugador 2: {self.__nombreJugador2}")
        print(f"Numero de lanzamientos: {self.__lanzamientos}")
        print(f"Dados: {self.dado1.getCaras()},{self.dado2.getCaras()} y {self.dado3.getCaras()} ")
        print(f"Puntos jugador 1: {self.totalResultadosJugador1}")
        print(f"Puntos jugador 2: {self.totalResultadoJugador2}")
        if self.totalResultadosJugador1 > self.totalResultadoJugador2:
            print(f"El GANADOR es {self.__nombreJugador1} con {self.totalResultadosJugador1} puntos")
        elif self.totalResultadosJugador1 == self.totalResultadoJugador2:
            print("Ha habido un EMPATE")
        else:
            print(f"El GANADOR es {self.__nombreJugador2} con {self.totalResultadoJugador2} puntos")
