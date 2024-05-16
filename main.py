from datetime import datetime

saldo = 0
indice = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = []

while True:
    print('\n*******************************************************************\n')
    print('Escolha a opcao desejada:')
    print('-------------------------------------------\n')
    print('[s] - Saque')
    print('[d] - Deposito')
    print('[e] - Extrato')
    print('[v] - Saldo')
    print('[q] - Sair\n')

    opcao = input(">> ").lower()

    if opcao =="d":
        try:               
            print(f'\nSaldo atual: {saldo}')
            valor = int(input(">> \nDigite o valor para deposito: "))
            if valor <= 0:
                print('\nValor Invalido')
            else:
                saldo += valor
                indice += 1
                data_hora_atual = datetime.now()
                data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
                extrato.append(f"{indice} - {data_hora_formatada} - Deposito realizado - Valor R$ {valor}")
                print(f'\n ----------------------------------\nNovo Saldo: R$ {saldo},00')
        except:
            print('\n\nDigite um valor válido, operação Cancelada')

    elif opcao == "s":
        try:
            print(f'\n Saldo em Conta: {saldo}')
            if numero_saques == LIMITE_SAQUES:
                print(f'Voce excedeu o limite de 3 saques diarios')
            else:
                valor = int(input("Digite o valor para Saque: "))
                if valor <= 0:
                    print('Valor Invalido')
                elif saldo < valor:
                    print('\n\nSaldo Insuficiente')
                elif valor > 500:
                    print(f'Limite maximo por saque é R$ {limite},00')  
                else:
                    saldo -= valor
                    indice += 1
                    numero_saques += 1
                    data_hora_atual = datetime.now()
                    data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
                    extrato.append(f"{indice} - {data_hora_formatada} - Saque realizado - Valor R$ {valor}")
                    print(f'\n ----------------------------------')
                    print(f'Saldo Atualizado: R$ {saldo},00')
        except:
            print('\n\n Digite um valor válido, operação Cancelada')
    
    if opcao =="v":

        print(f'\n ----------------------------------\nNovo Saldo: R$ {saldo},00')

    elif opcao =="e":
        data_hora_atual = datetime.now()
        data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
        print(f'{data_hora_formatada}') 
        print('\n###############    EXTRATO BANCÁRIO    ##################\n')

        for item in extrato:
            print(item)

        print(f'\nSaldo: R$ {saldo:.2f}')
        print('\n#############   FIM DO EXTRATO BANCÁRIO   ###############')


    elif opcao =="q":
        print('\n Obrigado por Ser nosso Cliente !!')
        break
    

else:
    print("Operação invalida, por favor selecione novamnete a operaçao desejada.")
        
    
