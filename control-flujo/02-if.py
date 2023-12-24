cromosoma = input("Con que cromosoma sexual naciste? eg xx, xy \n")
estatura = input("Ingresa la estatura en cm: ")

estatura = int(estatura)

if cromosoma == "xy":
    if estatura >= 200:  # importa el orden
        print("Estas MUY alto")
    elif estatura >= 185:
        print("Estas alto")
    elif estatura >= 170:
        print("Estas muy promedio")
    else:
        print("Chaparro")
        print("Muere")

if cromosoma == "xx":
    if estatura >= 190:  # importa el orden
        print("Estas MUY alta")
    elif estatura >= 170:
        print("Estas alta")
    elif estatura >= 160:
        print("Estas muy promedio")
    else:
        print("Chaparra")
        print("Muere")

print("Listo, ten un buen día")
