from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
escolha = (n1, n2, n3, n4)
print(f'O aluno escolhido foi: {choice(escolha)}')

n5 = int(input('Escolha um número: '))
n6 = int(input('Escolha outro número: '))
x = (n5, n6)
print(f'O número sortado foi: {choice(x)}')