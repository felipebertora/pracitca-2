import random


nombres = input("ingrese una lista de nombres")

nombres = nombres.split(",")

if len(nombres) < 3:
    print("no hay la cantidad suficiente de personas")
    exit 

normalizados = [nombre.lower() for nombre in nombres]
if len(set(normalizados)) != len(nombres):
    print("No puede haber nombres duplicados.")
    exit()

asignacion_valida = False

while not asignacion_valida:
    mezclados = nombres[:]
    random.shuffle(mezclados)

    asignacion_valida = True

    for i in range(len(nombres)):
        if nombres[i] == mezclados[i]:
            asignacion_valida = False
            break


for i in range(len(nombres)):
    print(f"{nombres[i]} -> {mezclados[i]}")

