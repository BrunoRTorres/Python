def notas(* notas, sit=False):
    """_summary_
    
        Funcao que mostra notas de uma turma, sua maior e menor nota,
        sua media e situacao (opcional)

    Parameters
    ----------
    sit : bool, optional
        _description_, by default False
    
        Mostra a situacao da turma

    Returns
    -------
    _type_
        _description_

        Retorna um dicionario com os dados da turma
        
    """
    turma = {'total': len(notas),
             'maior': max(notas),
             'menor': min(notas),
             'media': sum(notas) / len(notas)}

    if sit:
        if turma['media'] >= 9:
            turma['situacao'] = 'EXCELENTE'
        elif turma['media'] >= 8:
            turma['situacao'] = 'BOA'
        elif turma['media'] >= 6:
            turma['situacao'] = 'MEDIANA'
        else:
            turma['situacao'] = 'RUIM'

    return turma


print(notas(8, sit=True))