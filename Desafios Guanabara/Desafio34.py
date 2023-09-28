r1 = int(input('Digite a Reta 1: '))
r2 = int(input('Digite a Reta 2: '))
r3 = int(input('Digite a Reta 3: '))

reg1 = (r2 - r3)< r1 < r2 + r3
reg2 = (r1 - r3)< r2 < r1 + r3
reg3 = (r1 - r2)< r3 < r1 + r2

if reg1 and reg2 and reg3 == True:
    print('É possivel forma um triangulo com as retas fornecidas')
else:
    print('Não é possivel formar um triangulo com as retas fornecidas')
