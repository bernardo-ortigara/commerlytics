import defs

def nome():
  while true:
    nome = input('Nome: ')
    while nome == '':
      print('Erro! Entrada Vazia.')
      nome = input('Digite um nome válido: ')
    
def cpf():
  while true:
    cpf_digitado = input('Digite seu CPF (apenas números): ')
    if cpf_digitado.isdigit():
      if len(cpf_digitado) == 11:
        cpf_digitado = cpf
      else:
        while len(cpf) != 11:
        cpf = input('Certifique-se que o CPF tenha 11 números. Digite novamente: ')
         
    else:
      cpf_com_pontos = cpf_digitado
      cpf_sem_pontos = cpf_com_pontos.replace(".", "")
      if len(cpf_sem_pontos) == 11:
        cpf_digitado = cpf


def data():
  
def item():
  
def valor():
  
def quantidade():
  
def comissionado():
  
def canal():
