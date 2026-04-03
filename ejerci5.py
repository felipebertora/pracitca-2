peso = input("ingrese el peso del paquete en kilos ")
zona = input("ingrese el tipo de envio(local/regional/nacional)")

peso = int(peso)

if peso < 1:
    if zona == "local":
        costo = 500
    elif zona == "regional":
     costo = 1000
    else:
     costo = 2000
elif peso < 5:
    if zona == "local":
     costo = 1000
    elif zona == "regional":
     costo = 2500
    else:
     costo = 4500
else:
 if zona == "local":
     costo = 2000
 elif zona == "regional":
     costo = 5000
 else:
     costo = 8000
        

print("El costo del envio es de: $",costo)