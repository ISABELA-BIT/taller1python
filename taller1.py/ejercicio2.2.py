ini = 2

lim = 50

while True:  
    ini <= lim
    print(ini)
    ini = ini + 2
    if ini > lim:
        break
    else: 
        if ini < 0:
            print("Es incorrecto")
            break
        