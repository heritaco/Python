name = input("Enter your name: ")
phone_number = input("Enter your phone #: ")

length = len(name) # Cuenta el numero de caracteres
index = name.find(" ") # Busca el primer espacio en blanco
name = name.capitalize() # Pone la primera letra en mayuscula
name = name.upper()  # Pone todo en mayuscula
name = name.lower()  # Pone todo en minuscula
result = name.isdigit() # Devuelve True si es un numero
result = name.isalpha() # Devuelve True si es una letra
result = phone_number.count(" ") # Cuenta el numero de espacios en blanco
phone_number = phone_number.replace("-", "") # Reemplaza el guion por nada
