import random

Random = random.randint

def LanzarDado():
    return Random(1,6)

x=0

while x == 0:
    Dado1 = LanzarDado()
    Dado2 = LanzarDado()
    print("El primer dado ha caido: ",Dado1," y el segundo dado ha caido en ",Dado2)
    print("La suma total de los dados es: ",Dado1+Dado2)
    a=0
    while not(a == 1) and not(a == 2):
        while True:
            a = input("Â¿Desea lanzar nuevamente los dados?(1-Si|2-No)")
            try:
                a = int(a)
                break
            except ValueError:
                print("La entrada es incorrecta: escribe un numero entero")

        if not(int(a) == 1) and not(int(a) == 2):
            print("La opcion ingresada no es valida")
    if a == 2:
        break
