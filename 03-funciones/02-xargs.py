def suma(a, b):
    print("\nsuma")
    print(a+b)


suma(2, 5)


def sumaxarg(*numeros):  # el asterisco es la iteracion
    print("\nsumaxarg")
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


def sumaxarg2(*numeros):  # el asterisco es la iteracion
    print("\nsumaxarg2")
    resultado = 0
    for numero in numeros:
        resultado += numero
        print(resultado)  # importa el orden


sumaxarg(2, 5)
sumaxarg(2, 5, 13, 132, 543, 654, 123, 4, 1, 543, 5432, 542, 54, 6, 7665)
sumaxarg2(2, 5, 13, 132)
