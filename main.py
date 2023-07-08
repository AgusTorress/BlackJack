from Baraja import crear_baraja, barajar
from User import user
from collections import deque
from Crupier import Crupier

def main():
    # Crear baraja
    cartas = crear_baraja()

    # Barajar las cartas
    cartas = barajar(cartas)

    usuarios = []
    seguir_jugando = True
    
    crupier = Crupier()
    lockCantUser = False
    while seguir_jugando:
        
        if not lockCantUser:
            crearUser = str(input("Desea crear un usuario? ")) in ["Si", "si"]
            while crearUser and not lockCantUser:
                nombre = str(input("Ingrese el nombre del usuario: "))  
                if any(nombre == usuario.nombre for usuario in usuarios):
                    print("Ya hay un usuario con ese nombre en el sistema.")         
                else:
                    usuarios.append(user(nombre, 5000, 0))
                crearUser = str(input("Desea seguir agregando usuarios? ")) in ["Si", "si"]  
            lockCantUser = str(input("Desea no agregar mas usuarios hasta que finalice la partida? ")) in ["Si", "si"]

        for u in usuarios:
            ok = False
            while not ok:
                print(u.nombre + ", su saldo es: " + str(u.dineroTotal) + '\n')
                ok = u.nuevaApuesta(int(input("Ingrese cuanto desea apostar: ")))
        for u in usuarios:
            u.obtenerCarta(cartas.pop())
            u.obtenerCarta(cartas.pop())

        for u in usuarios:
            print(" ------------" + u.nombre + " ------------")
            print("Tus cartas son: ")
            for carta in u.misCartas:
                print(carta.idCarta + " " + carta.tipo)  
        for u in usuarios:
            valorCarta = u.calcularValorCartas() 
            if valorCarta == 21:
                u.nuevoPatri(u.apuesta * 2)
                print("BLACKJACK!")
            elif valorCarta > 21:
                u.nuevoPatri(-u.apuesta)
                print(u.nombre + ", has perdido, el valor de tus cartas es: " + str(valorCarta))
            else:
                seguirAgarrando = str(input(u.nombre + ", desea seguir tomando cartas? ")) in ["Si", "si"]
                while valorCarta < 21 and seguirAgarrando:
                    cartita = cartas.pop()
                    u.obtenerCarta(cartita)
                    print(u.nombre + " tus cartas son: " )
                    for carta in u.misCartas:
                        print(carta.idCarta + " " + carta.tipo)
                    valorCarta = u.calcularValorCartas()
                    if valorCarta < 21:
                        seguirAgarrando = str(input(u.nombre + ", desea seguir tomando cartas? ")) in ["Si", "si"]
                """if valorCarta == 21:
                    print("BLACKJACK!")
                    u.nuevoPatri(u.apuesta * 2)
                elif valorCarta > 21:
                    print("Has perdido, el valor de tus cartas es: " + str(valorCarta))
                    u.nuevoPatri(-u.apuesta)"""
        while crupier.debeTomarCarta():
            crupier.obtenerCarta(cartas.pop())
            crupier.mostrarCartas()
        valorCartasCrupier = crupier.calcularValorCartas()
        for u in usuarios:
            valorCarta = u.calcularValorCartas()
            if  valorCarta > 21:
                print("Has perdido, el valor de tus cartas es: " + str(valorCarta))
                u.nuevoPatri(-u.apuesta)
            elif valorCarta == 21:
                print("BLACKJACK!")
                u.nuevoPatri(u.apuesta * 3)
            elif valorCarta > valorCartasCrupier:
                print("Le has ganado al crupier :)")
                u.nuevoPatri(u.apuesta * 2)
            elif valorCarta == valorCartasCrupier:
                print("Has empatado con el crupier!")
            else:
                print("Has perdido, el crupier te ganó.")
                u.nuevoPatri(-u.apuesta)
        
        seguir_jugando = str(input("Desea seguir jugando? ")) in ["Si", "si"]
        for u in usuarios:
            u.limpiar_cartas()
        crupier.limpiar_cartas()
        cartas = crear_baraja()
        cartas = barajar(cartas)
        
                

        


if __name__ == "__main__":
    main()
