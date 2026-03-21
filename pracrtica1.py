import random

categorias = {
    "programacion": ["python", "programa", "variable", "funcion", "bucle"],
    "informatica": ["cadena", "entero", "lista"],
    "cualquiera": ["perro", "casa", "auto", "arbol"]
}

puntaje = 0

guessed = []
attempts = 6
print("¡Bienvenido al Ahorcado!")
print()

# Mostrar categorías
print("Categorías disponibles:")
for categoria in categorias:
    print("-", categoria)

# Elegir categoría
eleccion = input("Elegí una categoría: ")

# Validar elección
while eleccion not in categorias:
    print("Categoría inválida.")
    eleccion = input("Elegí una categoría: ")

palabras = random.sample(categorias[eleccion], len(categorias[eleccion]))

for word in palabras:
    guessed = []
    attempts = 6

    print("\nNueva palabra!")
    while attempts > 0:

        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
                # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            puntaje = puntaje + 6
            print("¡Ganaste!")
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        
        letter = input("Ingresá una letra: ")
        
        if len(letter) != 1:
                print("solo puedes ingresar una letra, intenta nuevamente")
                continue
        else :
            if not letter.isalpha():
                print("lo que ingresaste no es una letra, porfavor ingrese nuevamente")
                continue
            





        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -=1
            print("Esa letra no está en la palabra.")
            print()
    else:
        puntaje = 0
        print(f"¡Perdiste! La palabra era: {word}")

    print("tu puntaje es :", puntaje)