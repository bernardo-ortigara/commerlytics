import defs
import time

while True:
    defs.limpa_terminal()
    escolha = defs.menu()

    if escolha == '1':
        defs.limpa_terminal()
        defs.pesquisa()
        print('')
        defs.volta_menu()

    elif escolha == '2':
        defs.limpa_terminal()
        defs.cadastra()

    elif escolha == '3':
        defs.limpa_terminal()
        defs.lista()
        print("\n\n\n")
        defs.volta_menu()

    elif escolha == '4':
        defs.limpa_terminal()
        defs.gera_relatorio()
        print('')
        defs.volta_menu()

    elif escolha == '5':
        defs.limpa_terminal()
        defs.sai()
        break

    else:
        defs.invalida()
        time.sleep(2)
