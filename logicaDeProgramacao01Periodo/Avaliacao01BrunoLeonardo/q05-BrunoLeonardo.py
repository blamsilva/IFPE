idade = int(input())
if idade - 1 == 0:
    print("21")
elif idade - 2 == 0:
    print("42")
elif idade - 3 == 0:
    print("47")
elif idade - 4 == 0:
    print("52")
elif idade - 5 == 0:
    print("55")
elif idade - 6 == 0:
    print("58")
elif idade - 7 == 0:
    print("61")
else:
    resto = idade - 7
    idadeCachorroParaHumano = (resto*2) + 61 
    print(idadeCachorroParaHumano)
