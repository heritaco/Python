def esta_funcion_quita_espacios(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def esta_funcion_lo_pone_de_reversa(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    # eliminar espacios
    texto = esta_funcion_quita_espacios(texto)
    texto_al_reves = esta_funcion_lo_pone_de_reversa(texto)
    return texto.lower() == texto_al_reves.lower()


print(es_palindromo("amo la paloma"))
print(es_palindromo("juan"))


def es_palindromo2(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]


print(es_palindromo2("amo la paloma"))
