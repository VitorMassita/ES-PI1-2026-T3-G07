import CondicoesGlobais as estado
import Validações as v
import DATABASE as db

def cadastro_func():
    print("Para realizar o cadastro, por favor, digite o seu Nome, Sobrenome, CPF, Titulo Eleitoral.\nSua Senha será gerada automaticamente.\n")
    estado.nome = str(input("Digite o seu Nome Completo: "))
    try:
        while len(estado.nome) < 3:
            print("Nome inválido. O nome deve conter pelo menos 3 caracteres.")
            estado.nome = str(input("Digite o seu Nome Completo: "))
    except ValueError:
        print("Nome inválido. O nome deve conter pelo menos 3 caracteres.")


    estado.cpf = input("Digite o seu CPF: ")
    try:
        while len(estado.cpf) != 11:
            print("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")
            estado.cpf = input("Digite o seu CPF: ")
    except ValueError:
        print("CPF inválido. O CPF deve conter exatamente 11 dígitos numéricos.")
    v.validacao_cpf_func(estado.cpf)


    estado.teleitor = input("Digite o seu Titulo Eleitoral: ")
    try:
        while len(estado.teleitor) != 12:
            print("Titulo Eleitor inválido. O Titulo Eleitor deve conter exatamente 12 dígitos numéricos.")
            estado.teleitor = input("Digite o seu Titulo Eleitoral: ")
    except ValueError:
        print("Titulo Eleitor inválido. O Titulo Eleitor deve conter exatamente 12 dígitos numéricos.")
    v.validacao_tituloeleitor_func(estado.teleitor)

    estado.senha = input("Digite a sua Senha: ")

    db.conecta_mysql()
    estado.cadastro = "INSERT INTO eleitores (nome_ele, cpf_ele, titulo_ele, senha_ele) VALUES (%s, %s, %s, %s)"
    estado.valores = (estado.nome, estado.cpf, estado.teleitor, estado.senha)
    estado.cursor.execute(estado.cadastro, estado.valores)
    estado.connection.commit()
    estado.cursor.close()
    estado.connection.close()
    print("Cadastro realizado com sucesso!")