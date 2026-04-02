mensaje = input("ingrese un mensaje: ")
numero_fijo = int(input("ingrese un numero: "))

nuevo_mensaje = ""

for letra in mensaje:
    if letra.isalpha():
        # Convertir letra a número (posición en alfabeto)
        nueva = ord(letra) + numero_fijo
        
        # Manejar desbordes (pasarse de 'z' o 'Z')
        if letra.islower():
            if nueva > ord('z'):
                nueva -= 26
        else:
            if nueva > ord('Z'):
                nueva -= 26
        
        nuevo_mensaje += chr(nueva)
    else:
        nuevo_mensaje += letra

print(nuevo_mensaje)