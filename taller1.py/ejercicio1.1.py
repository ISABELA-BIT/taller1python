primeras_letras = str('abcdefghijklm')
ultimas_letras = str('nñopqrstuvwxyz')

letra = str(input("Ingrese una letra: "))


if letra in primeras_letras:
    print("La letra ingresada está entre las primeras letras del abecedario")
else:
    if letra in ultimas_letras:
        print("La letra ingresada está entre las últimas letras del abecedario")   
    else:
        print("ERROR: el caracter ingresado no está incluido")
        