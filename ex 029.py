km = int(input('Qual foi a velocidade do seu carro?: '))
if km >=80:
    multa = (km-80)*7
    print('Você ultrapassou o limite de 80km/h. Você será multado.')
    print(f'O valor da sua multa é de {multa}')
else:
    print('Sua velocidade está dentro do limite. PARABÉNS.')