soma = 0
nota = 0
contador = 0
while nota >= 0:
    contador += 1
    soma += nota
    nota = float(input())
    
media = (soma/(contador-1))
print(f"{media:.2f}")
