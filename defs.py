import os
import datetime
import json

def limpa_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/Mac
        os.system('clear')

def criar_barra():
    print('\n')
    print('')
    print('\n')

data = datetime.datetime.now()
dia = data.day
mes = data.month
ano = data.year

def menu():
    print('===== <<< ''\033[1;37;40m''DARTH COMPANY™''\033[0;0m >>> =====')
    print('|                                |') 
    print('|     [''\033[1;37;40m''1''\033[0;0m''] Pesquisar venda        |')
    print('|     [''\033[1;37;40m''2''\033[0;0m''] Cadastrar venda        |')
    print('|     [''\033[1;37;40m''3''\033[0;0m''] Listar clientes        |')
    print('|     [''\033[1;37;40m''4''\033[0;0m''] Gerar relatório        |')
    print('|     [''\033[1;37;40m''5''\033[0;0m''] Sair                   |')
    print('|                                |')
    print('==================================')
    print(' ')

    x = input('''\033[1;37;40mEscolha uma opção: \033[0;0m''')
    return x

def pesquisa():
    print('======== <<< ''\033[1;37;40m''PESQUISAR''\033[0;0m >>> ========')
    print('')
    recebe_pesquisa = input('> ')
    dados = lista_clientes()
    for cliente in dados:
        nome = cliente['nome'].strip().lower()
        cpf = cliente['cpf']

        if recebe_pesquisa == nome or recebe_pesquisa == cpf:

            limpa_terminal()
            
            print('======== <<< ''\033[1;37;40m''PESQUISAR''\033[0;0m >>> ========')
            print('')

            print(f"Nome: {cliente['nome']}")
            print(f"CPF: {cliente['cpf']}")
            print(f"Data: {cliente['data']}")
            print(f"Item: {cliente['item']}")
            print(f"Valor: {cliente['valor']}")
            print(f"Quantidade: {cliente['quantidade']}")
            print(f"Comissionado: {cliente['comissionado']}")
            print(f"Canal: {cliente['canal']}")

def volta_menu():
    input('''\033[2;49;39mPressione Enter para voltar ao menu \033[0;0m''')

def invalida():
    print('\n''\033[1;49;91mOpção inválida. Tente novamente. \033[0;0m''')
    print('')

def lista_clientes():
    if os.path.exists('clientes.json'):
        with open ('clientes.json', 'r', encoding = 'utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []
    
def imprime_clientes():
    dados = lista_clientes()
    for cliente in dados:
        nome_formatado = cliente['nome'].ljust(30)
        print(f"\033[1;37;40mNome: \033[0;0m{nome_formatado}\033[1;37;40mCPF:\033[0;0m {cliente['cpf']}")

def cadastra():
    print('======== <<< ''\033[1;37;40m''CADASTRAR''\033[0;0m >>> ========')
    print('')
    nome = input('Nome: ')
    cpf = input('CPF: ')
    data = input('Data: ')
    item = input('Item: ')
    valor = float(input('Valor: '))
    quantidade = input('Quantidade: ')
    comissionado = input('Comissionado: ')
    canal = input('Canal: ')

    cliente_novo = {
        'nome': nome,
        'cpf': cpf,
        'data': data,
        'item': item,
        'valor': valor,
        'quantidade': quantidade,
        'comissionado': comissionado,
        'canal': canal,
    }

    clientes = lista_clientes()
    clientes.append(cliente_novo)

    with open('clientes.json', 'w', encoding='utf-8') as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)

    print('')
    input('''\033[2;49;39mPressione Enter para confirmar \033[0;0m''')

def lista():
    print('================= <<< ''\033[1;37;40m''CLIENTES''\033[0;0m >>> =================')
    print('')
    imprime_clientes()

def gera_relatorio():
    print('Aba relatório')

def sai():
    print('\033[1;37;40m''Volte sempre ;)''\033[0;0m')
    print('')

def tira_ponto_cpf():
    cpf_com_pontos = cpf_digitado
    cpf_sem_pontos = cpf_com_pontos.replace('.', '')
    cpf_digitado = cpf_sem_pontos
    cpf = cpf_sem_pontos
 