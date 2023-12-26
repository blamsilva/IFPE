pessoas_pesquisadas = int(input())
media_salararial = 0
media_filhos = 0
maior_salario = 0
percentual = 0
soma_filhos = 0
soma_salario = 0
pessoas_salario_inferior = 0
for i in range(0,pessoas_pesquisadas):
    salario, filhos = input().split()
    salario = float(salario)
    filhos = int(filhos)
    soma_filhos += filhos
    soma_salario += salario
    if salario > maior_salario:
        maior_salario = salario    
    if salario < 1212.00:
        pessoas_salario_inferior += 1
print(f"MÉDIA SALARIAL = R$ {soma_salario/pessoas_pesquisadas:.2F}")
print(f"MÉDIA FILHOS = {soma_filhos/pessoas_pesquisadas:.1f}")
print(f"MAIOR SALÁRIO = R$ {maior_salario:.2f}")
print(f"PERCENTUAL = {(pessoas_salario_inferior/pessoas_pesquisadas)*100:.0f}%")
