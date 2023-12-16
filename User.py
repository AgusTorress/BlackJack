class user:
    def __init__(self, nombre, dineroTotal, apuesta):
        self.nombre = nombre
        self.dineroTotal = dineroTotal
        self.apuesta = apuesta
        self.misCartas = []

    def limpiar_cartas(self):
        self.misCartas = []

    def nuevoPatri(self, valor):
        if self.dineroTotal + valor < 0:
            self.dineroTotal = 0
        else:
            self.dineroTotal += valor

    def nuevaApuesta(self, apuesta):
        if apuesta <= self.dineroTotal and apuesta > 0:
            self.apuesta = apuesta
            return True
        else:
            return False

    def obtenerCarta(self, carta):
        self.misCartas.append(carta)
    
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
