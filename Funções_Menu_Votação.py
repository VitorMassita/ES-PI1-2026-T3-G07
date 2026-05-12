#Funções menus Votação
import CondicoesGlobais as estado
from datetime import datetime
import DATABASE as db

#Resgistrando o LOG de votação
def registrar_log(mensagem):
    with open("logs.txt", "a", encoding="utf-8") as arquivo: #Abrir arquivo logs.txt na UTF-8
        datahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S") #Usando o import para salvar a data certa do computador convertendo em strings (STRF)
        arquivo.write(f"[{datahora}] {mensagem}\n") #Escrevendo no arquivo


#Funcão para realizar votação, onde o usuário digita o número do candidato e o voto é registrado
def realizar_votacao_func():
    #Verificar se o sistema está aberto
    if estado.sistema_votacao_aberto == False:
        print("Sistema de votação fechado! Você não pode votar agora.")
    else:
        #Conectando ao banco de dados
        db.conecta_mysql()

        #solicitar o login do eleitor - feito no cadastramento
        titulo_eleitor = input("Digite o seu Título Eleitoral para votar: ")
        senha_eleitor = input("Digite a sua senha para votar: ")

        try: 
            #verificar se o título eleitoral e a senha estão corretos
            #Query para verificar o login do eleitor e ser jogada no MySQL
            query_login = """
            SELECT * FROM eleitores
            WHERE titulo_ele = %s
            AND senha_ele = %s
            """

            #Verificando login
            estado.cursor.execute(query_login, (titulo_eleitor, senha_eleitor))
            eleitor = estado.cursor.fetchone()

            if eleitor == None:
                print("Título ou senha inválidos!")
                registrar_log(f"Tentativa de login inválido!")
                return # Para a função de executar
            
            #Verificando se o eleitor já votou
            elif( eleitor["número da coluna True/False - se votou ou não"] == 1):
                print("Este eleitor já votou")
                registrar_log("Tentativa de voto duplo!")
                return
            
            else:
                print("\nLogin realizado com sucesso!")
                registrar_log(f"Login Realizado Por: Título: {titulo_eleitor}")

                #mostrando os candidatos usando FOR
                print("\n===== CANDIDATOS =====")

                query_candidatos = "SELECT * FROM candidatos" #Seleciona todos os candidatos
                estado.cursor.execute(query_candidatos)
                candidatos = estado.cursor.fetchall()

                for candidato in candidatos:
                    print(f"Número: {candidato[0]} | Nome: {candidato[1]}") # Ordenando os candidatos do MySQL por nome e número

                voto = input("\nDigite o número do candidato: ")               

                #Verificando se o candidato existe
                #Query para selecionar todos os candidatos do MySQL via número
                query_validacao = """
                SELECT * FROM candidatos
                WHERE num (Alterar se for preciso) = %s
                """

                
                estado.cursor.execute(query_validacao, (voto,))

                #salvando em uma variável
                candidato_existe = estado.cursor.fetchone()

                if candidato_existe == None:
                    print("Candidato não encontrado!")
                    registrar_log(f"Tentativa de voto inválido | Título: {titulo_eleitor}")
                    return
                
                #Inserindo o voto no MySQL
                #Query de Update para inserir o voto na tabela votos
                query_update = "Aqui deve se inserir o código UPDATE em MySQL para alterar o campo do eleitor se votou ou não para True (Altere para nosso banco)"
                estado.cursor.execute(query_update, (titulo_eleitor,))

                # Salvando alterações no banco
                estado.connection.commit()
                print("Voto registrado com sucesso!")
                #Registrando no Log de votações
                registrar_log(f"Voto registrado | Título: {titulo_eleitor} | Candidato: {voto}")

        #Fazendo o except para caso haja erros durante o processo
        except Exception as erro: #Ao usar "AS ERRO" a causa do erro é salva em uma variável
            print(f"Erro durante votação: {erro}")

            #Registrando erro no log
            registrar_log(f"Erro durante votação: {erro}")

        finally: #O finally é a terceira causa do TRY e serve para executar o ultimo comando quando acaba o bloco que deseja executar
            #serve para executar um bloco de código independentemente de dar erro ou não.
            #Fechando a conexão com o banco de dados
            estado.cursor.close()
            estado.connection.close()



"""Menu Votação"""
def menu_votacao_func():
    while estado.menu_principal == 2:
        try:
            print("0 - Voltar \n1 - Votação \n2 - Auditoria \n3 - Resultado")
            estado.menu_votacao= int(input("Escolha a opção desejada: "))
            match estado.menu_votacao:
                case 0:
                    import menu_principal as main
                    print("\n Voltando... ")
                    return(main.menu_principal_func())
                case 1:
                    print("Abir Sistema de Votação")
                    menu_sistem_votacao_func()
                    break
                case 2:
                    print("Auditoria")
                    menu_auditoria_func()
                    break
                case 3:
                    print("Resultado")
                    menu_resultado_func()
                    break
                case _:
                    print("Opção Invalida, tente novamente.")
        except ValueError:
            print("Entrada Inválida. Digite um Numero")


"""Auditoria"""
def menu_auditoria_func():
    while estado.menu_votacao == 2:
        try:
            print("\n0 - Voltar\n1 - Logs \n2 - Protocolo de Votação")
            estado.menu_auditoria= int(input("Escolha a opção desejada: "))
            match estado.menu_auditoria:
                case 0:
                    print("\nVoltando...")
                    return(menu_votacao_func())
                case 1:
                    print("Logs")

                case 2:
                    print("Protocolo de Votação")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

"""Sistema De Votação"""
def menu_sistem_votacao_func():
    
    while estado.menu_votacao == 1:
        try:
            print("\n0 - Voltar\n1 - Comecar Votação\n2 - Fechar Sistema de Votação")
            menu_sistem_votacao= int(input("Escolha a opção desejada: "))
            match menu_sistem_votacao:
                case 0:
                    print("\nVoltando...")
                    return(menu_votacao_func())
                case 1:
                    if (estado.sistema_votacao_aberto == True):
                        print("Sistema de votação já aberto!")
                    else:
                        #Variável global de controle, para não ter erros - Isso vai controlar se a urna está aberta.
                        estado.sistema_votacao_aberto == False

                        #Chamando a função pra registrar no logs.txt
                        registrar_log("Sistema de votação aberto!")
                        print("Sistema de votação aberto com sucesso!")
                        
                case 2:
                        #Variável global de controle, para não ter erros 
                        estado.sistema_votacao_aberto = False

                        #Registrando log
                        registrar_log("Sistema de votação encerrado")
                        print("Encerrando Sistema de Votação...")

                        import menu_principal as main
                        return(main.menu_principal_func())
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

""""Menu Resultado"""
def menu_resultado_func():

    while estado.menu_votacao == 3:
        try:
            print("\n0 - Voltar\n1 - Boletim de Urna")
            estado.menu_resultado= int(input("Escolha a opção desejada: "))
            match estado.menu_resultado:
                case 0:
                    print("\nVoltando...")
                    return(menu_votacao_func())
                case 1:
                    print("Boletim de Urna")
                    break   
                case _:
                    print("Opção inválida, tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

