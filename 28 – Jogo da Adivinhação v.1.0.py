from random import randint
from time import sleep
c= randint(1,5)
print('Olá, quero que voce adivinhe em qual numero eu pensei de (1-5)')
u=int(input('Qual o número que eu pensei?'))
print('processando.....')
sleep(3)
if c == u:
    print(f'parabens voce acertou, eu pensei no numero {c}')
else:
    print(f'você errou, eu pensei no número {c} e não no {u}')