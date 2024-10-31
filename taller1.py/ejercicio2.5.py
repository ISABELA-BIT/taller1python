numero = input("Ingrese un numero: ")

suma = 0
i = 0

while i < len(numero):
    suma = suma + int(numero[i])
    i = i + 1
print(f"La suma de los dígitos del número es: {suma}")
