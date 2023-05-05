from funcs import *
from listar import *
from time import sleep
from cadastro import cadastro

abrirlist()

while True:
    escolha = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    linha()
    if escolha == 3:
        cabecalho("Saindo do sistema... Até logo!")
        break

    elif escolha == 2:
        cadastro(input("\033[33mNome: \033[m"), int(input("\033[33mIdade: \033[m")))

    elif escolha == 1:
        listar()

    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
