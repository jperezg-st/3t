gato = {1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9'}


def muestra_gato(gato):
    print(f"{gato[1]} | {gato[2]} | {gato[3]}")
    print("--+---+--")
    print(f"{gato[4]} | {gato[5]} | {gato[6]}")
    print("--+---+--")
    print(f"{gato[8]} | {gato[8]} | {gato[9]}")


def juego():
    jugador = "X"
    for i in range(9):
        muestra_gato(gato)
        posicion = int(input(f"En que posicion quiere colocar {jugador} "))
        gato[posicion] = jugador
        if estado_partida(gato, jugador):
            print(f"Gana jugador {jugador}")
            break
        else:
            if jugador == "X":
                jugador = "0"
            else:
                jugador = "X"


def estado_partida(gato, jugador):
    return ((gato[1] == gato[2] == gato[3] == jugador) or
            (gato[3] == gato[4] == gato[5] == jugador) or
            (gato[7] == gato[8] == gato[9] == jugador) or
            (gato[1] == gato[3] == gato[7] == jugador) or
            (gato[2] == gato[4] == gato[8] == jugador) or
            (gato[3] == gato[5] == gato[9] == jugador) or
            (gato[1] == gato[4] == gato[9] == jugador) or
            (gato[8] == gato[4] == gato[3] == jugador))


if __name__ == '__main__':
    juego()
