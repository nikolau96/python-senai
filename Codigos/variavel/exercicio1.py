#Exercício 1
#Crie um código para conversão de US$ para R$, use como base a cotação do dólar de hoje.
dolar = float(input('Digite o valor a ser convertido: '))
real = dolar * 5.53
print(f'US${dolar} é equivalente a R${real}')