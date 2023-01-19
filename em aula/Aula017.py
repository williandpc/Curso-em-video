"""    LISTAS
~~para adicionar itens em listas:
*nome da lista*.append({item a ser adicionado na lista})
para isso, sera adicionado um novo index na lista para o novo item
~~para adicionar um item extra em um index ja criado.
{nome da lista}.instert({número do index onde vai ser acrescentado item, item})
ele move o item encontrado no index e todos após para a direita e acrescenta o item no index desejado
por exemplo: """
lista = ['arroz', 'feijão', 'batata']
print(f'{lista} = lista antes')
lista.insert(0, 'bolacha')
print(f'{lista} = lista após acrescentar bolacha no index 0')

""" para apagar elementos temos alguns modos
"""
del lista[0]
print(f'{lista} = lista após apagar com "del" antes do  index selecionado')
lista.pop(2)
print(f'{lista} = lista após apagar com o .pop um index selecionado')
lista.append('batata')
lista.append('bolacha')
print(f'{lista} = lista após adicionar palavras com o .append')
lista.remove('bolacha')
print(f'{lista} = lista após apagar com o .remove um item specifico procurado')

for indice, valor in enumerate(lista):
    print(f'para o indice {indice} temos o valor {valor}')
""" o remove elimina somente o primeiro elemento encontrado
    se igualar listas como: *lista copia* = *lista original*, todas as alterações em uma lista sera aplicada na outra lista;
    para simplesmente criar uma copia da lista e nao alterar a lista origianl futuramente, 
    temos que adicionar da seguinte forma: *lista copia* = *lista original*[:]. Assim as duas listas nao tem mais ligação
     #função list faz uma listagem"""