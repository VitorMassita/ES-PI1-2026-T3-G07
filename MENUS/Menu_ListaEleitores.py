import CondicoesGlobais as estado
import Menu_Eleitores as el

def menu_listaeleitores_func():
    while estado.menu_eleitores == 1:
        try:
            print("\n0 - Voltar\n1 - Mostrar a lista de Eleitores")
            estado.menu_listaeleitores= int(input("Escolha a opção desejada: "))
            match estado.menu_listaeleitores:
                case 0:
                    print("Voltando...")
                    el.menu_eleitores_func()
                    return
                case 1:
                    print("Mostrar a lista de Eleitores")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")