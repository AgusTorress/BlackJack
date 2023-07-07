class user:
    nombre = ""
    dineroTotal = 0
    apuesta = 0
    misCartas = []
    
    def __init__(self, nombre, dineroTotal, apuesta):
        self.nombre = nombre
        self.dineroTotal = dineroTotal
        self.apuesta = 0
    
def limpiar_cartas(self):
    self.misCartas = []
        
def nuevoPatri(self, valor):
    if self.dineroTotal + valor < 0:
        self.dineroTotal = 0
    else:
        self.dineroTotal += valor
        
def nuevaApuesta(self, apuesta):
    if apuesta <= self.dineroTotal:
        self.apuesta = apuesta
        return True
    else:
        return False

def obtenerCarta(self, carta):
    self.misCartas.append(carta)
