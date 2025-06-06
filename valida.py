import defs

def nome():
  while true:
    nome = input('Nome: ')
    while nome == '':
      print('Erro! Entrada Vazia.')
      nome = input('Digite um nome válido: ')
    
def cpf():
  while true:
  cpf = 1
  cpf_digitado = input('Digite seu CPF (apenas números): ')
  if cpf_digitado.isdigit(): #confere se tem pontos no meio 
      if len(cpf_digitado) == 11: #confere se tem os 11 digitos
          cpf = cpf_digitado #variavel que vai ser usada (cpf)
      else:
          while len(cpf_digitado) != 11:
            cpf_digitado = input('Certifique-se que o CPF tenha 11 números. Digite novamente: ')
            cpf_com_pontos = cpf_digitado
            cpf_sem_pontos = cpf_com_pontos.replace('.', '')
            cpf_digitado = cpf_sem_pontos
            cpf = cpf_sem_pontos
  else:
      cpf_com_pontos = cpf_digitado
      cpf_sem_pontos = cpf_com_pontos.replace('.', '')
      cpf_digitado = cpf_sem_pontos
    
      if len(cpf_digitado) == 11:
        cpf = cpf_sem_pontos
      else:
        while len(cpf_digitado) != 11:
            cpf_digitado = input('Certifique-se que o CPF tenha 11 números. Digite novamente: ')
            cpf_com_pontos = cpf_digitado
            cpf_sem_pontos = cpf_com_pontos.replace('.', '')
            cpf_digitado = cpf_sem_pontos
            cpf = cpf_sem_pontos


def data():
  
def item():
  
def valor():
  
def quantidade():
  
def comissionado():
  
def canal():
