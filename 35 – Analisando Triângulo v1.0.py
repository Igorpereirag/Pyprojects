r1=float(input('Digite um segmento'))
r2=float(input('Digite um segmento'))
r3= float(input('Digite um segmento'))
if r1 < r2+r3 and r2 < r1+r2 and r3 < r1+ r2:
    print('esses segmentos podem forma um triangulo')
else:
    print('esses segmentos não podem forma um triangulo')
