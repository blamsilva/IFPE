numeros = input().split()
for i in range(len(numeros)):
    numeros[i] = int(numeros[i])

inicio = 0
fim = 6
matriz = []
for linha in range(3):
    linha = []
    for coluna in range(inicio, fim):
        linha.append(numeros[coluna])
    matriz.append(linha)
    inicio += 6
    fim += 6
for linha in range(0,3):
    print(matriz[linha])
