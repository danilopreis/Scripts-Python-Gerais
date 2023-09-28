num = int(input('Digite um numero interio: '))
esc = int(input('''Escolha umas das opções para a conversão:
                   1-Binario:
                   2-Octal:
                   3-hexadecimal:
                   --> '''))
if esc == 1:
    print('O valor {} em Binario é: {}'.format(num, bin(num)))
elif esc == 2:
    print('O valor {} em octal é: {}'.format(num, oct(num)))
elif esc == 3:
    print('O valor {} em Hexadecimal é: {}'.format(num, hex(num)))
else:
    print('Escolha incorreta! Digite o numero correspondente para a sua opção!')
