supermercados = int(input())
menor_valor = 1000000
for i in range(0,supermercados):
    pbits, gramas = input().split()
    pbits = float(pbits)
    gramas = float(gramas)
    valor_por_grama = pbits/gramas
    if valor_por_grama < menor_valor:
        menor_valor = valor_por_grama
print(f"{menor_valor*1000:.2f}")
3