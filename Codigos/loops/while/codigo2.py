import os
import msvcrt
import time

os.system('cls')

while True:
    email = input('Digite seu email: ')
    senha = input('Digite a sua senha: ')

    if email == 'teste@teste.com' and senha == '123':
        print('Acesso permitido!')
        break
    else:
        os.system('cls')
        print('Acesso negado')
        print('Tente novamente!')
        time.sleep(3)
        os.system('cls')