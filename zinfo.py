import mysql
import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()
# DADOS DO USUARIO
class User:
    def __init__(self, nome, idade, cargo, empresa, salario, meta, economiaMensal, poupanca):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.empresa = empresa
        self.salario = float(salario)
        self.meta = float(meta)
        self.economiaMensal = float(economiaMensal)
        self.poupanca = float(poupanca)
        self.mesesRestantes = round((self.meta) - self.poupanca) / self.economiaMensal

    def __str__(self):
        return (f"Nome: {self.nome},\n"
            f"Idade: {self.idade},\n"
            f"Cargo: {self.cargo},\n"
            f"Empresa: {self.empresa},\n"
            f"Salário: R${self.salario:.2f},\n"
            f"Meta: R${self.meta:.2f},\n"
            f"Economia Mensal: R${self.economiaMensal:.2f},\n"
            f"Poupança: R${self.poupanca:.2f},\n"
            f"Meses Restantes: {self.mesesRestantes}")



# FUNÇÃO PARA ADICIONAR INFORMAÇÕES NO MySQL
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
                        user.salario,
                        user.meta,
                        user.economiaMensal,
                        user.poupanca,
                        user.mesesRestantes)
                
                cursor.execute(comando, dados)

                connection.commit()

                print("Adicionado a Meta")

    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")


#solicitando dados do usuario
def userInfoRequest():
    nome = input("Nome: \n")
    idade = input("Idade: \n")
    cargo = input("Cargo: \n")
    empresa = input("Empresa:\n")
    salario = input("Salário: R$\n")
    meta = input("Quanto pretende juntar?\n")
    economiaMensal = input("Quanto costuma guardar por mês?\n")
    poupanca = input("Quanto você já possui? \n")
    
    user = User(nome, idade, cargo, empresa, salario, meta, economiaMensal, poupanca)
    
    return user;