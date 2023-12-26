# Pegar cada uma das listas
lista1 = input().split()
lista2 = input().split()

# Transformar a listas com tipo strings para números inteiros
for i in range(len(lista1)):
    lista1[i] = int(lista1[i])

for i in range(len(lista2)):
    lista2[i] = int(lista2[i])

# adicionar cada valor da lista 1 na lista 3
lista3 = []

# Adicionar cada valor lista1 na lista3
for numero in lista1:
    if numero not in lista3:
        lista3.append(numero)

# Adicionar cada valor lista2 na lista3
for numero in lista2:
    if numero not in lista3:
        lista3.append(numero)

print(lista3)