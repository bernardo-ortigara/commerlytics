import os
import datetime
import json
import valida

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
    nome = valida.nome()
    cpf = valida.cpf()
    data = valida.data()
    item = input('Item: ')
    valor = valida.valor()
    quantidade = valida.quantidade()
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
    limpa_terminal()
    print('======== <<< ''\033[1;37;40m''RELATÓRIO DE VENDAS''\033[0;0m >>> ========')
    print('')
    vendas = lista_clientes()
    
    if not vendas:
        print("\n\033[1;49;93mNenhuma venda cadastrada para gerar relatório.\033[0;0m")
        return

    total_vendas = sum(venda['valor'] for venda in vendas)
    total_itens_vendidos = sum(int(venda['quantidade']) for venda in vendas)

    resumo_por_item = {}
    for venda in vendas:
        item = venda['item']
        quantidade = int(venda['quantidade'])
        valor = venda['valor']
        
        if item in resumo_por_item:
            resumo_por_item[item]['quantidade'] += quantidade
            resumo_por_item[item]['total_valor'] += valor
        else:
            resumo_por_item[item] = {'quantidade': quantidade, 'total_valor': valor}


    gasto_por_cliente = {}
    for venda in vendas:
        nome_cliente = venda['nome']
        valor_gasto = venda['valor']
        gasto_por_cliente[nome_cliente] = gasto_por_cliente.get(nome_cliente, 0) + valor_gasto
    
    
    top_5_clientes = sorted(gasto_por_cliente.items(), key=lambda item: item[1], reverse=True)[:5]
    top_5_clientes_formatado = [{ "cliente": nome, "gasto": valor } for nome, valor in top_5_clientes]

    vendas_por_canal = {}
    for venda in vendas:
        canal = venda['canal']
        vendas_por_canal[canal] = vendas_por_canal.get(canal, 0) + 1
    canais_mais_vendidos_list = sorted(vendas_por_canal.items(), key=lambda item: item[1], reverse=True)[:5]
    canais_mais_vendidos = dict(canais_mais_vendidos_list)
    
    itens_vendidos_contagem = {}
    for venda in vendas:
        item = venda['item']
        itens_vendidos_contagem[item] = itens_vendidos_contagem.get(item, 0) + int(venda['quantidade'])
    
    produto_mais_vendido_info = None
    if itens_vendidos_contagem:
        produto_mais_vendido_tuple = max(itens_vendidos_contagem.items(), key=lambda item: item[1])
        if produto_mais_vendido_tuple:
            nome_prod, qtd_prod = produto_mais_vendido_tuple
            produto_mais_vendido_info = {"produto": nome_prod, "quantidade_vendida": qtd_prod}

    data_emissao = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    nome_arquivo = f"relatorio_vendas_{data_emissao}.json"

    relatorio_dados = {
        "data_emissao": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "total_geral_vendas": total_vendas,
        "total_geral_itens_vendidos": total_itens_vendidos,
        "resumo_por_item": resumo_por_item,
        "analises_adicionais": {
            "top_5_clientes_maior_gasto": top_5_clientes_formatado,
            "canais_mais_vendidos": canais_mais_vendidos,
            "produto_mais_vendido": produto_mais_vendido_info
        },
        "detalhes_vendas": vendas
    }

    # --- INÍCIO DA IMPRESSÃO NO CONSOLE ---
    #print("--- Relatório de Vendas ---")
    print(f"Data de Emissão: {relatorio_dados['data_emissao']}")
    print(f"Total Vendas: R$ {relatorio_dados['total_geral_vendas']:.2f}")
    print(f"Total Itens Vendidos: {relatorio_dados['total_geral_itens_vendidos']}")

    print("\n--- Resumo por Item ---")
    if relatorio_dados['resumo_por_item']:
        for item, dados in relatorio_dados['resumo_por_item'].items():
            print(f"\nItem: {item}")
            print(f"Quantidade Vendida: {dados['quantidade']}")
            print(f"Total Valor: R$ {dados['total_valor']:.2f}")
    else:
        print("Nenhum item vendido.")

    print("\n--- Análises Adicionais ---")
    print("\nTop 5 Clientes com Maior Gasto:")
    if relatorio_dados['analises_adicionais']['top_5_clientes_maior_gasto']:
        for cliente_info in relatorio_dados['analises_adicionais']['top_5_clientes_maior_gasto']:
            print(f"- Cliente: {cliente_info['cliente']} | Gasto: R$ {cliente_info['gasto']:.2f}")
    else:
        print("\nNenhum cliente com gasto registrado.")

    print("\nCanais Mais Vendidos:")
    if relatorio_dados['analises_adicionais']['canais_mais_vendidos']:
        for canal, quantidade_vendas in relatorio_dados['analises_adicionais']['canais_mais_vendidos'].items():
            print(f"- Canal: {canal}, Vendas: {quantidade_vendas}")
    else:
        print("\nNenhum canal de venda registrado.")

    print("\nProduto Mais Vendido:")
    if relatorio_dados['analises_adicionais']['produto_mais_vendido']:
        prod_info = relatorio_dados['analises_adicionais']['produto_mais_vendido']
        print(f"- Produto: {prod_info['produto']}, Quantidade Vendida: {prod_info['quantidade_vendida']}")
    else:
        print("\nNenhum produto vendido.")


   #print("\n--- Detalhes de Todas as Vendas ---")
    #if relatorio_dados['detalhes_vendas']:
        #for i, venda in enumerate(relatorio_dados['detalhes_vendas']):
            #print(f"  Venda #{i+1}:")
            #print(f"    Nome: {venda['nome']}")
            #print(f"    CPF: {venda['cpf']}")
            #print(f"    Data: {venda['data']}")
            #print(f"    Item: {venda['item']}")
            #print(f"    Valor: R$ {venda['valor']:.2f}")
            #print(f"    Quantidade: {venda['quantidade']}")
            #print(f"    Comissionado: {venda['comissionado']}") # O campo ainda pode existir nos dados de venda
            #print(f"    Canal: {venda['canal']}")
            #print("    ---")
    #else:
        #print("  Nenhuma venda para exibir detalhes.")

    print("\n--- Fim do Relatório ---")

    # --- FIM DA IMPRESSÃO NO CONSOLE ---

    print('')
    escolha_relatorio = input("Digte 1 para exportar relatório ou 2 para sair: ")

    if escolha_relatorio == '1':
        try:
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                json.dump(relatorio_dados, f, indent=4, ensure_ascii=False)
            print(f"\n\033[1;32mRelatório de vendas gerado com sucesso em '{nome_arquivo}'\033[0;0m")
        except IOError as e:
            print(f"\n\033[1;49;91mErro ao salvar o relatório: {e}\033[0;0m")


def sai():
    print('\033[1;37;40m''Volte sempre ;)''\033[0;0m')
    print('')

def tira_ponto_cpf():
    cpf_com_pontos = cpf_digitado
    cpf_sem_pontos = cpf_com_pontos.replace('.', '')
    cpf_digitado = cpf_sem_pontos
    cpf = cpf_sem_pontos
 
