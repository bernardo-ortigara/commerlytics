import defs

def nome():
  nome = input('Nome: ')
  while nome == '':
    print('Erro! Entrada Vazia.')
    nome = input('Digite um nome válido: ')
    
def cpf():
  cpf_digitado = input('Digite seu CPF: ')
  cpf_digitado = defs.tira_ponto_cpf(cpf_digitado)
  while cpf_digitado.isdigit() == False or len(cpf_digitado) != 11:
    cpf_digitado = input('Certifique-se que o CPF tenha 11 números (apenas dígitos). Digite novamente: ')
    cpf_digitado = defs.tira_ponto_cpf(cpf_digitado)
    cpf = cpf_digitado

def data():
  while True:
    data = input('Data (dd/mm/aaaa): ')
    if data == '':
        print('Erro! Entrada inválida.')
        continue
    temp = ''.join(data.split('/'))  # retorna uma string de valores sem '/'
    if not temp.isnumeric():         # analisa se essa string tem caracteres
        print('Insira uma data válida')
        continue
    # data.count('/') retorna o numero de '/' na data
    if data.count('/') == 2 and data != '//':  # Checa se data tem duas '/' e não é apenas //
        dia, mes, ano = data.split('/')        # cada valor divido é jogado nas variaveis em sequencia
        if 1 <= int(dia) <= 31 and 1 <= int(mes) <= 12 and 1900 <= int(ano) <= 2025:
            return data.strip(' ')
        else:
            print('Dia/Mes/Ano Inválido(s)')
    else:
        print('A data deve seguir o padrão dd/mm/aaaa')
    
def item():
  while True:
    entrada = input('Item: ')
    if entrada == '':
      print('Erro! Entrada inválida.')
    else:
      item = entrada
      break
  
def valor():
  while True:
    entrada = input('Valor: ')
    if entrada == '':
        print('Erro! Entrada inválida.')
    elif entrada.replace('.', '', 1).isdigit():
        valor = float(entrada)
        if valor < 0:
            print('Erro! Valor não pode ser negativo.')
        else:
            break
    else:
        print('Erro! Digite um número válido.')
        
def quantidade():
  while True:
    entrada = input('Quantidade: ')
    if entrada == '':
        print('Erro! Entrada inválida.')
    elif entrada.isdigit():
        quantidade = int(entrada)
        break
    else:
        print('Erro! Digite um número inteiro válido.')
  
def comissionado():
  while True:
    entrada = input('Comissionado: ')
    if entrada == '':
      print('Erro! Entrada inválida.')
    else:
      comissionado = entrada
      break
  
def canal():
  while True:
    entrada = input('Comissionado: ')
    if entrada == '':
      print('Erro! Entrada inválida.')
    else:
      canal = entrada
      break
