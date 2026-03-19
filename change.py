def change():
    """ee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    print("Ingresar gasto:")
    gasto = float(input())
    
    print("Dinero recibido")
    pago = int(input())
    
    vuelto_centavos = int(round((pago - gasto) * 100))
    
    pesos = vuelto_centavos // 100
    centavos = vuelto_centavos % 100
    
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
