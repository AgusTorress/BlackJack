from Baraja import crear_baraja, barajar
from User import user
from collections import deque
from Crupier import Crupier
import time

def main():
    # Crear baraja
    cartas = crear_baraja()

    # Barajar las cartas
    cartas = barajar(cartas)

    usuarios = []
    seguir_jugando = True
    
    crupier = Crupier()

    while seguir_jugando:

        crearUser = str(input("Desea crear un usuario? ")) in ["Si", "si"]
        while crearUser:
            nombre = str(input("Ingrese el nombre del usuario: "))  
            if any(nombre == usuario.nombre for usuario in usuarios):
                print("Ya hay un usuario con ese nombre en el sistema.")
            elif nombre == '':
                print("Porfavor ingrese un nombre válido")     
            else:
                usuarios.append(user(nombre, 5000, 0))
            crearUser = str(input("Desea seguir agregando usuarios? ")) in ["Si", "si"]  
        
        

        for u in usuarios:
            ok = False
            while not ok:
                print("------------")
                print(u.nombre + ", su saldo es: " + str(u.dineroTotal))
                ok = u.nuevaApuesta(int(input("Ingrese cuanto desea apostar: ")))
                if not ok:
                    print("------------")
                    print("ERROR: Tu saldo es menor a la cantidad de dinero que quieres apostar.")
                    print("------------")

        print("------------")

        for u in usuarios:
            u.obtenerCarta(cartas.pop())
            u.obtenerCarta(cartas.pop())

        for u in usuarios:
            print("----- " + u.nombre + " -----")
            print("Tus cartas son: ")
            for carta in u.misCartas:
                print(carta.idCarta + " " + carta.tipo)
            valorCarta = u.calcularValorCartas() 
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
            print('')
            
        while crupier.debeTomarCarta():
            crupier.obtenerCarta(cartas.pop())
            crupier.mostrarCartas()
            time.sleep(1)

        valorCartasCrupier = crupier.calcularValorCartas()
        print("------------")
        print('\n')

        for u in usuarios:
            valorCarta = u.calcularValorCartas()
            print("------------ " + u.nombre + " ------------")
            if valorCarta == 21 and valorCartasCrupier != 21:
                print("BLACKJACK!")
                u.nuevoPatri(u.apuesta * 3)
            elif  valorCarta > 21:
                print("Has perdido, el valor de tus cartas es: " + str(valorCarta))
                u.nuevoPatri(-u.apuesta)
            elif valorCartasCrupier > 21:
                print("El crupier ha perdido") 
                u.nuevoPatri(u.apuesta * 2)   
            elif valorCarta > valorCartasCrupier:
                print("Le has ganado al crupier!")
                u.nuevoPatri(u.apuesta * 2)
            elif valorCarta == valorCartasCrupier:
                print("Has empatado con el crupier!")
            else:
                print("Has perdido, el crupier te ganó.")
                u.nuevoPatri(-u.apuesta)
            if u.dineroTotal > 0:    
                print("Tu saldo ahora es de: " + str(u.dineroTotal))
            else:
                print("Te has quedado sin saldo")
                usuarios.remove(u)
            print('\n')
        
        seguir_jugando = str(input("Desea seguir jugando? ")) in ["Si", "si"]
        for u in usuarios:
            u.limpiar_cartas()
        crupier.limpiar_cartas()
        cartas = crear_baraja()
        cartas = barajar(cartas)

if __name__ == "__main__":
    main()
