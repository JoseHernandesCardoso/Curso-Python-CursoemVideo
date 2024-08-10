def notas(*n, sit=False):
    """
    -→ Recebe e analisa diversas notas de vários alunos de uma turma
    :param n: notas da turma (pode receber várias)
    :param sit: habilita ou desabilita mostrar a situação da turma (PADRÃO = FALSE)
    :return: retorna um dicionário com o total de notas, a maior e menor nota, a média e a situação
    """
    turma = dict()
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['média'] = sum(n)/len(n)
    if sit:
        if turma['média'] < 5:
            turma['situação'] = 'PÉSSIMA'
        elif 5 <= turma['média'] < 6:
            turma['situação'] = 'RUIM'
        elif 6 <= turma['média'] < 7:
            turma['situação'] = 'RAZOÁVEL'
        elif 7 <= turma['média'] < 8.5:
            turma['situação'] = 'BOA'
        else:
            turma['situação'] = 'EXCELENTE'
    return turma


print(notas(7.5, 9.5, 9, 10, sit=True))
help(notas)
