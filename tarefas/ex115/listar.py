def listar():
    with open("registro.txt", "r+") as registro:
            tabela = registro.read()
            if tabela == '':
                return print("Arquivo vazio, cadastre uma nova pessoa")
            else:
                return print(tabela)

