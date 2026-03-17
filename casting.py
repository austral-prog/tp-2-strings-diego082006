def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio = int(input("Precio: "))
    descuento = float(input("Descuento: "))
    cantidad = int(input("Cantidad: "))
    precio_con_descuento = precio - descuento
    print("Precio con descuento:", precio_con_descuento)
    total = precio_con_descuento * cantidad
    print("Total:", total)
    pass
