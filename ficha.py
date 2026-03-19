def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    nombre = input().strip().title()
    email = input().lower()
    nota1 = int(input())
    nota2 = int(input())
    nota3 = int(input())

    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")

    print(f"Nombre: {nombre}")
    print(f"Email: {email}")
    print(f"Caracteres en nombre: {len(nombre)}")

    espacio = nombre.find(" ")
    iniciales = nombre[0] + nombre[espacio + 1]
    print(f"Iniciales: {iniciales}")

    nombre_lower = nombre.lower()
    espacio = nombre_lower.find(" ")
    usuario = nombre_lower[espacio + 1:] + "." + nombre_lower[:espacio]
    print(f"Usuario: {usuario}")

    print(f"Email valido: {'@' in email}")

    arroba = email.find("@")
    dominio = email[arroba + 1:]
    print(f"Dominio: {dominio}")

    print(f"Nombre para archivo: {nombre.replace(' ', '_')}")
    print(f"Cantidad de a: {nombre.lower().count('a')}")
    print(f"Codigo secreto: {nombre[::-1].upper()}")

    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")

    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    promedio_entero = suma // 3

    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")

    print("========================")
