def voto(ano):
    from datetime import datetime
    idade = datetime.today().year - ano
    if idade < 16:
        print(f"Com {idade} anos: NÃO VOTA.")
    elif 16 < idade < 65:
        print(f"com {idade} anos: VOTO OBRIGATÓRIO.")
    elif idade >= 65 or 16 <= idade < 18:
        print(f"com {idade} anos: VOTO OPCIONAL.")


print("-"*30)
voto(int(input("Em que ano você nasceu? ")))
