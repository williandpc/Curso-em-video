def cadastro(nome, idade):
    try:
        with open("registro.txt") as registro:
            pessoa = {nome: idade}
            registro.writelines(f"{pessoa} \n")
    except:
        print("Ocorreu um erro")
