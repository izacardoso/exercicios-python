nome = str(input('Digite seu nome completo: ')).strip()
separado = nome.split()
print(f'Seu primeiro nome é {separado[0]}')
print(f'Seu ultimo nome é {separado[-1]}')