mail = input("ingrese su email")

valido = True

if(mail.count("@") != 1):
    valido = False

usuario, dominio = mail.split("@")

if(len(usuario) == 0):
    valido = False

if(dominio.count(".") == 0):
   valido = False

if mail.startswith("@") or mail.endswith("@"):
    valido = False


if mail.startswith("..") or mail.endswith(".."):
    valido = False

if len(dominio) < 2:
    valido = False

if valido == True:
    print("el email es valido")
else:
    print("el email es invalido")