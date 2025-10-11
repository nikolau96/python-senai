#Exercício Consumo Watt
consumo = int(input('Digite o seu consumo: '))
if consumo >= 1 and consumo <= 100:
    valor = consumo * 0.65
    print(f'Total a pagar: R${valor}')
elif consumo <= 150:
    valor = consumo * 0.70
    print(f'Total a pagar: R${valor}')
elif consumo <= 200:
    valor = consumo * 0.75
    print(f'Total a pagar: R${valor}')
else:
    valor = consumo * 0.80
    print(f'Total a pagar: R${valor}')