# La máquina genera un número aleatorio. El usuario ingresa un número y la máquina indica si el número del usuario es mayor o menor

import random

print(
"""-------------------------------
¡ADIVINA EL NÚMERO!
-------------------------------""")

numMin = 0
numMax = 10
pcNum = random.randint(numMin, numMax)
intentos = 3

print(f"La máquina ha generado un número entero entre el {numMin} y el {numMax}.")

userNum = int(input(f"Te quedan {intentos} intento(s). Ingresa un número: "))

while (userNum != pcNum) :
    intentos -= 1
    if (userNum < pcNum) :
        print("El número es más alto")
    else :
        print("El número es más bajo")
    
    userNum = int(input(f"Te quedan {intentos} intento(s). Ingresa un número: "))

    if (intentos <= 1) :
        break

if (intentos <= 0) :
    print(f"¡PERDISTE! el número era {pcNum}")
else:
    print(f"¡El número es {pcNum}, lo adivinaste!")



