from funcs import *
from listar import *
from time import sleep

abrirlist()

while True:
    escolha = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    linha()
    if escolha == 3:
        cabecalho("Saindo do sistema... Até logo!")
        break
    elif escolha == 2:
        cabecalho("opção 2")
    elif escolha == 1:
        listar()
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
,