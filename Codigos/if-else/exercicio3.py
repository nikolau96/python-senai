print("** CÁLCULO DE FRETE **")
compra = float(input('Digite o valor da compra: '))
distancia = float(input('Digite a distância da entrega em km: '))
if compra > 200:
    frete = 0
elif distancia <= 50:
    frete = distancia * 1
elif distancia > 50:
    frete = distancia * 1.5
print(f'Valor do frete: R${frete:0.2f}')
print(f'Valor total da compra: R${compra+frete:0.2f}')