nome = input('Digite seu nome completo: ')
s = nome.upper().split().count('SILVA')
if s == 1:
    print('O nome digitado TEM SILVA')
else:
    print('O nome digitado NAO tem SILVA')
