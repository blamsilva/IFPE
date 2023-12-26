n1 = int(input())
n2 = int(input())
n3 = int(input())
if n2 < n1 > n3 or n1 == n2 and n1 > n3 or n1 == n3 and n1 > n2 or n3 == n1 == n2:
    maior = n1
elif n1 < n2 > n3 or n2 > n1 and n2 == n3:
    maior = n2
else:
    maior = n3
    print(f"{maior} é o maior")
