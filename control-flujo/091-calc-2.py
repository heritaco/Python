descripcion_cal = """ 
Para salir escribe \"0\"
Tienes + - / *
"""

n = ""
m = ""

print(descripcion_cal)

while True:
    if not n:
        n = input("ingrese el primer numero: ")
        if n.lower() == "salir":
            break
        n = float(n)
    op = input("ingresa operación: ")
    if op.lower() == "salir":
        break
    m = ("ingresa el siguiente num: ")
    if m.lower() == "salir":
        break
    m = float(m)

    if op == "+":
        n += m
    elif op == "-":
        n -= m
    elif op == "*":
        n *= m
    elif op == "/":
        n /= m
    else:
        print("no valido")

    print(n)
