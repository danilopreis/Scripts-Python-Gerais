nome = input('Digite seu nome completo: ')
n1 = nome.upper()
print('nome completo em maiusculo: ', n1)
n2 = nome.lower()
print('nome completo em minusculo: ', n2)
n3 = len(nome.strip())
print('quantidade de letras sem considerar espaços: ', n3-nome.count(' '))
n4 = nome.split()
print('Primeiro nome: ', len(n4[0]))
