import math

a = float(input('Digite o comprimento do cateto: '))
b = float(input('Digite o comprimento do adjacente: '))
hip = math.hypot(a, b)
print('A hipotenusa das cordenadas {} e {} é: {:.3f}'.format(a, b, hip))
