from datetime import datetime

def menu():
    print('\n*******************************************\n')
    print('Escolha a opcao desejada:')
    print('-------------------------------------------\n')
    print('[s] - Saque')
    print('[d] - Deposito')
    print('[e] - Extrato')
    print('[v] - Saldo')
    print('[nu] - Novo User')
    print('[nc] - Nova Conta')
    print('[lc] - Listar contas')
    print('[q] - Sair\n')

    opcao = input(">> ").lower()
    return opcao

def depositar(conta, indice):
    #print(conta)
    saldo = conta[4]['saldo']
    extrato = conta[4]['extrato']
    print(f'\nSaldo atual: {saldo}\n')

    valor = int(input(">> Digite o valor para deposito: "))
    if valor <= 0:
        print('\nValor Invalido')
    else:
        saldo += valor
        conta[4]['saldo'] = saldo
        indice += 1
        data_hora_atual = datetime.now()
        data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
        extrato.append(f"Conta:{conta[3]} - {indice} - {data_hora_formatada} - Deposito realizado - Valor R$ {valor}")
        print(f'\n ----------------------------------\nNovo Saldo: R$ {saldo},00\n\n')
    return (conta, saldo, indice)

def sacar(conta, indice, numero_saques, LIMITE_SAQUES):
    #print(conta)
    saldo = conta[4]['saldo']
    extrato = conta[4]['extrato']
    print(f'\nSaldo atual: {saldo}\n')

    print(f'\n Saldo em Conta: {saldo}')
    print(f'\nVoce ja fez {numero_saques} saques hoje')
    if numero_saques == LIMITE_SAQUES:
        print(f'\nVoce excedeu o limite de 3 saques diarios')
    else:
        #try:
            valor = int(input(">> Digite o valor para Saque: "))
            if valor <= 0:
                print('Valor Invalido')
            elif saldo < valor:
                print('\n\nSaldo Insuficiente')
            elif valor > 500:
                print(f'Limite maximo por saque é R$ 500,00')
            else:
                #print('passou')
                saldo -= valor
                conta[4]['saldo'] = saldo
                indice += 1
                numero_saques += 1
                data_hora_atual = datetime.now()
                data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
                extrato.append(f"Conta:{conta[3]} - {indice} - {data_hora_formatada} - Saque    realizado - Valor R$ {valor}")
                print(f'\n ----------------------------------')
                print(f'Saldo Atualizado: R$ {saldo},00')
                #return (saldo, extrato, indice, numero_saques)
        #except:
            #print('\nValor Invalido - Operação Cancelada')
            #return (saldo, extrato, indice, numero_saques)
 
def ver_extrato(conta):
    extrato = conta[4]['extrato']
    saldo = conta[4]['saldo']
    data_hora_atual = datetime.now()
    data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
    print(f'{data_hora_formatada}') 
    print('\n###############    EXTRATO BANCARIO    ##################\n')

    for item in extrato:
        print(item)

    print(f'\nSaldo: R$ {saldo:.2f}')
    print('\n#############   FIM DO EXTRATO BANCARIO   ###############')

def ver_saldo(conta):
    saldo = conta[4]['saldo']
    print(f'\n ----------------------------------\nNovo Saldo: R$ {saldo},00')

def cad_user(cpf):
    print('\nSeja Bem-Vindo ao Cadastro !!\n')
    nome = input('Digite o seu nome: ')
    data_nascimento = input('Digite sua data de Nascimento: ')
    print("\nAgora preciso de seu endereco\n")
    rua = input('Digite o nome da Rua: ')
    nro = input('Digite o Numero: ')
    bairro = input('Digite seu Bairro: ')
    cidade = input('Digite a cidade: ')
    uf = input('Digite a sigla do estado: ')
    endereco = rua + "," + nro + '-' + bairro + "-" + cidade + '/' + uf
    return (nome, data_nascimento, cpf, endereco)

def cad_conta(clientes, contas, AGENCIA, cpf):
    nome = clientes[0]
    cpf = clientes[2]
    agencia = AGENCIA
    conta = len(contas) + 1
    transacoes = {'saldo':0, 'extrato':[]}
    print(f'Conta criada com sucesso: \n\nCliente:\t{nome}\nConta:\t{agencia}.{conta}\n')
    return (nome, cpf, AGENCIA, conta, transacoes)

def checar_user(clientes): # ('Anderson', '27141755896', '0001', 1)
    cpf = input('Digite seu CPF: ')

    for cliente in clientes:
        if cpf in cliente:
            return cliente, cpf
    return None, cpf

def checar_conta(contas): # ('Anderson', '27141755896', '0001', 1)
    cpf = input('Digite seu CPF: ')
    for conta in contas:
        if cpf in conta:
            return conta, cpf
    return None, cpf

# Faltando organizar o codigo tentei depositra mas nao ta salvando o saldo na lista

def main():

    AGENCIA = "0001"
    saldo = 0
    indice = 0
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3
    extrato = []
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao =="d":
            conta, cpf = checar_conta(contas)
            if conta:
                depositar(conta, indice)
                #indice += transacao[2]
                #print(transacao)
            else:
               print('Abra já a sua conta !!')

        elif opcao == "s":
            conta, cpf = checar_conta(contas)
            if conta:
               sacar(conta, indice, numero_saques, LIMITE_SAQUES)
               #print(transacao)
            else:
                pass

        if opcao =="v":
            conta, cpf = checar_conta(contas)
            if conta:
                ver_saldo(conta)
            else: 
                return

        elif opcao =="e":
            conta, cpf = checar_conta(contas)
            if conta:
                ver_extrato(conta)
            else:
                return
        
        elif opcao =='nu':
            cliente, cpf = checar_user(clientes)
            if cliente:
                print(f'\n Voce ja possui um cadastro em nosso Banco Sr.(a) {cliente[0]}')
            else:
                clientes.append(cad_user(cpf))
                for cliente in clientes:
                    print(f'\nCliente:{cliente[0]}, data:{cliente[1]}, cpf:{cliente[2]}, endereco:{cliente[3]}')

        elif opcao =="nc":
            cliente, cpf = checar_user(clientes)
            if cliente:
                print('\nVamos cadastrar sua conta\n')
                contas.append(cad_conta(cliente, contas, AGENCIA, cpf))
            else:
                clientes.append(cad_user(cpf))

        elif opcao =="lc":
            if contas:
                for conta in contas:
                    print(f'\nAgencia:\t{conta[2]}\nConta:\t{conta[3]}\nUsuario:\t{conta[0]}\nCPF:\t{conta[1]}\n')
            else:
                 print('\nNao ha contas cadastradas !')

        elif opcao =="q":
            print('\nObrigado por Ser nosso Cliente !!')
            break
        

        # else:
        #     print("Operacao invalida, por favor selecione novamente a operacao desejada.")
            
main()