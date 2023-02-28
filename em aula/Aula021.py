## utilizar o comando help() no console do pycharm
# ou entao help(*comando a pesquisar*) e startar o programa
# que ira aparecer uma lista de ajuda
#print(*comando a pesquisar*.__doc__) mesma questao do help de uma forma diferente

#PARA FAZER UM MANUAL DA FUNÇÃO QUE VOCE GEROU, ABRIR 3 ASPAS DUPLAS APOS EMBAIXO DO DEF
#EXEMPLO EX 96:

def area(l, h):
    """
    Funçaõ para calcular a area de um espaço retangular e mostrar na tela
    :param l: Inserir a largura do espaço
    :param h: Inserir o comprimento do espaço
    :return:sem retorno
    """
    a = l * h
    print(f'A área de um terreno de {h} x {l} é de {a}m²')


area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (M):')))

help(area)