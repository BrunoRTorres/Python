def fatorial(num=1, show=False):
    """_summary_
    Calcula o fatorial de um numero.

    Parameters
    ----------
    num : int, optional
        _description_, by default 1
        O numero a ser colocado.

    show : bool, optional
        _description_, by default False
        Mostrar ou nao a conta.

    Returns
    -------
    _type_
        _description_
        O valor do fatorial de um numero num.

    """
    if show == False:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f
    elif show == True:
        for n in range(num, 0, -1):
            if n == 1:
                print(n, end=' = ')
            else:
                print(n, end=' x ')
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f

valor = int(input('Digite um valor: '))
print(f'O fatorial de {valor}: ', end='')
print(fatorial(valor, show=True))
help(fatorial)
