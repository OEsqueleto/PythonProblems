produto = float(input('\033[0;37mQual o valor do Produto? '))
pagamento = str(input('Qual será o método de pagamento? ')).strip().lower()

if pagamento in ['cheque','dinheiro']:
    print('\033[1;32m10% DESCONTO! O produto vai custar: {:.2f}'.format(produto*0.9))
elif pagamento == 'cartão':
    print('\033[1;32m5% DESCONTO! O produto vai custar: {:.2f}'.format(produto*0.95))
elif pagamento == '2x cartão':
    print('\033[1;32mSEM JUROS! O produto vai custar: {:.2f}'.format(produto))
elif pagamento == '3x cartão':
    print('\033[1;32mCom 20% de juros O produto vai custar: {:.2f}'.format(produto*1.20))
else:
    print('\033[1;31mFORMA DE PAGAMENTO INVÁLIDA!')