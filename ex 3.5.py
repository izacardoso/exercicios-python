n = int(input('digite um numero'))
print(f'o numero antecessor de {n} é {n-1}, e o sucessor é {n+1} ')

n = int(input('Digite outro numero'))
print(f'o dobro de {n} é {n*2}, o tripo é {n*3}, e sua raiz quadrada é {n**2}')

n1 = int(input('Digite sua primeira nota: '))
n2 = int(input('Digite sua segunda nota: '))
s = n1+n2
print(f'A sua média é {s/2}')


print('Bem vindo ao convertor de medidas')
n = float(input('Digite um valor em metros: '))
print(f'{n} Metros equivale a:')
print(f'{n*100} Centrimetros e a {n*1000} Milimetros')

print('Quantos dolares voce pode comprar?')
n = float(input('Quanto dinheiro em real voce tem?'))
print(f'Com {n} voce consegue comprar {n/5.25:f} Dolares')
