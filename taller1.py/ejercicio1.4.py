temperatura = float(input("Ingrese la temperatura actual en grados centígrados: "))

if temperatura >= 24:
    print("El clima es cálido")
else:
    if temperatura >= 17 and temperatura < 24:
        print("El clima es templado")
    else:
        if temperatura >= 12 and temperatura < 17:
            print("El clima es frío")
        else:
            temperatura < 12
            print("El valor actual de temperatura es inválido") 
        