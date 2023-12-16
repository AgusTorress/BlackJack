import random
from Carta import carta
from collections import deque

def crear_baraja():
    cartas = deque()
    idCartas = [str(num) for num in range(2, 11)] + ["J", "Q", "K", "A"]

    tipos = ["♦", "♠️", "☘", "❤"]
    for idCarta in idCartas:
        for tipo in tipos:
            cartas.append(carta(idCarta, tipo))
    return cartas

def barajar(cartas):
    random.shuffle(cartas)
    return cartas
