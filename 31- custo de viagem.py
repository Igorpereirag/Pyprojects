k=float(input('Digite a distancia da sua viagem em km'))
if k <=200:
  p = k * 0.50
  print(f'o valor de sua pasaagem é  R$ {p:.2f}')
else:
    d = k * 0.45
    print(f' O valor de sua passagem com desconto é R$ {d:.2f}')
