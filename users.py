import mysql
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# DADOS DO USUARIO
class User:
    def __init__(self, nome, idade, cargo, empresa, renda, meta, economiaMensal, poupanca):
        self.nome = nome.capitalize()
        self.idade = idade
        self.cargo = cargo
        self.empresa = empresa
        self.renda = float(renda)
        self.meta = float(meta)
        self.economiaMensal = float(economiaMensal)
        self.poupanca = float(poupanca)
        self.mesesRestantes = round((self.meta) - self.poupanca) / self.economiaMensal

    def __str__(self):
        return (f"Nome: {self.nome},\n"
            f"Idade: {self.idade},\n"
            f"Cargo: {self.cargo},\n"
            f"Empresa: {self.empresa},\n"
            f"Salário: R${self.renda:.2f},\n"
            f"Meta: R${self.meta:.2f},\n"
            f"Economia Mensal: R${self.economiaMensal:.2f},\n"
            f"Poupança: R${self.poupanca:.2f},\n"
            f"Meses Restantes: {self.mesesRestantes}")


# Lista de Usuarios
def usersList():
    users = []
    try:
        with mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST"),
            user=os.environ.get("MYSQL_USER"),
            passwd=os.environ.get("MYSQL_PASS"),
            database=os.environ.get("MYSQL_DB")
        ) as connection:
            with connection.cursor() as cursor:
                comando = "SELECT nome, idade, cargo, empresa, salario, meta, economiaMensal, poupanca FROM meta"
                cursor.execute(comando)

                resultados = cursor.fetchall()

                for row in resultados:
                    nome, idade, cargo, empresa, salario, meta, economiaMensal, poupanca = row
                    user = User(nome, idade, cargo, empresa, salario, meta, economiaMensal, poupanca)
                    users.append(user)
    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")

    return users


users = usersList()
# for user in users:
#     print(user, "\n")



#Adicionando usuario em uma lista.
def userInfo(users, user):
    users.append(user)
    print(f"{user.nome} listado.")



#Validar STR
def validarSTR(string):
    if all(i.isalpha() or i.isspace() for i in string): 
        return True
    else:
        return False



#Validar NUM
def validarNUM(number):
    if len(number) > 2:
        try:
            number = float(number)
            return number > 0
        except ValueError:
            print("Digite o numero corretamente.")
    else:
        try:
            number = int(number)
            return number
        except ValueError:
            print("Digite o numero corretamente.")
    


# Criar usuario
def userInfoRequest():
    # nome
    nome = input("Nome: \nR: ")  
    while not validarSTR(nome):
        print("Por favor, insira um NOME VALIDO.")
        nome = input("Nome: \n")

    #idade
    idade = input("Idade: \nR: ")
    while not validarNUM(idade):
        print(" Por favor, insira uma idade válida.")
        idade = input("Idade: \n")
    

    #empregado = True or False
    empregado = input("Está trabalhando atualmente? 's' para SIM ou 'n' para NÃO\nR: ")
    while not validarSTR(nome):
        print("Por favor, insira uma resposta válida.")
        empregado = input("Está trabalhando atualmente? 's' para SIM ou 'n' para NÃO\nR: ")
        
    if empregado.lower() == "s":  
        cargo = input("Qual seu cargo?  \nR: ")
        empresa = input("Empresa:\nR: ")
    else:
        cargo = "Não possui"
        empresa = ""

    # Informações sobre renda
    renda = input("Qual a sua renda?\nR: ")

    # validação renda.
    while not validarNUM(renda):
        print(" Por favor, insira um valor válido.")
        renda = input("Qual a sua renda?\nR: ")


    # Informações sobre o objetivo (meta).
    meta = input("Quanto pretende juntar?\nR: ")

    # validação meta.
    while not validarNUM(meta):
        print(" Por favor, insira um valor válido.")
        meta = input("Quanto pretende juntar?\nR: ")


    # Informações sobre a economia mensal do usuário.
    economiaMensal = input("Quanto costuma guardar por mês?\nR: ")

    # validação economia mensal.
    while not validarNUM(economiaMensal):
        print(" Por favor, insira um valor válido.")
        economiaMensal = input("Quanto costuma guardar por mês?\nR: ")


    # Informação sobre quanto o usuário já possui.
    poupanca = input("Quanto você já possui? \nR: ")

    # validação poupanca.
    if poupanca != 0:
        while not validarNUM(poupanca):
            print(" Por favor, insira um valor válido.")
            poupanca = input("Quanto você já possui? \nR: ")
    

    # Tentavida de criação de usuario, utilizando try catch para captar possiveis erros.
    try:
        user = User(nome, idade, cargo, empresa, renda, meta, economiaMensal, poupanca)

        userInfo(users, user)
        return user
    except ValueError:
        return None 
    