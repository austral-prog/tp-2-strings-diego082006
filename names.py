def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre = input()
    apellido = input()
    
    print(f"{nombre.lower()} {apellido.lower()}")
    print(f"{nombre.title()} {apellido.title()}")
    print(f"{nombre.upper()} {apellido.upper()}")
    print(f"\t{nombre.lower()} {apellido.lower()}")
