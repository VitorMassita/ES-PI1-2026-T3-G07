import CondicoesGlobais as estado
import Menu_Eleitores as el 

def menu_buscaeleitores_func():
    while estado.menu_eleitores == 3:
        try:
            print("\n0 - Voltar\n1 - Buscar Eleitores")
            estado.menu_buscaeleitores= int(input("Escolha a opção desejada: "))
            match estado.menu_buscaeleitores:
                case 0:
                    print("Voltando...")
                    el.menu_eleitores_func()
                    return
                case 1:
                    print("Buscar Eleitores")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")