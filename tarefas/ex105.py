def notas(*num, stt=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita diversas notas)
    :param stt: Opcional, indica se a situação será ou não apresentada
    :return: Dicionário com várias informações sobre a situação da turma.
    """

    resultados = {'total': len(num),
                  'maior': max(num),
                  'menor': min(num),
                  'média': sum(num) / len(num)}
    if stt:
        if resultados['média'] >= 7:
            resultados['situação'] = 'BOA'
        elif resultados['média'] >= 5:
            resultados['situação'] = 'RAZOÁVEL'
        else:
            resultados['situação'] = 'RUIM'
    return resultados


resp = notas(5, 5, 5, stt=True)
print(resp)
