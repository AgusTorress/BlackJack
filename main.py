from Baraja import crear_baraja, barajar
from User import nuevoPatri, nuevaApuesta, user, obtenerCarta, limpiar_cartas
def main():
    # Crear baraja
    cartas = crear_baraja()

    # Barajar las cartas
    cartas = barajar(cartas)

    # Imprimir las cartas en el orden aleatorio
    #for carta in cartas_barajadas:
        #print(carta.valor, carta.tipo)
    usuarios = []
    seguir_jugando = True
    while seguir_jugando:
        crearUser = str(input("Desea crear un usuario? ")) in ["Si", "si"]
        while crearUser:
            nombre = str(input("Ingrese el nombre del usuario: "))  
            if any(nombre == usuario.nombre for usuario in usuarios):
                print("Ya hay un usuario con ese nombre en el sistema.")         
            else:
                usuarios.append(user(nombre, 5000, 0))
            crearUser = str(input("Desea seguir agregando usuarios? ")) in ["Si", "si"]
        indice = 0
        for u in usuarios:
            ok = False
            while not ok:
                print(u.nombre + ", su saldo es: " + str(u.dineroTotal) + '\n' )
                ok = nuevaApuesta(u, int(input("Ingrese cuanto desea apostar: ")))
        for u in usuarios:
            obtenerCarta(u, cartas[indice])
            obtenerCarta(u, cartas[indice+1])
            indice = indice + 2
            print(" ------------" + u.nombre + " ------------")
            for carta in u.misCartas:
                print(u.nombre + " tus cartas son: " + carta.idCarta + " " + carta.tipo)
        for u in usuarios:
            valorCarta = 0
            for carta in u.misCartas:
                valorCarta += carta.valor 
            if valorCarta == 21:
                nuevoPatri(u, u.apuesta * 2)
                print("BLACKJACK!")
            elif valorCarta > 21:
                nuevoPatri(u, - u.apuesta)
                print(u.nombre + ", has perdido, el valor de tus cartas es: " + str(valorCarta))
            else:
                seguirAgarrando = str(input(u.nombre + ", desea seguir tomando cartas? ")) in ["Si", "si"]
                while valorCarta < 21 and seguirAgarrando:
                    cartita = cartas[indice]
                    obtenerCarta(u, cartita)
                    for carta in u.misCartas:
                        print(u.nombre + " tus cartas son: " + carta.idCarta + " " + carta.tipo)
                    valorCarta += cartita.valor
                    seguirAgarrando = str(input(u.nombre + ", desea seguir tomando cartas? ")) in ["Si", "si"]
                if valorCarta == 21:
                    print("BLACKJACK!")
                    nuevoPatri(u, u.apuesta * 2)
                elif valorCarta > 21:
                    print("Has perdido, el valor de tus cartas es: " + str(valorCarta))
                    nuevoPatri(u, - u.apuesta)
        seguir_jugando = str(input("Desea seguir jugando? ")) in ["Si", "si"]
        for u in usuarios:
            limpiar_cartas(u)
        cartas = crear_baraja()
        cartas = barajar(cartas)
        
                

        


if __name__ == "__main__":
    main()
