# and, or, not
# es lo de algebra superior

gas = True
encendido = True
edad = 20

if gas and encendido:
    print("Puedes avanzar con el and")
else:
    print("uno es falso")


gas = True
encendido = False

if gas and encendido:
    print("Puedes avanzar con el and")
else:
    print("jeje uno es falso")

if gas or encendido:
    print("Puedes avanzar con el or")

if gas and not encendido:
    print("Puedes avanzar con la negacion del ENCENDIDO")

if gas and (encendido or edad >= 18):  # para el orden
    print("Cumple las 3 cosas, avanza")

# operadores de corto circuito
# cuando hay muchas operaciones hace que no ejecutes todo
    # con el and, solo hace falta que uno sea false
    # con el or, solo hace falta que uno sea true
    # Se evaluan de izquiera a derecha
if gas and encendido and edad >= 18:  # para el orden
    print("Cumple las 3 cosas, avanza")
