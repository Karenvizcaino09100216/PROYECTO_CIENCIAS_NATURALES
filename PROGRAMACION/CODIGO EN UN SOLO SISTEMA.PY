print("hola bienvenido al programa de fisica")
print("")
print("antes de empezar te explico los dos tipos de movimiento:")
print("")
print("MRU - movimiento rectilineo uniforme")
print("es cuando un objeto se mueve en linea recta")
print("con velocidad constante, es decir que no acelera ni frena")
print("la formula principal es: distancia = velocidad * tiempo")
print("")
print("MRUA - movimiento rectilineo uniformemente acelerado")
print("es cuando un objeto se mueve en linea recta")
print("pero su velocidad va cambiando porque hay una aceleracion constante")
print("un ejemplo de esto es cuando algo cae por gravedad")
print("las formulas que se usan son:")
print("  vf = vo + a * t")
print("  x = vo * t + a * t^2 / 2")
print("  x = (vf + vo) / 2 * t")
print("  a = (vf - vo) / t")
print("  vf^2 = vo^2 + 2 * a * x")
print("")


def pedir_distancia(mensaje="distancia"):
    print(f"  unidad de {mensaje}:")
    print("    1 metros")
    print("    2 kilometros")
    unidad = input("  escoge unidad: ")
    valor = float(input(f"  {mensaje}: "))
    if unidad == "2":
        valor = valor * 1000
        print(f"  (convertido a {valor} metros)")
    return valor


def pedir_tiempo(mensaje="tiempo"):
    print(f"  unidad de {mensaje}:")
    print("    1 segundos")
    print("    2 minutos")
    print("    3 horas")
    unidad = input("  escoge unidad: ")
    valor = float(input(f"  {mensaje}: "))
    if unidad == "2":
        valor = valor * 60
        print(f"  (convertido a {valor} segundos)")
    elif unidad == "3":
        valor = valor * 3600
        print(f"  (convertido a {valor} segundos)")
    return valor


def pedir_velocidad(mensaje="velocidad"):
    print(f"  unidad de {mensaje}:")
    print("    1 m/s")
    print("    2 km/h")
    unidad = input("  escoge unidad: ")
    valor = float(input(f"  {mensaje}: "))
    if unidad == "2":
        valor = valor / 3.6
        print(f"  (convertido a {round(valor, 4)} m/s)")
    return valor


def pedir_aceleracion(mensaje="aceleracion"):
    valor = float(input(f"  {mensaje} en m/s2: "))
    return valor


print("QUE TIPO DE MOVIMIENTO RECTILINEO DESEAS UTILIZAR")
print("")
print("1 MRU")
print("2 MRUA")
print("")

opcion = input("que quieres calcular: ")

if opcion == "1":
    print("")
    print("ok escogiste MRU")
    print("")
    print("que quieres calcular:")
    print("1 distancia")
    print("2 velocidad")
    print("3 tiempo")
    print("")

    opcion2 = input("escoge una: ")
    print("")

    if opcion2 == "1":
        v = pedir_velocidad("velocidad")
        t = pedir_tiempo("tiempo")
        d = v * t
        print("")
        print("la distancia es", round(d, 4), "metros")

    elif opcion2 == "2":
        d = pedir_distancia("distancia")
        t = pedir_tiempo("tiempo")
        v = d / t
        print("")
        print("la velocidad es", round(v, 4), "m/s")

    elif opcion2 == "3":
        d = pedir_distancia("distancia")
        v = pedir_velocidad("velocidad")
        t = d / v
        print("")
        print("el tiempo es", round(t, 4), "segundos")

    else:
        print("eso no existe")

elif opcion == "2":
    print("")
    print("ok escogiste MRUA")
    print("")
    print("que formula quieres usar:")
    print("1 velocidad final      vf = vo + a * t")
    print("2 distancia            x = vo * t + a * t^2 / 2")
    print("3 distancia            x = (vf + vo) / 2 * t")
    print("4 aceleracion          a = (vf - vo) / t")
    print("5 velocidad final      vf^2 = vo^2 + 2 * a * x")
    print("")

    opcion2 = input("escoge una: ")
    print("")

    if opcion2 == "1":
        vo = pedir_velocidad("velocidad inicial")
        a = pedir_aceleracion("aceleracion")
        t = pedir_tiempo("tiempo")
        vf = vo + a * t
        print("")
        print("la velocidad final es", round(vf, 4), "m/s")

    elif opcion2 == "2":
        vo = pedir_velocidad("velocidad inicial")
        a = pedir_aceleracion("aceleracion")
        t = pedir_tiempo("tiempo")
        x = vo * t + (a * t ** 2) / 2
        print("")
        print("la distancia es", round(x, 4), "metros")

    elif opcion2 == "3":
        vf = pedir_velocidad("velocidad final")
        vo = pedir_velocidad("velocidad inicial")
        t = pedir_tiempo("tiempo")
        x = ((vf + vo) / 2) * t
        print("")
        print("la distancia es", round(x, 4), "metros")

    elif opcion2 == "4":
        vf = pedir_velocidad("velocidad final")
        vo = pedir_velocidad("velocidad inicial")
        t = pedir_tiempo("tiempo")
        a = (vf - vo) / t
        print("")
        print("la aceleracion es", round(a, 4), "m/s2")

    elif opcion2 == "5":
        vo = pedir_velocidad("velocidad inicial")
        a = pedir_aceleracion("aceleracion")
        x = pedir_distancia("distancia")
        vf = (vo ** 2 + 2 * a * x) ** 0.5
        print("")
        print("la velocidad final es", round(vf, 4), "m/s")

    else:
        print("eso no existe")

else:
    print("eso no existe")