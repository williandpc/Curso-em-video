##Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Por quantos dias ele foi usado?:'))
km = float(input('Quantos km foi rodado?:'))
tkm = km * 0.15
td = d * 60

print(f'O total por km rodado deu R${tkm} e o total por dia deu R${td}. \n'
      f'O total à pagar pelo aluguel é de R${tkm + td}.')