import random
import time


while True:
    res = input("Desea lanzar los dados (s/n): ")

    if res != 's':
        exit(0)

    print('Tirando dados...')
    time.sleep(.7)

    n1 = random.randint(1,6)

    print('Ya casi')
    n2 = random.randint(1,6)
    time.sleep(.7)

    print(f"el dado_primero cayo en: {n1} y el dado_segundo en: {n2}")
    print(f"la suma de los dos dados lanzados es: {n1 + n2}\n")

    # res =input('desea lanzar los dados: s/n ')
