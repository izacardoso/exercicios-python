import random
n1 = int(input('O computador escolheu um número de 0 a 5. Você é capaz de adivinhar?: '))
sorteio = random.randint(0,5)
if n1 == sorteio:
    print('Parabéns, você acertou!')
else:
    print('Você errou. Tente novamente.')

