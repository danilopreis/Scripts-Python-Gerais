import random

n = int(input('Digite um numero interio entre 0 e 5: '))
nc = random.randint(0, 5)
if n == nc:
    print('o computador pensou no numero {}.PARABÉNS!'.format(nc))
else:
    print('o computador pensou no numero {}.TENTE NOVAMENTE!'.format(nc))
