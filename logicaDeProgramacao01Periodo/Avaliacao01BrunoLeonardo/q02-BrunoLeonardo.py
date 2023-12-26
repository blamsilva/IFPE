soma  = 0
for participantes in range(0,6):
    resultado = str(input()).upper()
    if resultado == "V":
        soma += 1
if 5 == soma or soma == 6:
    print(int(1))
elif 3 == soma or soma == 4:
    print(int(2))
elif 1 == soma or soma == 2:
    print(int(3))
else:
    print("-1")
