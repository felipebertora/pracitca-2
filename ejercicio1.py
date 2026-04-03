text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way
to do it.
Although that way may not be obvious at first unless you're
Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good
idea.
Namespaces are one honking great idea -- let's do more of
those!"""
 

text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way
to do it.
Although that way may not be obvious at first unless you're
Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good
idea.
Namespaces are one honking great idea -- let's do more of
those!"""

#cantidad de lineas
lineas = text.splitlines()
cant_lineas = len(lineas)
cantidad_palabras= []

#cantidad de palabras
total_palabras = 0
for linea in  lineas:
    palabras = linea.split()
    cantidad_palabras.append(len(palabras))
    total_palabras += len(palabras)



promedio = total_palabras / cant_lineas

mayores = []
for i in range (cant_lineas):
   if cantidad_palabras[i] > promedio:
        mayores.append(lineas[i])

    



print("total de lineas " , cant_lineas)
print("total de palabras : ", total_palabras)
print("el promedio de palabras es: ", promedio)

print("\nLíneas con más palabras que el promedio:")
for l in mayores:
    print("-", l)