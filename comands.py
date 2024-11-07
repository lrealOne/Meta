from users import *

# FUNÇÃO PARA ADICIONAR INFORMAÇÕES NO MySQL (C)
def add(user: User):
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



def delete():
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

    
# SOLICITANDO NECESSIDADE DO USUÁRIO
def escolha():
    print("Seja bem vindo ao Meta!!\nO que deseja?\n")
    comando = input(" 'I' para INSERIR USUÁRIO\n 'D' para DELETAR USUÁRIO\n 'A' para ATUALIZAR INFORMAÇÕES\n 'V' para VISUALIZAR INFORMAÇÔES\nR:")

    while not comando in ["i", "d", "a", "l"]:
        print()
        comando = input("Comando invalido. Digite uma das opções a seguir.\n" + " 'I' para INSERIR USUÁRIO\n 'D' para DELETAR USUÁRIO\n 'A' para ATUALIZAR INFORMAÇÕES\n 'V' para VISUALIZAR INFORMAÇÔES\nR:")
    
    comando = comando.lower()
    if comando == "a":
        user = userInfoRequest()
        add(user)
    elif comando == "d":
        delete()
    
        
    

