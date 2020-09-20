from random import randint
import time

#Saludo del juego
print ( " " )
print ('Bienvenidos a Juego de dados')
print ( " " )
time.sleep(1)

#Saludo a Jugador 1
print('Insertar nombre de Jugador1: ',end='')
jugador1 = input()
def Hello1():
    "Saludo a jugador 1"
    print("- Hola " + jugador1 + ' eres el primer jugador')
Hello1()
print ( " " )

time.sleep(1)

# Saludos a jugador 2
print('Insertar nombre de Jugador2: ',end='')
jugador2 = input()
def Hello2():
    "Saludo a jugador 2"
    print("- Hola " + jugador2 + ' eres el segundo jugador')
Hello2()
print ( " " )
time.sleep(1)

#Deficion de funcion tiro de dado
def tiro_dado():
    'imprime el random de cada dados'
    return randint (1,6)

# imprime instruccions
print('**INSTRUCCIONES**')
print('- Cada jugador lanzara dos dados')
time.sleep(0.7)
print('- Para lanzar cada dado Presiona Enter')
time.sleep(0.7)
print('- La suma de ambos dados sera tu puntaje')
time.sleep(0.7)
print('- El puntaje mayor sera el ganador')
time.sleep(0.7)
print('')
print('Buena Suerte')
print('')
print('')
time.sleep(1.1)
#Bucle
juega_otra="Si"
while juega_otra=="Si" or juega_otra=="" or juega_otra=="si" or juega_otra==" Si" or juega_otra==" SI"or juega_otra==" =SI"or juega_otra==" si" or juega_otra=="yes" or juega_otra=="Yes" or juega_otra==" yes" or juega_otra==" Yes":

#Resultado de primer jugador
    print('Los tiros de ' + jugador1 + ' son los siguientes:' )
    primer_dado = tiro_dado()
    segundo_dado = tiro_dado()
    suma = primer_dado + segundo_dado
    input()
    print (f'El primer dado ha caido: {primer_dado}')
    input()
    print (f'El segundo dado ha caido: {segundo_dado}')
    time.sleep(0.2)
    print ('')
    print(f"El total de puntos de {jugador1}  es: {suma} ")
    print ( " " )
    time.sleep(1.1)

#Resultado de segundo jugador
    print('Los tiros de ' + jugador2 + ' son los siguientes:' )
    tercer_dado = tiro_dado()
    cuarto_dado = tiro_dado()
    suma2 = tercer_dado + cuarto_dado
    input()
    print (f'El primer dado ha caido: {tercer_dado}')
    input()
    print (f'El segundo dado ha caido: {cuarto_dado}')
    time.sleep(0.2)
    print ('')
    print(f"El total de puntos de {jugador2} es: {suma2}")
    print ('')

#Resultado del ganador
    if suma > suma2:
        print(f'El ganador del juego es {jugador1} con un puntaje total de: {suma}')
    elif suma < suma2:
        print(f'El ganador del juego es {jugador2} con un puntaje total de: {suma2}')
    else:
        print(f'El juego es un empate con un puntaje total de: {suma}')
    print("")

    #Consulta tirar nuevamente
    juega_otra= input('Â¿Quieres jugar nuevamente y lanzar los dados? Ingresa si o no :')
