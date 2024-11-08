from users import *



def checkUser(userIn):
    users = usersList()
    for user in users:
        if user.nome == userIn:
            return True
    else:
        print("Usuario não encontrado")


# FUNÇÕES PARA ADICIONAR, EXCLUIR, ATUALIZAR E VISUALIZAR INFORMAÇÕES NO MySQL 
def adicionar(user: User):
    comando = f"""
    INSERT INTO meta (nome, idade, cargo, empresa, salario, meta, economiaMensal, poupanca, mesesRestantes)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    try:
        with mysql.connector.connect(
            host= os.environ.get("MYSQL_HOST"),
            user= os.environ.get("MYSQL_USER"),
            passwd= os.environ.get("MYSQL_PASS"),
            database= os.environ.get("MYSQL_DB")
        ) as connection:
            with connection.cursor() as cursor:

                dados = (user.nome,
                        user.idade,
                        user.cargo,     
                        user.empresa,
                        user.renda,
                        user.meta,
                        user.economiaMensal,
                        user.poupanca,
                        user.mesesRestantes)
                
                cursor.execute(comando, dados)

                connection.commit()

                print("Adicionado a Meta")

    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")



def deletar():
    user = input("Excluir usuário: ")
    comando = """
    DELETE FROM meta WHERE nome = %s;
    """
    try:
        with mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST"),
            user=os.environ.get("MYSQL_USER"),
            passwd=os.environ.get("MYSQL_PASS"),
            database=os.environ.get("MYSQL_DB")
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(comando, (user,))
                connection.commit()

                if cursor.rowcount > 0:
                    print(f"{user} foi removido.")
                else:
                    print(f"Não foi possivel excluir {user}.")
                
    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")

    

def visualizar():
    print("O que deseja vizualizar?")
    escolha = input("1 - VISUALIZAR TUDO\n2 - VISUALIZAR APENAS 1 USUARIO\n3 - CANCELAR\n")
    try:
        if escolha == "1":
            users = usersList()
            for user in users:
                print(user, "\n")
        elif escolha == "2": 
            users = usersList()
            nomes = []
            for user in users:
                nomes.append(user.nome)
            userEscolhido = input("USUARIO: ").capitalize()
            if userEscolhido in nomes:
                for user in users:
                    if user.nome == userEscolhido:
                        print(user)
            else:
                print(f"{userEscolhido} não foi encontrado.")
        elif escolha == "3":
            print("Cancelando..")                 
            return            
    except:
        print("Digite um valor válido.")
    


def atualizar():
    userUpdate = input("Qual usuário você deseja alterar? ").capitalize()
    while not checkUser(userUpdate):
        print("Usuário não encontrado.")
        userUpdate = input("Qual usuário você deseja alterar? ").capitalize()

    campos = ["nome", "idade", "cargo", "empresa", "salario", "meta", "economiaMensal", "poupanca"]

    print("Escolha a informação que deseja alterar?")
    escolha = input("\n1. Idade\n2. Cargo\n3. Empresa\n4. Salário\n5. Meta\n6. Economia Mensal\n7. Poupança\n")
    while escolha not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Campo não encontrado.")
        escolha = input("\n1. Idade\n2. Cargo\n3. Empresa\n4. Salário\n5. Meta\n6. Economia Mensal\n7. Poupança\n")

    i = int(escolha) 
    campo = campos[i]

    if i in [1, 4, 5, 6, 7]:
        alter = input(f"Do campo {campo}, qual será o novo valor?\nR: ")
        while not validarNUM(alter):
            print("Insira um valor válido.")
            alter = input(f"Do campo {campo}, qual será o novo valor?\nR: ")
        alter = float(alter)  
    elif i in [2, 3]: 
        alter = input(f"Do campo {campo}, qual será o novo valor?\nR: ")
        while not validarSTR(alter):
            print("Use apenas caracteres permitidos.")
            alter = input(f"Do campo {campo}, qual será o novo valor?\nR: ")

    # Formatação do comando SQL
    comando = f"""
        UPDATE meta
        SET {campo} = %s
        WHERE nome = %s;
    """
    try:
        with mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST"),
            user=os.environ.get("MYSQL_USER"),
            passwd=os.environ.get("MYSQL_PASS"),
            database=os.environ.get("MYSQL_DB")
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(comando, (alter, userUpdate))

                connection.commit()
                print(f"{campo} de {userUpdate} foi alterado.")

    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")

# SOLICITANDO NECESSIDADE DO USUÁRIO
def escolha():
    print("Seja bem vindo ao Meta!!\nO que deseja?\n")
    comando = input(" 'I' para INSERIR USUÁRIO\n 'D' para DELETAR USUÁRIO\n 'A' para ATUALIZAR INFORMAÇÕES\n 'V' para VISUALIZAR INFORMAÇÔES\nR:")

    while not comando in ["i", "d", "a", "v"]:
        print()
        comando = input("Comando invalido. Digite uma das opções a seguir.\n" + " 'I' para INSERIR USUÁRIO\n 'D' para DELETAR USUÁRIO\n 'A' para ATUALIZAR INFORMAÇÕES\n 'V' para VISUALIZAR INFORMAÇÔES\nR:")
    
    comando = comando.lower()
    if comando == "i":
        user = userInfoRequest()
        adicionar(user)
    elif comando == "d":
        deletar()
    elif comando == "v":
        visualizar()
    else:
        atualizar()
        
        
        

