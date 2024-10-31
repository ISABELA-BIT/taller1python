palabra = input("Escriba una palabra: " )
vocales=("aeiouAEIOU")
contador= 0

i = 0

while i < len(palabra):
    
    if palabra[i] in vocales:
        contador = contador + 1 
    i = i + 1      

print("La palabra tiene ", contador, " vocales")

    
        
        
        
        