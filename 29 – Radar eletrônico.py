v=int(input('Qual a velocidade atual do seu carro?'))
multa= (v-80) * 7
if v > 80:
    print(f'''MULTADO! VOCÊ ULTRAPASSOU O LIMITE MÁXIMO PERMITIDO QUE É DE 80KM/H
                     Sua multa foi de {multa} R$''')
else:
    print('PARABENS,você está dentro da velocidade permitida!')