import CondicoesGlobais as estado
import Menu_Eleitores as el

def menu_cadastramento_ele_func():
    while estado.menu_eleitores == 5:
        try:
            print("\n0 - Voltar\n1 - Cadastramento de Eleitores")
            estado.menu_cadastramento_ele= int(input("Escolha a opção desejada: "))
            match estado.menu_cadastramento_ele:
                case 0:
                    print("Voltando...")
                    el.menu_eleitores_func()
                    return
                case 1:
                    print("Cadastramento de Eleitores")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")    