cadenaIngresada = input("Ingrese una cadena: ")
cadenaInvertida = ""

for i in range(len(cadenaIngresada) - 1, -1, -1):
    cadenaInvertida = cadenaInvertida + cadenaIngresada[i]
print("La cadena invertida es:", cadenaInvertida)