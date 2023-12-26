ddd = int(input())
capital = "naodefinida"
match ddd:
    case 82:
        capital = "Maceió"
    case 71:
        capital = "Salvador"
    case 88:
        capital = "Fortaleza"
    case 98:
        capital = "São Luís"
    case 83:
        capital = "João Pessoa"
    case 81:
        capital = "Recife"
    case 86:
        capital = "Teresina"
    case 84:
        capital = "Natal"
    case 79:
        capital = "Aracaju"
    case _:
        capital = "DDD INEXISTENTE"
print(capital)
