jogadas = input().split()
jogadas2 = []
for i in range(0,len(jogadas)):
    jogadas2.append(int(jogadas[i]))
for n in range(1,7):
    print(f"Número {n} saiu {jogadas2.count(n)} vezes.")
