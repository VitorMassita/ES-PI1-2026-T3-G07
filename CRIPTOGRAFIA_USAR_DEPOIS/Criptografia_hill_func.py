# Cifra de Hill - Criptografia
# Deve-se seguir o seguinte fluxo: letras -> números -> blocos -> multiplicação -> mod 26 -> letras

#Criando uma tabela de referenção para posição das letras do alfabeto
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Passando de letra para número: usa-se o comando INDEX() que procura a posição da letra
def letra_para_numero(letra): # Dentro do parenteses está algo chamado parâmetro, algo que a função de pede que irá determinar o comportamento do código
    # Nesse caso o parâmetro pede a letra que será retornada como número
    return(alfabeto.index(letra))

#Passando um número para letra
def numero_para_letra(num):
    return (alfabeto[num % 26]) # Entre os colchetes está o comando que delimita que o número fique entre 0 e 25 (mod 26)

def multiplicar_matriz(A, Vetor): 
    #A representa a matriz chave que será utilizada
    #Vetor representa o bloco numérico em que a palavra é separada
    x = A[0][0]*Vetor[0] + A[0][1]*Vetor[1] # Aqui há a multiplicação de matrizes normal, do mesmo jeito que faz no caderno
    y = A[1][0]*Vetor[0] + A[1][1]*Vetor[1]
    return([x % 26, y % 26]) # Retorna os valores X e Y no mod 26

# Criptografando com cifra de hill
def cifra_hill(texto, A):
    # Texto = palavra a ser criptografada
    # A = matriz chave
    # Deve-se primeiro otimizar o texto, deixar padronizado
    texto = texto.replace(" ", "").upper() #Isso irá retirar todos espaços e deixar tudo em letra maiúscula

    #Após isso, deve-se verificar se o texto possui um número ímpar de caracteres
    if(len(texto) % 2 != 0):
        texto += "X" # Adiciona um X no final, mudando para PAR

    resultado = "" # String vazia para resultado

    for i in range(0, len(texto), 2): #Loop que vai de 0 até o tamanho de texto, pulando/agrupando de 2 em 2!
        bloco = [letra_para_numero(texto[i]), letra_para_numero(texto[i+1])] # Transforma o grupamento de letras em número
        cifrado = multiplicar_matriz(A, bloco) #Multiplica o bloco numérico criado pela matriz chave

        resultado += numero_para_letra(cifrado[0]) #Define o resultado como o produto da multiplicação do bloco 1
        resultado += numero_para_letra(cifrado[1]) #Define o resultado como o produto da multiplicação do bloco 2

    return(resultado) # Retorna o valor para a função deixar guardada para ser usada depois
    

#Chamando a função do jeito certo
#Essa função, se for chamada do jeito que está, não irá funcionar, pois é preciso setar o texto e a matriz chave

