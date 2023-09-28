km = int(input('Digite quantos km você irá viajar: '))
if km <= 200:
    print('O valor da sua viagem é: R${}'.format(km*0.50))
else:
    print('O valor da sua viagem é: R${}'.format(km*0.45))
