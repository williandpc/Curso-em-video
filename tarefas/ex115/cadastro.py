def cadastro(nome, idade):
    try:
        registro = open('registro.txt', 'w+')
        registro.writelines(nome)
        registro.writelines(str(idade))
    except:
        print("Ocorreu um erro")









cadastro.cadastro(input("\033[33mNome: \033[m"), int(input("\033[33mIdade: \033[m")))