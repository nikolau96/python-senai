import os
import time

os.system('cls')
numero = 15
cont = 1
while True:
    usuario = int(input('Qual é o número secreto?: '))
    if cont == 4:
        os.system('cls')
        print('PERDEU MANÉ')
        print('KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK')
        break
    elif usuario == 15:
        os.system('cls')
        print('Parabéns!!!\nVocê acertou o número secreto\n')
        break
    else:
        os.system('cls')
        print('Erroooooooooooooooooooooooooooooooooooooooooooooooooooooooouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu!!!')
        print('Tente acertar da próxima vez')
        if usuario < numero:
            print('O número indicado é menor que o número secreto')
        else:
            print('O número indicado é maior que o número secreto')
        time.sleep(5)
        os.system('cls')

        cont = cont + 1
