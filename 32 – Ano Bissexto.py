from datetime import date
ano=int(input('Digite um ano para analisar ou digite 0 para analisar o ano atual'))
if ano == 0:
    ano=date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print(f' O ano {ano} é bissexto, formado por aproximadamente,366 dias. ')
else:
    print(f'o ano {ano} não é bissexto, formado por aproximadamente,365 dias e 6 horas.')


