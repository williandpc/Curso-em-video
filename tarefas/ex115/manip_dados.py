from funcs import *


def cadastro(nome=str, idade=int):
    try:
        with open("registro.txt", 'a') as registro:
            registro.writelines(f"{nome.title()}; {idade}\n")
    except:
        print("Ocorreu um erro")
    else:
        print(f'Novo registro de {nome.title()} adicionado')


def abrirlist():
    try:
        with open('registro.txt', 'r+') as registro:
            print('Registro encontrado e aberto com sucesso!')
            return registro
    except FileNotFoundError:
        with open('registro.txt', 'w+') as registro:
            print('Registro, não encontrado! Gerando um novo registro...')
            sleep(1)
            print("Registro gerado com sucesso!")
            return registro


def listar():
    with open("registro.txt", "r") as registro:
        tabela = registro.readlines()
        if tabela == '':
            return print("Arquivo vazio, cadastre uma nova pessoa")
        else:
            for pessoa in tabela:
                nome = pessoa.split(';')[0]
                idade = pessoa.split(';')[1].replace('\n', '')
                print(f"{nome:<33} {idade} anos")
