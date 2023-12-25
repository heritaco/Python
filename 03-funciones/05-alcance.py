def saludar():
    saludo = "hola"
    print(saludo)


def saludarbonito():
    saludo = "ola"  # son variables diferentes
    print(saludo)

# print(saludo) !!


saludar()
saludarbonito()
saludar()


# contexto global
saludo = "buenos dias global"


# def saludar3():
#     print(saludo)
#     saludo = "ola"  # el error esta en que no puedes llamar globales en funciones

def saludar2():
    print(saludo)


saludar2()

#
# ES MEJOR NO USAR GLOBALES, pero siii quieres
#


def saludarglob():
    global saludo
    saludo = "ya es de la funcion pero mejor no usar globaes"


saludarglob()
