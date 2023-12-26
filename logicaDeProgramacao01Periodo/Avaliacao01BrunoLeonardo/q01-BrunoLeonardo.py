n = 1
soma = 0
while n > 0:
    n = int(input())
    cont = 0 
    if n > 1:
        for divisores in range(1,n+1):
            if n % divisores == 0:
                cont += 1
        if cont == 2:
            soma += n
print(soma)
