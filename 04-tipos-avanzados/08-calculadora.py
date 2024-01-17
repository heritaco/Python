# para que ingrese datos el usuario

n1 = input("ingresa el primer numero: ")
n2 = input("ingresa el segundo numero: ")

print(n1, ", ", n2)
print(n1+n2)

# ahorita son strings, tenemos que hacerlos integers

n1 = int(n1)
n2 = int(n2)
print(n1+n2)

suma = n1+n2
resta = n1-n2
multi = n1*n2
divi = n1/n2

mensaje = """ 
Para los numeros {n1} y {n2}
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multiplicacino es {multi}
el resultado de la division es {divi}
"""
print(mensaje)

mensaje = f""" 
Para los numeros {n1} y {n2}
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multiplicacino es {multi}
el resultado de la division es {divi}
"""  # NECESITAS LA F
print(mensaje)
