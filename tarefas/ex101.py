from datetime import datetime


def voto(ano):
    idade = datetime.today().year - ano
    if idade < 18:
        print(f"Com {idade} anos: NÃO VOTA.")
    elif 18 < idade < 65:
        print(f"com {idade} anos: VOTO OBRIGATÓRIO.")
    elif idade >= 65:
        print(f"com {idade} anos: VOTO OPCIONAL.")


print("-"*30)
voto(int(input("Em que ano você nasceu? ")))
