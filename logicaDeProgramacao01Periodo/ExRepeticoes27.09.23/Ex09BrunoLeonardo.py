n1 = int(input())
n2 = int(input())

if n1 < n2:
    for numeros in range(n1, n2+1):
        if numeros % 3 == 0:
            print(numeros, end=" ") 
