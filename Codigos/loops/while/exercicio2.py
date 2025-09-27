import os
import time

os.system('cls')
numero = 15
while True:
    usuario = int(input('Qual é o número secreto?: '))
    if usuario == 15:
        os.system('cls')
        print('Parabéns!!!\nVocê acertou o número secreto')
        break
    else:
        os.system('cls')
        print('Erroooooooooooooooooooooooooooooooooooooooooooooooooooooooouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu!!!')
        print('Tente acertar da próxima vez')
        time.sleep(5)
        os.system('cls')