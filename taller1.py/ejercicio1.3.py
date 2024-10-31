nota = float(input("Ingrese el valor de la nota: "))

if nota >= 0 and nota < 3:
    print("El rendimiento del estudiante es insuficiente")
else:
    if nota >= 3 and nota < 3.5:
        print("El rendimiento del estudiante es regular")
    else:
        if nota >= 3.5 and nota < 4.5:
            print("El rendimiento del estudiante es bueno")
        else:
            if nota >= 4.5 and  nota <=5:
                print("El rendimiento del estudiante es excelente")
            else:
                nota > 5
                print("Nota no válida")