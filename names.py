def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre = input("Ingresar nombre: ")
    apellido = input("Ingresar apellido: ")
    print(nombre.lower() + " " + apellido.lower())
    print(nombre.title() + " " + apellido.title())
    print(nombre.upper() + " " + apellido.upper())
    print("\t" + nombre.lower() +  " " + apellido.lower())
