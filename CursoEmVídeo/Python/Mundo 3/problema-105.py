def notas(*notas,sit=False):
    """
    notas(*notas,sit=False):"
    Função que analisa notas de alunos
    -> *notas : Recebe qualquer Float e adiciona 
    a um dicionário se obedecer alguma condição
    -> sit=False : Diz se deve mostrar a situação
    do aluno, cálculo feito usando média simples
    """
    conjunto = dict()
    conjunto['maior'] = max(notas)
    conjunto['menor'] = min(notas)
    conjunto['quant'] = len(notas)
    conjunto['media'] = sum(notas)/len(notas)
    if sit == True:
        if conjunto['media'] >= 7:
            conjunto['situa'] = 'APROVADO!'
        elif conjunto['media'] >= 5:
            conjunto['situa'] = 'RAZOÁVEL'
        else:
            conjunto['situa'] = 'REPROVADO' 
    return(conjunto)

print(notas(4.0,5.0,6.0,5.0,))
#Por Emerson Machado 17/04/2025