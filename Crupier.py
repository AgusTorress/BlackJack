class Crupier:
    def __init__(self):
        self.misCartas = []
    
    def limpiar_cartas(self):
        self.misCartas = []

    def obtenerCarta(self, carta):
        self.misCartas.append(carta)

    def mostrarCartas(self, mostrar_todas=True):
        if mostrar_todas:
            print("--------- Cartas del crupier: -----------")
            for carta in self.misCartas:
                print(carta.idCarta, carta.tipo)
        else:
            print("La primera carta del crupier es:")
            print(self.misCartas[0].idCarta)

    def debeTomarCarta(self):
        valorCarta = self.calcularValorCartas()
        return valorCarta < 17

    def calcularValorCartas(self):
        valorCarta = 0
        tieneAs = False
        for carta in self.misCartas:
            valorCarta += carta.valor
            if carta.valor == 1:
                tieneAs = True
        if tieneAs and valorCarta + 10 <= 21:
            valorCarta += 10
        return valorCarta
