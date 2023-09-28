import math

a = float(input('Digite um angulo: '))
sin = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O seno do angulo de {}º é: {:.2f}'.format(a, sin))
print('O coseno do angulo de {}º é: {:.2f}'.format(a, cos))
print('A tangente do angulo de {}º é: {:.2f}'.format(a, tan))
