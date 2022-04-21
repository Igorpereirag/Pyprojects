c =float(input('Digite o valor da casa'))
s =float(input('Digite o valor do seu salario'))
a = int(input('Em quantos anos você deseja pagar?'))
p = (c / ( a * 12 ))
m = s * 30 / 100
print(f'para pagar uma casa no valor de R$ {c} em {a} anos')
print(f'A prestação será de R$ {p:.2f} ')
if p <= m:
    print('Emprestimo aprovado')
else:
    print('Emprestimo negado')