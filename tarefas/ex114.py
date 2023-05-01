teste = int(input("""Qual teste você deseja fazer?
 O próprio feito por mim [1].
 Ou o feito pelo guanabara [2]?
 """))


if teste == 1:
    """
        meu metodo
    """
    import webbrowser

    try:
        site = input("Digite a URL do site: ")
        webbrowser.open_new_tab(site)
    except:
        print("Não foi possivel acessar o site")
    else:
        print(f'Consegui acessar o site {site}')

elif teste == 2:
    """
        Metodo Guanabara
    """

    from urllib import request

    try:
        sit = input("Digite a URL do site: ")
        request.urlopen('pudim.com.br')
    except Exception as erro:
        print(f'O site não está disponivel no momento, erro:{erro}')
    else:
        print(f'Consegui acessar o site {sit}')
