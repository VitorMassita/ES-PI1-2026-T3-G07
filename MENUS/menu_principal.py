while True:
    try:
        print("\n1 - Gerenciamento \n2 - Votação")
        escolha = int(input("Escolha a opção desejada: "))
        if escolha == 1:
            print("Gerenciamento \n")
            while True:
                try:
                    print("0 - Voltar \n1 - Candidatos \n2 - Eleitores")
                    escolha = int(input("Escolha a opção desejada: "))
                    if escolha == 0: 
                        print("Voltando..." )
                        break
                    elif escolha == 1:
                        print("Candidatos \n")
                        while True:
                            try:
                                print("0 - Voltar \n1 - Edição de Dados\n2 - Cadastramento\n3 - Remoção \n4 - Busca de Candidatos \n5 - Candidatos ")
                                escolha = int(input("Escolha a opção desejada: "))
                                if escolha == 0 :
                                    print("Voltando..." )
                                elif escolha == 1:
                                    print("Edição de Dados")
                                    break    
                                elif escolha == 2:
                                    print("Cadastramento")
                                    break
                                elif escolha == 3:
                                    print("Remoção")
                                    break
                                elif escolha == 4:
                                    print("Busca de Candidatos")
                                    break
                                elif escolha == 5:
                                    print("Lista de Candidatos")
                                    break
                            except ValueError:
                                print("Entrada inválida. Digite um número.")
                    elif escolha == 2:
                        print("Eleitores")
                        break
                    else:
                        print("Opção inválida, tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")   
        elif escolha == 2:
            print("Votação")
            break
        else:
            print("Opção inválida, tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

