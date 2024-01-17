for numero in range(5):
    # empieza en 0,1,2,3,4
    print(numero, numero * "jaja ")


buscar = 3
for numero in range(5):
    if numero == buscar:  # recuerda que es ==
        print("\n")
        print(numero, numero * "jaja ")
        break  # detiene lo que sigue del codigo

buscar = 10
for numero in range(5):
    if numero == buscar:  # recuerda que es ==
        print("\n")
        print(numero, numero * "jaja ")
        break  # detiene lo que sigue del codigo
else:
    print("no está el número buscado :c")

for char in "Te amo, Bad Bunny":
    print(char)
