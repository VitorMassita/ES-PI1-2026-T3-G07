"""Menu Votação"""
import menu_principal as main
import CondicoesGlobais as estado

def menu_votacao_func():
    while estado.menu_principal == 2:
        try:
            print("0 - Voltar \n1 - Sistema de Votação \n2 - Auditoria \n3 - Resultado")
            estado.menu_votacao= int(input("Escolha a opção desejada: "))
            match estado.menu_votacao:
                case 0:
                    print("Voltando...")
                    main.menu_principal_func()
                    return
                case 1:
                    print("Sistema de Votação")
                    main.menu_sistem_votacao_func()
                    break
                case 2:
                    print("Auditoria")
                    main.menu_auditoria_func()
                    break
                case 3:
                    print("Resultado")
                    main.menu_resultado_func()
                    break
                case _:
                    print("Opção Invalida, tente novamente.")
        except ValueError:
            print("Entrada Inválida. Digite um Numero")