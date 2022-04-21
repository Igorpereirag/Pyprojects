nome=str(input('Digite  seu nome completo')).strip()
n= nome.split()
print(f'seu primeiro nome é {n[0]} e seu ultimo é {n[len(n)-1]}')
print(n)