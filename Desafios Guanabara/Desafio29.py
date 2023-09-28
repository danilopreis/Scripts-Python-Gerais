kmh = int(input('Digite sua velocidade atual: '))
if kmh > 80:
    print('Você ultrapassou o limite de velocidade! Sua multa é de: R${}'.format((kmh - 80)*7))
else:
    print('Muito bem! Não ultrapasse 80km/h')
