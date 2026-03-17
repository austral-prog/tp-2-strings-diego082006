def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = input("Base: ")
    altura = input("Altura: ")
    base_entera = int(base)
    altura_entera = int(altura)
    print(f"Base:  {base_entera}")
    print(f"Altura:  {altura_entera}")
    Area = base_entera * altura_entera
    print("Area: ", Area)
    Perimetro = (2 * base_entera) + (2 * altura_entera)
    print("Perimetro: ", Perimetro)
    pass
