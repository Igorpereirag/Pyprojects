n1=int(input('digite um numero'))
n2=int(input('digite outro numero'))
s= n1+n2
sub= n1-n2
div=n1/n2
m=n1*n2
ex=n1**n2
divi=n1//n2
rest=n1%n2
#print(' a soma é: {} \n a diferença é {} \n a divisão é {:.3f}\n o produto é:{}\n a exponenciação é {}\n a divisão inteira é {}\n o resto é {}'.format(s,sub,div,m,ex,divi,rest))
print(f''' a soma é: {n1+n2} 
a diferença é {sub} 
a divisão é {div:.3f}
o produto é:{m}
a exponenciação é {ex}
a divisão inteira é {divi} 
o resto é {rest}''')

