import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co,ca)
print(f' A hipotenusa vai medir {hi:.2f}')

angulo = float(input('Digite o angulo que deseja: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'O angulo de {angulo} tem o seno de {seno:.2f}')
print(f'O angulo de {angulo} tem o cosseno de {cos:.2f}')
print(f'O angulo de {angulo} tem a tangente de {tan:.2f}')