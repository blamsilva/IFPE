n1 = int(input())
n2 = int(input())
n3 = input()
if n3 in ("1", "2", "3"):
    if n3 == "1":
        print(f"{n1**n2:.1f}")
    elif n3 == "2":
        print(f"{(n1**2)+(n2**2):.1f}")
    else:
        print(f"{((n1**(1/2))+((n2**(1/2)))):.1f}")
else:
    print("ERRO")
