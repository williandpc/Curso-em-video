"""DICIONARIOS
declarados por {} (chaves)
ou entao declarados por dict()
exemplo:
dicionario = {}
dicionario = dict()
Não precisa de comeando para adicionar um novo item ao dicionario, somente executar
exemplo: adicionar uma coluna para definição de sexo
dados['sexo'] = 'M'
para remover o elemento temos somente o del
exemplo, quero remover os dados idade
del dados['idade']
"""
dicionario ={'nome':'Pedro',
             'idade': 25}
print(dicionario.keys()) # mostra os topicos
print(dicionario.values()) # mostra os valores adicionados atrelados as chaves
print(dicionario.items()) # mostra os dois
"""Para for composto"""
for keys, valor in dicionario.items():
    print(f'o {keys} é {valor}')
lista = [dicionario]
print(lista[0]['idade'])