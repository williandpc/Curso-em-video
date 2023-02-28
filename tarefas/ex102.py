def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser faturado
    :param show: (Opcional) Mostrar (True) ou não mostar (False(padrão)) o calculo.
    :return: O valor do Fatorial de um número num.
    """
    f = 1
    if show:
        for c in range(num, 0, -1):
            f *= c
            if c != 1:
                print(c, end=' x ')
            else:
                print(c, end=f' = {f}')
        print()
    elif not show:
        for c in range(num, 0, -1):
            f *= c
        print(f)


fatorial(5)
