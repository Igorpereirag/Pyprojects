n=int(input('digite um numero'))
u= n//1 % 10
d= n//10 % 10
c= n//100 % 10
m= n//1000 % 10
print('analisando o numero:',n)
print(f'a unidade é:{u}')
print(f'a dezena é:{d}')
print(f'a centena é:{c}')
print(f'a unidade de milhar é:{m}')