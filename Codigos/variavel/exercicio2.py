#Exercício 2
#Crie um código para calcular o valor da HIPOTENUSA de um triângulo. O usuário irá inserir o valor primeiro cateto depois o valor do segundo e por fim o código mostrará o valor da HIPOTENUSA.
cateto1 = float(input('Digite o valor do primeiro cateto: '))
cateto2 = float(input('Digite o valor do segundo cateto: '))
hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2))
print(f'O valor da hipotenusa é {hipotenusa}')