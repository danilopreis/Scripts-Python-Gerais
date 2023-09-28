casa = float(input('Digite o valor do imóvel: '))
sal = float(input('Digite o seu salario atual: '))
ano = int(input('Em quantos anos você quer pagar o imovel? '))

pmen = ano*12
prest = casa/pmen
exd = sal + (sal * 0.30)

if prest < exd:
    print('Desculpe o emprestimo não pode ser liberado!')
else:
    print('Emprestimo liberado! Você irá pagar em {}x de {} por mês'.format(pmen, prest))
