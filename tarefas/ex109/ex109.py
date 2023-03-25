import moeda

p = float(input("Digite o preço: R$"))
print(f"""A metade de {moeda.moeda(p)} é {moeda.metade(p, False)}.
O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.
Aumentando 10%, temos {moeda.aumentar(p, 10, True)}.
Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}.""")