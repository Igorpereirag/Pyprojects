s=float(input('Digite seu salario'))
if s <= 1250:
    a = s+s*15/100
    print(f'Seu salario de R$ {s} com aumento de 15% é {a:.2f}')
else:
    a = s+s*10/100
    print(f'O seu salario de R$ {s} com aumento de 10% é {a:.2f} ')


