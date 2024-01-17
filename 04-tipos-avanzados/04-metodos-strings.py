animal = "    MONito FeLEliz e e e mocoso "
print(animal.upper())  # PONE TODO EN MAYUSCULAS
print(animal.lower())  # pone todas en minusculas
print(animal.capitalize())  # Lo escribe bien
print(animal.title())  # Pone Las Letras Asi
print(animal.strip())  # elimina espacios a la izquierda y derecha
# capitalize tiene que estar stripeado. Para que lo escriba bien
print(animal.strip().capitalize())
print(animal.lstrip())  # quita los de la izquierda
print(animal.rstrip())  # aja
print(animal.find("mo"))  # encuentra el indice del string que buscamos
print(animal.find("juan"))  # da negativo, aka no está
print(animal.replace("MON", "CHANGU"))
print(animal.replace("MON", "CHANGU").capitalize())
print(animal.replace("MON", "CHANGU").strip().capitalize())
print(animal.replace("MON", "CHANGU").replace(
    "mocoso", "changoso").strip().capitalize())

print("mocoso" in animal)
print("feliz" in animal)
print("mocoso" not in animal)
print("feliz" not in animal)  # Boolean, si o no
