
angulo = float(input("Ingresa el valor de un ángulo en grados:"))

if angulo > 0 and angulo < 90:
    print("El angulo se encuentra en el cuadrante I")

else: 
    if angulo > 90 and angulo < 180:
        print("El angulo se encuentra en el cuadrante II")
    else:
        if angulo > 180 and angulo < 270:
            print("El angulo se encuentra en el cuadrante III")
        else:
            if angulo > 270 and angulo < 360:
                print("El angulo se encuentra en el cuadrante II")
            else:
                print("El valor ingresado no es un ángulo válido")