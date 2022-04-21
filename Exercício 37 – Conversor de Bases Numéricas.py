n= int(input('Digite um número inteiro'))
print('''Escolha uma das bases para conversão
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')
op1=int(input('Digite uma opção'))
if op1==1:
    print(f'O numero {n} convertido para binário é {bin(n)[2:]}')
elif op1==2:
    print(f'O numero {n} cobertido para octal é {oct(n)[2:]}')
elif op1==3:
    print(f'o numero {n} convertido para hexadecimal é {hex(n)[2:]}')
else:
    print('opção invalida digite novamente')

