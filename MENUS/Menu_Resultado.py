"""Resultado"""
import menu_principal as main
import Menu_Votacao as vt

def menu_resultado_func():
    global menu_resultado
    while main.menu_votacao == 3:
        try:
            print("\n0 - Voltar\n1 - Boletim de Urna")
            menu_resultado= int(input("Escolha a opção desejada: "))
            match menu_resultado:
                case 0:
                    print("Voltando...")
                    return(vt.menu_votacao_func())
                case 1:
                    print("Boletim de Urna")
                    break   
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")