salario = int(input('Insira o Salário: '))
if salario <= 1250:
    print('O aumento vai ser de: {:.2f} Aumentou em 15%'.format(salario*1.15))
else: print('O aumento vai ser de: {:.2f} Aumentou em 10%'.format(salario*1.10))