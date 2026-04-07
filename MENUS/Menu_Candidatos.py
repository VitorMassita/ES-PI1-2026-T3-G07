"""Menu Candidatos"""
def menu_candidatos_func():
    global menu_candidatos
    while menu_gerenciamento == 1:
        try:
            print("\n0 - Voltar\n1 - Lista de Candidatosn \n2 - Remoção de Candidatos \n3 - Busca de Candidatos \n4 - Edição de Dados \n5 - Cadastramento")
            menu_candidatos= int(input("Escolha a opção desejada: "))
            match menu_candidatos:
                case 0:
                    print("Voltando...")
                    return(gr.menu_gerenciamento_func())
                case 1:
                    print("Lista de Candidatos")
                    break    
                case 2:
                    print("Remoção de Candidatos")
                    break
                case 3 : 
                    print("Busca de Candidatos")
                    break   
                case 4: 
                    print("Edição de Dados")
                    menu_edicaodados_func()
                    break
                case 5: 
                    print("Cadastramento")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")