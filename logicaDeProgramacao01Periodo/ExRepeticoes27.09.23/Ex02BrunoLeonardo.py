custoDeFabrica = float(input())
pd = 0
pi = 0
if 0 <= custoDeFabrica < 35000.00:
    pd = 0.05
    pi = 0
elif 35000.00 <= custoDeFabrica < 70000.00:
    pd = 0.1
    pi = 0.15
elif 70000.00 < custoDeFabrica:
    pd = 0.15
    pi = 0.20
print(f"R$ {custoDeFabrica*(1+pd+pi):.2f}")
