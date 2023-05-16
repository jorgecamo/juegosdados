import juego

Juego1 = juego.Juego(str(input("Introdueix el nom del primer jugador: ")),
                     str(input("Introdueix el nom del segon jugador: ")),
                     str(input("Introdueix el nom del tercer jugador: ")),
                     int(input("Introdueix el numero de cares per al primer dau: ")),
                     int(input("Introdueix el numero de cares per al segon dau: ")),
                     int(input("Introdueix el numero de cares per al tercer dau: ")),
                     int(input("Introdueix el numero de cares per al cuart dau: ")),
                     int(input("Introdueix el numero de llançaments: ")),
                     input("Vols veure els resultats intermedis per pantalla? (S/N): "))

Juego1.jugar()
Juego1.mostrar()
