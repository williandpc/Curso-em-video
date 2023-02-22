from time import sleep


def maior(lst):
    print("-="*30)
    print('Analisando os valores passados...')
    sleep(0.5)
    for num in lst:
        print(num, end=' ')
        sleep(0.5)
    print(f"""Foram informados {len(lst)} valores ao todo.
O maior valor informado foi {max(lst) if len(lst) != 0 else 0}.""")


maior([2, 9, 4, 5, 7, 1])
maior([4, 7, 0])
maior([1, 2])
maior([6])
maior(list())
