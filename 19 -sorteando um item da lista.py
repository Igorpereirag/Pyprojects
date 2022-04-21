import random

n1=input('primeiro nome')
n2=input('segundo nome')
n3=input('terceiro nome')
n4=input('quarto nome')
alunos= [n1,n2,n3,n4]
sorteado= random.choice(alunos)
print(f' o aluno escolhido foi {sorteado}')