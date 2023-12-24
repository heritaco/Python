descripcion_cal = """ 
Para salir escribe \"0\"
Tienes + - / *
"""

n = ""
m = ""

print(descripcion_cal)

if n == "":
    n = input("Ingresa el primer número: ")

    if n == "0":
        print("bye")

    while n != 0:
        m = input("ingresa el siguiente num: ")
        if m == "0":
            print("bye bye")
            break
        else:
            m = float(m)
            n = float(n)
            n = n + m
            print(n)
