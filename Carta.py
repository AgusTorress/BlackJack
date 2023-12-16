class carta:
    def __init__(self, idCarta, tipo):
        self.tipo = tipo
        self.idCarta = idCarta
        if idCarta not in ["K", "Q", "J", "A"]:
            valor = int(idCarta) 
            self.valor = valor
        elif idCarta in ["K", "Q", "J"]:
            self.valor = 10
        else:
            self.valor = 1
    
    def es_letra(self):
        letras_permitidas = ["Q", "J", "K", "A"]
        return self.valor in letras_permitidas    



