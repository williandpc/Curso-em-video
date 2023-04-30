def metade(n, f=False):
    r = n / 2
    if f:
        r = f"R${r:.2f}"
        r = str(r)
        r = r.replace(".", ",")
    return r


def dobro(n, f=False):
    r = n * 2
    if f:
        r = f"R${r:.2f}"
        r = str(r)
        r = r.replace(".", ",")
    return r


def aumentar(n, c, f=False):
    r = n * (1 + c / 100)
    if f:
        r = f"R${r:.2f}"
        r = str(r)
        r = r.replace(".", ",")
    return r


def diminuir(n, c, f=False):
    r = n * (1 - c / 100)
    if f:
        r = f"R${r:.2f}"
        r = str(r)
        r = r.replace(".", ",")
    return r


def moeda(n):
    r = f"R${n:.2f}"
    r = str(r)
    return r.replace(".", ",")


def resumo(v, a = 10, d = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    dicionario = {"Preço analisado:": moeda(v),
                  "Dobro do preço:": dobro(v, True),
                  "Metade do preço:": metade(v, True),
                  f"{a}% de aumento:": aumentar(v, a, True),
                  f"{d}% de redução:": diminuir(v, d, True)}
    for v, k in dicionario.items():
        print(f"{v:<20}", end='')
        print(f"{k}")
