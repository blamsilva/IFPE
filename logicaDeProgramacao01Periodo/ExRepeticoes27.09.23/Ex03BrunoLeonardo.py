codigo = int(input())
quantidade = float(input())

match codigo:
    case 1:
        if quantidade <= 5:
            preco = 7.00
        else:
            preco = 5.80
        
    case 2:
        if quantidade <= 5:
             preco = 11.80
        else:
            preco = 8.50 
    
    case 3:
        if quantidade <= 5:
             preco = 2.25
        else:
            preco = 1.70

    case 4:
        if quantidade <= 5:
             preco = 5.50
        else:
            preco = 4.00

    case 5:
        if quantidade <= 5:
             preco = 6.90
        else:
            preco = 5.60

    case 6:
        if quantidade <= 5:
             preco = 4.50
        else:
            preco = 2.40      
    
    case _:
        print("Opção Inválida")
print(f"R$ {preco*quantidade:.2f}")
