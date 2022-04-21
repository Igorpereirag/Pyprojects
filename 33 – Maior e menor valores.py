a=int(input('Digite o primeiro número'))
b=int(input('Digite o segundo número'))
c=int(input('Digite o  terceiro número'))
menor = a
if b<a and b<c:
    menor = b
if  c<a and c<b:
    menor = c
print(f'o menor valor digitado foi {menor}')
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'o maior valor digitado foi {maior}')