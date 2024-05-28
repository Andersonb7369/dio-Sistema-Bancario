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

def depositar(saldo, valor, extrato, indice):             
    saldo += valor
    indice += 1
    data_hora_atual = datetime.now()
    data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
    extrato.append(f"{indice} - {data_hora_formatada} - Deposito realizado - Valor R$ {valor}")
    print(f'\n ----------------------------------\nNovo Saldo: R$ {saldo},00')
    return (saldo, extrato, indice)

def sacar(saldo, valor, extrato, indice, numero_saques):
    saldo -= valor
    indice += 1
    numero_saques += 1
    data_hora_atual = datetime.now()
    data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
    extrato.append(f"{indice} - {data_hora_formatada} - Saque realizado - Valor R$ {valor}")
    print(f'\n ----------------------------------')
    print(f'Saldo Atualizado: R$ {saldo},00')
    return (saldo, extrato, indice, numero_saques)
 
def ver_extrato(saldo, extrato):
    data_hora_atual = datetime.now()
    data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
    print(f'{data_hora_formatada}') 
    print('\n###############    EXTRATO BANCÁRIO    ##################\n')

    for item in extrato:
        print(item)

    print(f'\nSaldo: R$ {saldo:.2f}')
    print('\n#############   FIM DO EXTRATO BANCÁRIO   ###############')

def ver_saldo(saldo):
    print(f'\n ----------------------------------\nNovo Saldo: R$ {saldo},00')

def cad_user():
    print('Seja Bem-Vindo ao Cadastro !!')
    nome = input('Digite o seu nome: ')
    data_nascimento = input('Digite sua data de Nascimento: ')
    cpf = input('Digite seu CPF sem pontos: ')
    print("Agora preciso de seu endereço")
    rua = input('Digite o nome da Rua: ')
    nro = input('Digite o Numero: ')
    bairro = input('Digite seu Bairro: ')
    cidade = input('Digite a cidade: ')
    uf = input('Digite a sigla do estado: ')
    endereco = rua + "," + nro + '-' + bairro + "-" + cidade + '/' + uf
    return (nome, data_nascimento, cpf, endereco)

def cad_conta(clientes, contas, AGENCIA):
        cpf1 = input('Digite seu CPF: ')
        for lista in clientes:
            if cpf1 in lista[2]:
                nome = lista[0]
                cpf = lista[2]
                agencia = AGENCIA
                conta = len(contas) + 1
                print(f'Conta criada com sucesso: \n\nCliente:\t{nome}\nConta:\t{agencia}.{conta}\n')
            return (nome, cpf, AGENCIA, conta)

def checar_user(clientes):
    user_atual = input('Digite seu CPF: ')

    for cliente in clientes:
        if user_atual in cliente:
            return cliente
    return

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
            print(f'\nSaldo atual: {saldo}\n')
            valor = int(input(">> Digite o valor para deposito: "))
            if valor <= 0:
                print('\nValor Invalido')
            else:
                saldo, extrato, indice = depositar(saldo, valor, extrato, indice)

        elif opcao == "s":
            print(f'\n Saldo em Conta: {saldo}')
            print(f'Voce ja fez {numero_saques} saques hoje')
            if numero_saques == LIMITE_SAQUES:
                print(f'Voce excedeu o limite de 3 saques diarios')
            else:
                try:
                    valor = int(input(">> Digite o valor para Saque: "))
                    print(valor)
                    if valor <= 0:
                        print('Valor Invalido')
                    elif saldo < valor:
                        print('\n\nSaldo Insuficiente')
                    elif valor > 500:
                        print(f'Limite maximo por saque é R$ {limite},00')
                    else:
                        saldo, extrato, indice, numero_saques = sacar(saldo, valor, extrato, indice, numero_saques)
                except:
                    print('\nValor Invalido - Operação Cancelada')
                    
        if opcao =="v":
            ver_saldo(saldo)

        elif opcao =="e":
            ver_extrato(saldo, extrato)
        
        elif opcao =='nu':
            cliente = checar_user(clientes)
            if cliente:
                print(f'\n Voce já possui um cadastro em nosso Banco Sr.(a) {cliente[0]}')
            else:
                clientes.append(cad_user())

        elif opcao =="nc":
            cliente = checar_user(clientes)
            if cliente:
                print('\nVamos cadastrar sua conta\n')
                contas.append(cad_conta(clientes, contas, AGENCIA))
            else:
                clientes.append(cad_user())

        elif opcao =="lc":
            for conta in contas:
                print(f'Agencia:\t{conta[2]}\nConta:\t{conta[3]}\nUsuario:\t{conta[0]}\nCPF:\t{conta[1]}\n\n')
                
        elif opcao =="q":
            print('\nObrigado por Ser nosso Cliente !!')
            break
        

        # else:
        #     print("Operacao invalida, por favor selecione novamente a operacao desejada.")
            
main()