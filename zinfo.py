import mysql
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# DADOS DO USUARIO
class User:
    def __init__(self, nome, idade, cargo, empresa, renda, meta, economiaMensal, poupanca):
        self.nome = nome
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

#Lista de usuarios
users = []

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
            return number > 0
        except ValueError:
            print("Digite o numero corretamente.")
    

#solicitando dados do usuario.
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

    while not validarSTR(empregado):
        print("Por favor, insira caracteres válidos.")
        empregado = input("Está trabalhando atualmente? 's' para SIM ou 'n' para NÃO\nR: ")
        if empregado.lower() == "s":  
            cargo = input("Qual seu cargo?  \nR: ")
            empresa = input("Empresa:\nR: ")
        else:
            cargo = ""
            empresa = ""
    

    renda = input("Qual a sua renda?\nR: ")
    meta = input("Quanto pretende juntar?\nR: ")
    economiaMensal = input("Quanto costuma guardar por mês?\nR: ")
    poupanca = input("Quanto você já possui? \nR: ")

    try:
        renda = float(renda)
        meta = float(meta)
        economiaMensal = float(economiaMensal)
        poupanca = float(poupanca)
        user = User(nome, idade, cargo, empresa, renda, meta, economiaMensal, poupanca)

        userInfo(users, user)
        return user
    except ValueError:
        print("Erro: Por favor, insira valores validos em campos númericos.")
        return None 
    
#########################################################################

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

#########################################################################