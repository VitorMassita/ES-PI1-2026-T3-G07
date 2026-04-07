"""Auditoria"""
def menu_auditoria_func():
    global menu_auditoria
    while menu_votacao == 2:
        try:
            print("\n0 - Voltar\n1 - Logs \n 2 - Protocolo de Votação")
            menu_auditoria= int(input("Escolha a opção desejada: "))
            match menu_auditoria:
                case 0:
                    print("Voltando...")
                    return(vt.menu_votacao_func())
                case 1:
                    print("Logs")
                    break   
                case 2:
                    print("Protocolo de Votação")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")