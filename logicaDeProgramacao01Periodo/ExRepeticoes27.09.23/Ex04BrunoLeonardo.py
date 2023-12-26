a1 = int(input())
a2 = int(input())
a3 = int(input())

if (a1 + a2 + a3) == 180:
    if a1==90 or a2 == 90 or a3 == 90:
       print("Retângulo")
    elif a1 > 90 or a2 > 90 or a3 > 90:
        print("Obtusângulo")
    else:
        print("Acutângulo")
    