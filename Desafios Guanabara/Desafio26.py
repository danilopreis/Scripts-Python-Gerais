nome = input('Digite uma frase: ')
qa = nome.upper().count('A')
p1 = nome.upper().rfind('A')
p2 = nome.upper().find('A')
print('Quantas letra A possuem dentro da frase? ', qa)
print('Qual a posição da primeira letra A? ', p2)
print('Qual a posição da ultima letra A?', p1)
