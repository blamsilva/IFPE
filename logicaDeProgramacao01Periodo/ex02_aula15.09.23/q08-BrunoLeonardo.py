nota1 = float(input())
nota2 = float(input())
media = ((nota1 + nota2)/2)
if 0.0 <= media <= 3.0:
    print("Reprovado")
elif 3.0 < media <= 7.0:
    print("Exame")
elif 7.0 < media <= 10.0:
    print("Aprovado")
else:
    print("Média Inválida, Digite Notas de 0 a 10!")
