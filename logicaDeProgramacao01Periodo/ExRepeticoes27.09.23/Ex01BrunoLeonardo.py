saldoMedio = float(input())
if saldoMedio > 400.00:
    print(f"R$ {(saldoMedio*.3):.2f}")
elif 400.00 <= saldoMedio >= 300.00:
    print(f"R$ {(saldoMedio*.25):.2f}")
elif 300.00 <= saldoMedio >= 200.00:
    print(f"R$ {(saldoMedio*.20):.2f}")
else:
    print(f"R$ {(saldoMedio*.10):.2f}")
