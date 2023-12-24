def get_product(**datos):  # ahora es con dos asteriscos
    print(datos["id"], datos["name"])


get_product(id="id",
            name="iphone",
            desc="desc")
