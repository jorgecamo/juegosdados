import juego

Juego1 = juego.Juego(str(input("Introduce el nombre del primer jugador: ")),
                     str(input("Introduce el nombre del segundo jugador: ")),
                     str(input("Introduce el nombre del tercer jugador: ")),
                     int(input("Introduce el numero de caras para el primer dado: ")),
                     int(input("Introduce el numero de caras para el segundo dado: ")),
                     int(input("Introduce el numero de caras para el tercer dado: ")),
                     int(input("Introduce el numero de caras para el cuarto dado: ")),
                     int(input("Introduce el numero de lanzamientos: ")),
                     input("¿Quieres ver los resultados intermedios por pantalla? (S/N): "))

Juego1.jugar()
Juego1.mostrar()
