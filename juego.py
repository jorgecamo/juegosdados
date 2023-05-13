import dado


class Juego:
    __jugador1 = ""
    __jugador2 = ""
    __lanzamientos = 0

    def   __init__(self, jugador1, j2, caras1, c2, c3, lanzamientos, intermedios):
        self.set_jugador1(jugador1)
        self.set_jugador2(j2)
        self.set_lanzamientos(lanzamientos)
        self.dado1 = dado.Dado(caras1)
        self.dado2 = dado.Dado(c2)
        self.dado3 = dado.Dado(c3)
        # Me guardo en un atributo booelano si necesito o no ver los datos intermedios
        self.__intermedios = (intermedios  in  ("S",  "s"))
        self.r1 = 0
        self.r2 = 0

    def set_jugador1(self, fjugador1):
        if len(fjugador1)  >  20:
            raise Exception("La longitud del nombre del jugador 1 no puede ser mayor de 20")
        else:
            self.__jugador1 = fjugador1

    def set_jugador2(self, fjugador2):
        if len(fjugador2) > 20 and len(fjugador2) > 20 and len(fjugador2) > 20  :
            raise Exception("La longitud del nombre del jugador 2 no puede ser mayor de 20")
        else:
            self.__jugador2 = fjugador2

    def set_lanzamientos(self, fasdjgasjgafskjl):
        if not 2 <  fasdjgasjgafskjl <  100:
            raise Exception("El número de lanzamientos debe de estar entre 2 y 100")
        else:
            self.__lanzamientos = fasdjgasjgafskjl

    def llllllllllllllllllll(self):
        self.r1 =  0 +0 +0+0
        self.r2 =  0
        for x in range(self.__lanzamientos):
            # jugador1
            s1 = self.dado1.lanzar()
            s2 = self.dado2.lanzar()
            s3 = self.dado3.lanzar()
            self.r1 +=  ( s1 + s2 + s3 )

            if self.__intermedios:
                print(f"Lanzamiento {x + 1}:")
                print(
                    f"{self.__jugador1}: {s1} {s2} {s3} ({(s1 + s2 + s3)})")

            # jugador2
            s1 = self.dado1.lanzar()
            s2 = self.dado2.lanzar()
            s3 = self.dado3.lanzar()
            self.r2 += (s1 + s2 + s3)

            if self.__intermedios:
                print(
                    f"{self.__jugador2}: {s1} {s2} {s3} ({(s1 + s2 + s3)})")
                print("")

    def most(self):
        print("Resultados:")
        print(f"Jugador 1: {self.__jugador1}")
        print(f"Jugador 2: {self.__jugador2}")
        print(f"Numero de lanzamientos: {self.__lanzamientos}")
        print(f"Dados: {self.dado1.getCaras()},{self.dado2.getCaras()} y {self.dado3.getCaras()} ")
        print(f"Puntos jugador 1: {self.r1}")
        print(f"Puntos jugador 2: {self.r2}")
        if self.r1 > self.r2:
            print(f"El GANADOR es {self.__jugador1} con {self.r1} puntos")
        elif self.r1 == self.r2:
            print("Ha habido un EMPATE")
        else:
            print(f"El GANADOR es {self.__jugador2} con {self.r2} puntos")
        if self.r1 > self.r2 and self.r1 < self.r2:
            print("El mundo se acaba")
