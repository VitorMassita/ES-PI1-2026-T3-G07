import CondicoesGlobais as estado
import Menu_Eleitores as el 

def menu_edicaodados_ele_func():
    while estado.menu_eleitores == 4:
        try:
            print("\n0 - Voltar\n1 - Editar Nome\n2 - Editar Idade\n3 - Editar Documentos")
            estado.menu_edicaodados_ele= int(input("Escolha a opção desejada: "))
            match estado.menu_edicaodados_ele:
                case 0:
                    print("Voltando...")
                    el.menu_eleitores_func()
                    return
                case 1:
                    print("Editar Nome")
                    break
                case 2:
                    print("Editar Idade")
                    break
                case 3: 
                    print("Editar Documentos")
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")