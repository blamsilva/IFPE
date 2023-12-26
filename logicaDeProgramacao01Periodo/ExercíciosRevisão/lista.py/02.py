#Receber gabarito
gabarito = input().upper().split()

#Receber cada resposta de cada aluno em uma lista
qntd_alunos = int(input())
alunos = []
for i in range(qntd_alunos):
    estudante = input().upper().split()
    alunos.append(estudante)
print(alunos)
# Comparar Gabarito com resposta dos alunos
acerto_cada_alunos = []
aprovacao = 0
for aluno in alunos:
    acertos = 0
    for i in range(len(aluno)):
    #se estiver certo, adicionar em um contador
        if aluno[i] == gabarito[i]:
            acertos += 1
    acerto_cada_alunos.append(acertos)
    #calcular porcentagem de aprovação
    if acertos >=6:
        aprovacao = 1/len(alunos)
for i in range(len(acerto_cada_alunos)):
    print(f"Aluno #{i} `{acerto_cada_alunos[i]:.1f}")
print(f"Aprovação: {aprovacao*100:.0f}%")

