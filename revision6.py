import random

n1 = random.randint(1,6)
n2 = random.randint(1,6)
suma = n1+n2

juega_otra_vez = "si"

while juega_otra_vez == "si" or juega_otra_vez == "s":
    print("Lanzando los dados...")
    print("Los nÃºmeros son los siguientes...")
    print(n1)
    print(n2)
    print("La suma de los dados es...", suma)
    juega_otra_vez = input("Â¿Tirar los dados otra vez?")
