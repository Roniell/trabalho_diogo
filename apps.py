from Servico import *

# Menu em loop
while True:
    print('#' * 24)
    print('# 1 - Novo cliente           #')
    print('# 2 - Buscar cliente         #')
    print('# 3 - Mostrar todos          #')
    print('# 4 - Alterar cliente        #')
    print('# 5 - Pagar conta            #')
    print('# 6 - Pagar parcialmente     #')
    print('# 7 - Sair                   #')
    print('#' * 24)

    op = input('Informe a operação:')

    if op == '1':
        cpf = input('Informe o cpf:')
        nome = input('Informe o nome:')
        sexo = input('Informe o sexo:')
        telefone = input('Informe o telefone:')
        cidade = input('Informe a cidade:')
        estado = input('Informe o estado:')
        endereco = input('Informe o endereco:')
        cep = input('Informe o cep:')
        conta = input('Informe a conta:')
        novo_cliente(cpf, nome, sexo, telefone, cidade, estado, endereco, cep, conta)

    elif op == "2":
        nome = input('Informe o nome :')
        print(buscar_cliente_por_nome(nome))

    elif op == "3":
        print(mostrar_todos())


    elif op == "4":
        cpf_busca = int(input('Informe o cpf do cliente:'))
        cpf = int(input('Informe o cpf:'))
        nome = input('Informe o nome:')
        sexo = input('Informe o sexo:')
        telefone = int(input('Informe o telefone:'))
        cidade = input('Informe a cidade:')
        estado = input('Informe o estado:')
        endereco = input('Informe o endereco:')
        cep = int(input('Informe o cep:'))
        conta = int(input('Informe a conta:'))
        alterar_cliente(cpf, nome, sexo, telefone, cidade, estado, endereco, cep, conta, cpf_busca)
    #
    # elif op == "5":
    #
    # elif op == "6":
    #
    # elif op == "7":
