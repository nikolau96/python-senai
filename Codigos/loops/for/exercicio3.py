valor = int(input('Insira o número da tabuada: '))
inicio = int(input('Começar por: '))
fim = int(input('Terminar por: '))
print(f'Vou montar a tabuada de {valor} começando por {inicio} e terminando por {fim}')
for i in range(inicio, (fim + 1)):
    print(f'{i} - {valor} X {i} = {valor * i}')