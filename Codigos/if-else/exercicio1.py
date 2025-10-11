#Exercício Calculadora IMC
peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura em metros: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'O seu IMC é de {imc}.\nVocê está abaixo do peso.')
elif imc < 25:
    print(f'O seu IMC é de {imc}.\nVocê está no peso ideal.')
elif imc < 30:
    print(f'O seu IMC é de {imc}.\nVocê está obeso.')
elif imc < 35:
    print(f'O seu IMC é de {imc}.\nVocê está com obesidade severa.')
else:
    print(f'O seu IMC é de {imc}.\nVocê está com obesidade mórbida.')