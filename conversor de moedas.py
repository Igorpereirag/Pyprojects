#print
import  urllib
import  re
#d= dolar.py
d=float(input('Quanto de dinheiro você tem na carteira R$?'))
print('Com R${:.2f} você pode comprar US${:.2f}'.format(d,d/5.28))