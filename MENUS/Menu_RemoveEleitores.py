import CondicoesGlobais as estado
import Menu_Eleitores as el 

def menu_removeeleitores_func():
    while estado.menu_eleitores == 2:
        try:
            print("\n0 - Voltar\n1 - Remover Eleitores")
            estado.menu_removeeleitores= int(input("Escolha a opção desejada: "))
            match estado.menu_removeeleitores:
                case 0:
                    print("Voltando...")
                    el.menu_eleitores_func()
                    return
                case 1:
                    print("Remover Eleitores")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")