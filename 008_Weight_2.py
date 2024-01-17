# Constants for conversion factors
KG_TO_LBS = 2.205
LBS_TO_KG = 1 / KG_TO_LBS

while True:
    try:
        weight = float(input("Enter your weight: "))
        break
    except ValueError:
        print("Invalid weight. Please enter a number.")

while True:  # Loop infinito hasta que se cumpla la condicion
    # .upper() convierte a mayusculas
    unit = input("Kilograms or Pounds? (K or L): ").upper()
    if unit == "K":
        weight *= KG_TO_LBS  # *= es lo mismo que weight = weight * KG_TO_LBS
        unit = "Lbs."
        break
    elif unit == "L":
        weight *= LBS_TO_KG
        unit = "Kgs."
        break
    else:
        print(f"{unit} was not valid. Please enter K or L.")

print(f"Your weight is: {round(weight, 1)} {unit}")
