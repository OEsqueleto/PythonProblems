casa = float(input('\033[1;37mQual o valor da casa? '))
anos = float(input('\033[1;37mQuer pagar em quantos anos? '))
sala = float(input('\033[1;37mQual seu salario todo mês? '))

mensalidade = (casa/anos)/12

if mensalidade <= sala*0.3:
    print('\033[1;32mEmpréstimo permitido! A mensalidade será de: {:.2f}'.format(mensalidade))
else:
    print('\033[1;31mNEGADO! A mensalidade {:.2f} seria maior que 30% do seu salário: {:.2f}!'.format(mensalidade,sala))
 