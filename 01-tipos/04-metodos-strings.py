perre = "  PeRRitO Feliz    "

print(perre.upper())
print(perre.lower())
print(perre.capitalize())
print(perre.title())
print(perre.strip())
print(perre.lstrip())
print(perre.rstrip())

print(perre.strip().capitalize())
print(perre.upper().strip())

print(perre.find("RR"))
print(perre.find("rr"))
print(perre.find("FASD"))

print(perre.replace("RR", "g"))
print(perre.replace("RR", "g").capitalize())
print(perre.replace("RR", "g").capitalize().lstrip())
print(perre.replace("RR", "g").lstrip().capitalize())

print("Feliz" in perre)
print("feliz" in perre)  # bolean verdaderi o falso

print("Feliz" not in perre)
