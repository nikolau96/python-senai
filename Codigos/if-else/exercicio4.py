print("MENU PIZZARIA")
print('Escolha o sabor da pizza:\n1 - Calabresa\n2 - Napolitana\n3 - Portuguesa\n4 - Marguerita')
# print('''
# Escolha o sabor da pizza
# 1 - Calabresa
# 2 - Napolitana 
# 3 - Portuguesa
# 4 - Marguerita
# '''
# )
# Comentar várias linhas = CTRL + ;
opcao = int(input('\nDigite o sabor escolhido: '))
if opcao == 1:
    vr_pizza = 42.5
elif opcao == 2:
    vr_pizza = 32.5
elif opcao == 3:
    vr_pizza = 36.5
elif opcao == 4:
    vr_pizza = 39.8
else:
    print('ERRO!!! Opção não permitida.')
refri_input = input('Deseja refrigerante? (S/N): ')
refri = refri_input.upper()
if refri == 'S':
    total = vr_pizza + 8.9
elif refri == 'N':
    total = vr_pizza
else:
    print('ERRO!!! Opção não permitida.')
print(f'Valor total da compra: R${total:0.2f}')
