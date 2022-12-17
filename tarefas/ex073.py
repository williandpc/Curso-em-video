# -*- coding: iso-8859-15 -*-
CBF = (
    'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico - PR', 'Atlético - MG',
    'Fortaleza', 'São Paulo', 'América - MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
    'Ceará SC', 'Atlético - GO', 'Avaí', 'Juventude')

print('~~~~'*30)
print("Desafio 73:A\n"
      "Os 5 primeiros colocados")
print('Resposta:')
print(CBF[:5])
print('~~~~'*30)
print("Desafio 73:B\n"
      "Os 4 últimos colocados.")
print('Resposta:')
print(CBF[-4:])
print('~~~~'*30)
print("Desafio 73:C\n"
      "Lista em ordem alfabetica da tupla")
print('Resposta:')
print(sorted(CBF))
print('~~~~'*30)
print("Desafio 73:D\n"
      "Posição do Chapecoence")
print('Resposta:')
if 'Chapecoence' in CBF:
    print(f"O Chapecoence se encontra na {CBF.index('Chapecoence') + 1}ª posição")
else:
    print(f"O Chapecoence não está entre os 20 colocados. Mas meu time favorito, grande São Paulo está, e ele está"
          f"em {CBF.index('São Paulo') + 1}º lugar!!")



