review = """La película sigue a un grupo de astronautas que
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo
a través
de tormentas solares y fallos en el sistema de navegación. Al
llegar
a Marte descubren que la base está abandonada y los
suministros
destruidos. Torres decide sacrificar la nave nodriza para
salvar
al equipo y logran volver a la Tierra en una cápsula de
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje
secreto."""




palabras = input("ingrese una palabra que considere spoiler")

lista_palabras = []
lista_palabras = palabras.split(",")

for prohibidas in lista_palabras:
    
    if review.find(prohibidas) != -1:
        review = review.replace(prohibidas, "*" * len(prohibidas))
    
print(review)