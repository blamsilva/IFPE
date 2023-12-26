
def imparesentre(inicio, fim):
    soma = 0
    for impares in range(inicio,fim+1):
        if impares % 2 != 0:
            soma += impares
    return soma
print((imparesentre(inicio=int(input()),fim=int(input()))))
