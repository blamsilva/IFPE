resultadoSomas = []
cont = 0
while True:
    m, n = input().split()
    m = int(m)
    n = int(n)
    if m > n:
        break
    else:
        cont +=1
        soma = 0
        for i in range(m,n+1):
            soma += i
    resultadoSomas.append(soma)
for n in range(0,cont):
    print(resultadoSomas[n], end=" ")
