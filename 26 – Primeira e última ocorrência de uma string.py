nome= str(input('Digite seu nome')).upper().replace(' ','')

print(f'A Letra "a" aparece {nome.count("A")} vezes')
print(f'A primeira letra "a" se encontra na posição {nome.find("A")+1}')
print(f'A ultima letra "a" apareceu na posição {nome.rfind("A")+1}')





