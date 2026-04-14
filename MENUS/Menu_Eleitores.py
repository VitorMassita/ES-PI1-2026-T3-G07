"""Menu Eleitores"""
import CondicoesGlobais as estado
import Menu_Gerenciamento as gr
import Menu_ListaEleitores as le
import Menu_RemoveEleitores as re
import Menu_BuscaEleitores as be
import Menu_EdicaoDados_Ele as ed
import Menu_Cadastramento_Ele as ct

def menu_eleitores_func():
   
    while estado.menu_gerenciamento == 2:
        try:
            print("\n0 - Voltar\n1 - Lista de Eleitores\n2 - Remoção de Eleitores \n3 - Busca de Eleitores \n4 - Edição de Dados \n5 - Cadastramento")
            estado.menu_eleitores= int(input("Escolha a opção desejada: "))
            match estado.menu_eleitores:
                case 0:
                    print("Voltando...")
                    gr.menu_gerenciamento_func()
                    return
                case 1:
                    print("Lista de Eleitores")
                    le.menu_listaeleitores_func()
                    break
                case 2:
                    print("Remoção de Eleitores")
                    re.menu_removeeleitores_func()
                    break
                case 3 : 
                    print("Busca de Eleitores")
                    be.menu_buscaeleitores_func()
                    break
                case 4: 
                    print("Edição de Dados")
                    ed.menu_edicaodados_ele_func() 
                    break
                case 5: 
                    print("Cadastramento")
                    ct.menu_cadastramento_ele_func()
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
