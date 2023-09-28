sal = float(input('Digite seu salario atual: '))
sal10 = sal + (sal*0.10)
sal15 = sal + (sal*0.15)
if sal > 1250:
    print('Seu salario sofreu um reajuste de 10%: R$', sal10)
else:
    print('Seu salario sofreu um reajuste de 15%: R$', sal15)
