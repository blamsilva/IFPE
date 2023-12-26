n = int(input())
soma = 0 
for divisores in range(1,n+1):
    if n % divisores == 0:
        soma += 1
print(soma)
print(type(soma))