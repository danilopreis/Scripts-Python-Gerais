nome = str(input('Digite seu nome completo: ')).strip()
pn = nome[:nome.find(' ')+1]
pu = nome[nome.rfind(' ')+1:]
print('Seu primeiro nome é: {}'.format(pn))
print('Seu ultimo nome é: {}'.format(pu))
