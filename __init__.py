"""import random

parent = [-1, 0, 1, 2]
parent2 = parent[:]
print(parent)
amp = int(len(parent) / 2)
dicionario = {}
for c in range(amp):
    valor = random.choice(parent2)
    dicionario[f"Dados {c + 1}"] = valor
    del parent2[parent2.index(valor)]
print(parent2)
print(dicionario)
for v, i in enumerate(parent):

"""