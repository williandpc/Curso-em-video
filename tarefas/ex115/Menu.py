from funcs import *
from time import sleep

while True:
    escolha = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    linha()
    if escolha == 3:
        cabecalho("Saindo do sistema... Até logo!")
        break
    elif escolha == 2:
        cabecalho("opção 2")
    elif escolha == 1:
        cabecalho("opção 1")
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
