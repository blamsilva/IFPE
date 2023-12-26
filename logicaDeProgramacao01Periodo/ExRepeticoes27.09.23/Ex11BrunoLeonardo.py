while True:
    numero = int(input())
    cont = 0
    if numero > 1:
        for divisores in range(1,numero+1):
            if numero % divisores == 0:
                cont += 1
        
        if cont == 2:
            print("Sim")
        else:
            print("Não")
