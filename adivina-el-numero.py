# La máquina genera un número aleatorio. El usuario ingresa un número y la máquina indica si el número del usuario es mayor o menor

import random

print(
"""-------------------------------
¡ADIVINA EL NÚMERO!
-------------------------------""")

numMin = 0
numMax = 10
pcNum = random.randint(numMin, numMax)

print(f"La máquina ha generado un número entero entre el {numMin} y el {numMax}.")

userNum = int(input("Ingresa un número: "))

while (userNum != pcNum) :
    if (userNum < pcNum) :
        print("El número es más alto")
    else :
        print("El número es más bajo")
    
    userNum = int(input("Ingresa un número: "))

print(f"¡El número es {pcNum}, lo adivinaste!")



