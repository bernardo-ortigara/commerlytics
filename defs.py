import os
import datetime

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
    recebe_pesquisa = input('🔎 ')

    return recebe_pesquisa

def volta_menu():
    input('''\033[2;49;39mPressione Enter para voltar ao menu \033[0;0m''')

def invalida():
    print('\n''\033[1;49;91mOpção inválida. Tente novamente. \033[0;0m''')

def cadastra():
    print('Aba cadastro')

def lista():
    print('Aba lista')

def gera_relatorio():
    print('Aba relatório')

def sai():
    print('Volte sempre ;)')
