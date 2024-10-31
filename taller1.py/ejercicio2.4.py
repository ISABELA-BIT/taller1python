import random
puntos_en_el_dado = 0
tiradas = 0 

print (input("Lanza el dado oprimiendo la tecla Enter"))
while puntos_en_el_dado != 6:
    puntos_en_el_dado = random.randint(1, 6) 
    tiradas = tiradas + 1

    if puntos_en_el_dado < 6:
        print(f"Tirada {tiradas} Resultado {puntos_en_el_dado}, lanza de nuevo el dado oprimiento la tecla Enter")
    elif puntos_en_el_dado == 6: 
        print(f"Tirada {tiradas}, resultado {puntos_en_el_dado}")
        
print(f"¡FELICIDADES. Obtuviste un 6 después de {tiradas} tiradas!")