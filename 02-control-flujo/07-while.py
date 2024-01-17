# numero = 1
# while numero < 100:
#     print(numero)
#     numero += numero + 1

# comento todas con ctrl c

comando = ""

while comando.lower() != "salir":
    comando = input(
        "Escribe \"salir\" para salir, si no nunca vas a salir: ")
    print(comando)


while True:
    comando = input(
        "Ahora estas en un loop infinito hasta que me digas Bye Bye: ")
    print(comando)
    if comando.lower() == "bye bye":
        break
