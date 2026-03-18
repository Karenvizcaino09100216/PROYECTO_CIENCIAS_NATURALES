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


print("bienvenido al resolvedor de MRU")
print("que quieres calcular?")
print("1. distancia")
print("2. velocidad")
print("3. tiempo")

opcion = input("escribe 1, 2 o 3: ")

if opcion == "1":
    print("vamos a calcular la distancia")
    velocidad = float(input("escribe la velocidad en m/s: "))
    tiempo = float(input("escribe el tiempo en segundos: "))
    distancia = velocidad * tiempo
    print("la distancia es:", distancia, "metros")

elif opcion == "2":
    print("vamos a calcular la velocidad")
    distancia = float(input("escribe la distancia en metros: "))
    tiempo = float(input("escribe el tiempo en segundos: "))
    velocidad = distancia / tiempo
    print("la velocidad es:", velocidad, "m/s")

elif opcion == "3":
    print("vamos a calcular el tiempo")
    distancia = float(input("escribe la distancia en metros: "))
    velocidad = float(input("escribe la velocidad en m/s: "))
    tiempo = distancia / velocidad
    print("el tiempo es:", tiempo, "segundos")

else:
    print("eso no es una opcion valida")