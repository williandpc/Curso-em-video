# -*- coding: iso-8859-15 -*-
CBF = (
    'Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico - PR', 'Atl�tico - MG',
    'Fortaleza', 'S�o Paulo', 'Am�rica - MG', 'Botafogo', 'Santos', 'Goi�s', 'Bragantino', 'Coritiba', 'Cuiab�',
    'Cear� SC', 'Atl�tico - GO', 'Ava�', 'Juventude')

print('~~~~'*30)
print("Desafio 73:A\n"
      "Os 5 primeiros colocados")
print('Resposta:')
print(CBF[:5])
print('~~~~'*30)
print("Desafio 73:B\n"
      "Os 4 �ltimos colocados.")
print('Resposta:')
print(CBF[-4:])
print('~~~~'*30)
print("Desafio 73:C\n"
      "Lista em ordem alfabetica da tupla")
print('Resposta:')
print(sorted(CBF))
print('~~~~'*30)
print("Desafio 73:D\n"
      "Posi��o do Chapecoence")
print('Resposta:')
if 'Chapecoence' in CBF:
    print(f"O Chapecoence se encontra na {CBF.index('Chapecoence') + 1}� posi��o")
else:
    print(f"O Chapecoence n�o est� entre os 20 colocados. Mas meu time favorito, grande S�o Paulo est�, e ele est�"
          f"em {CBF.index('S�o Paulo') + 1}� lugar!!")



