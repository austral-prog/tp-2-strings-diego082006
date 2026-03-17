def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    gasto = float(input(""))
    print("Dinero recibido")
    pago = int(input(""))
    print("")
    print("Vuelto")
    print("")
    vuelto = pago - gasto
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
    pass
