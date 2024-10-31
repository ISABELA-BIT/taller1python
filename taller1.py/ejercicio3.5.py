lista = input("Ingrese una lista de caracteres: ")
elemento = input("Ingrese el carácter a buscar: ")

posiciones = []

for i in range(len(lista)):
    if lista[i] == elemento:
        posiciones.append(i)
if posiciones:
    print(f"El elemento buscado '{elemento}' fue encontrado en la posición {posiciones}")
else:
    print(f"El elemento buscado '{elemento}' no encontrado en la lista de caracteres ingresada")