cuadros = 8

for i in range(cuadros):
    for j in range(cuadros):
        if (i + j) % 2 == 0:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()