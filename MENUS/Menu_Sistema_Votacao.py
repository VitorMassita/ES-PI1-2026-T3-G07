"""Sitema de Votação"""
def menu_sistem_votacao_func():
    global menu_sistem_votacao
    while menu_votacao == 1:
        try:
            print("\n0 - Voltar\n1 - Solicitar Dados")
            menu_sistem_votacao= int(input("Escolha a opção desejada: "))
            match menu_sistem_votacao:
                case 0:
                    print("Voltando...")
                    return(vt.menu_votacao_func())
                case 1:
                    print("Solitar Dados")
                    break   
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")