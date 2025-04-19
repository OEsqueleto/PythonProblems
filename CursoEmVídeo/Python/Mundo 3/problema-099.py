def maximo(*nums):
    if not nums:
        print('Nenhum argumento foi informado! O valor retornado é 0')
        nums = (0,)
    print(f'\nAnalisando os números:' ,", ".join(str(n) for n in nums))
    maioral = max(nums)
    quantia = len(nums)
    print(f'Dos {quantia} Números, o Maior é o {maioral}!')

maximo(2,9,4,5,7,1)
maximo(4,7,0)
maximo(1,2)
maximo(6)
maximo()

#Por Emerson Machado 16/04/2025