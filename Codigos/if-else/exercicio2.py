print('** CÁLCULO DE DESCONTO **')
compra = float(input('Digite o valor da compra: '))
if compra <= 100:
    desconto = 0
elif compra <= 300:
    desconto = compra * 0.1
elif compra <= 400:
    desconto = compra * 0.15
else:
    desconto = compra * 0.2
print(f'Desconto: R${desconto:0.2f}') #a parte da variável {desconto:0.2f} = limita o número de casas decimais exibidas
total = compra - desconto
print(f'Total a pagar: R${total:0.2f}')