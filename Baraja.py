import random
from Carta import carta

def crear_baraja():
    cartas = []
    idCartas = [str(num) for num in range(2, 11)] + ["J", "Q", "K", "A"]

    tipos = ["DIAMANTES", "PICAS", "TREBOLES", "CORAZONES"]
    for idCarta in idCartas:
        for tipo in tipos:
            cartas.append(carta(idCarta, tipo))
    return cartas

def barajar(cartas):
    random.shuffle(cartas)
    return cartas
