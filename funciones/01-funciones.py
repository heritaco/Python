print("ola")  # ejemplo de funcion


def ola():
    print("\nola")
    print("hiciste tu primera funcion")
    print("wuu ves")


ola()


def ola2(nombre, apellido, num_fav):
    print("\nola2")
    print("argumentos y parametros de la funcion")
    print(f"wuu ves {nombre} {apellido} con num fav {num_fav}")  # parametros


ola2("heri", "esp", 8)  # argumentos


def ola3(nombre="no pusiste nombre", apellido="no pusiste apellido", num_fav="no se"):
    print("\nola3")
    print("ahora tu")
    print(f"wuu ves {nombre} {apellido} con num fav {num_fav}")  # parametros


ola3("juan")  # argumentos
ola3(num_fav=632, apellido="perez")  # argumentos
