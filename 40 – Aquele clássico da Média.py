n1=int(input("Digite a primeira nota"))
n2=int(input("Digite a segunda nota"))
m= (n1+n2)/2
if m < 5:
    print("VOCE FOI REPROVADO")
elif 5 >= m <= 6.9:
    print("vocE está na recuperação")
elif m > 7:
    print("voce foi aprovado!!")