# inicio de codigo para cor \033[**:**:**m, sendo os ** numeros para estilo, cor e fund (pode colocar em qualquer
# ordem pois cada numeração tem uma caracteristica especifica, por exemplo para estilo só tem 0,1,4 e 7 onde o 0 é
# sem estilo nenhum, o 1 deixa o texto em negrito, o 4 vai sublinhar e o 7 vai trocar as cores do fundo com as cores
# da letra para mudar a cor das letras são outros numeros especificos por isso a ordem nao importa para numero temos:
# 30 = branco
# 31 = vermelho
# 32 = verde
# 33 = amarelo
# 34 = azul
# 35 = roxo
# 36 = ciano
# 37 = cinza
# para fundo a ordem de cores segue igual so que ao inves de 30 a 37 o fundo recebe de 40 a 47
# sendo o 40 branco e o 47, o ultimo, cinza
# por padrão o fundo é preto, o texto é cinza e o estilo é nao existe
print('\033[0:30:41mteste')
print('\033[30:41mteste') # sem o codigo para estilo o python colocou o padrão
print('\033[0;30;40mteste') # coloquei a letra em branco e inverti a cor da letra com a do fundo
# (fundo nao identificado que por padrão do sistema é preto)