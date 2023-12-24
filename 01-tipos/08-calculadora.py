n1 = input("Ingresa el primer numero: ")
n2 = input("Ingresa el segundo numero: ")

print(n1 + n2)  # los concatena

n1 = float(n1)
n2 = float(n2)

print(n1 + n2)

suma = n1 + n2
resta = n1 - n2
division = n1 / n2
multiplicacion = n1 * n2

mensaje = f"""
Para los numeros {n1} y {n2}.
El resultado de la suma es {suma}.
El resultado de la resta es {resta}.
El resultado de la division es {division}.
El resultado de la multiplicacion es {multiplicacion}.
"""

print(mensaje)
