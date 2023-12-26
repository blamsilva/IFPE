valor = float(input())
codigo = int(input())

match codigo:
    case 1:
        desconto = 0.30
    case 2:
        desconto = 0.20
    case 3:
        desconto = 0.10
    case 4:
        desconto = 0 
    case _:
        print("ERRO")
        exit() # função interna do Python que encerra o programa ao ser executada.
print(f"{codigo}x de R$ {(valor*(1-desconto)/codigo):.2f}")   
