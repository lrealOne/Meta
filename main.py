'''
Esse codigo ainda será atualizado, está em teste.

-- Atualizações previstas:
.Mais verificações para desempenho;
.Otimizar todo o codigo.

'''
import mysql.connector
from users import *
from comands import *
 # type: ignore
import os

campos = ["nome", "idade", "cargo", "empresa", "salario", "meta", "economiaMensal", "poupanca"]

print("Escolha o a informação que deseja alterar?")
escolha = input("\n1. Idade\n2. Cargo\n3. Empresa\n4. Salario\n5. Renda\n 6. Saldo Mensal\n 7. Poupança")
while not escolha in ['1', '2', '3', '4', '5', '6', '7']:
    print("Campo não encontrado..")
    escolha = input("\n1. Idade\n2. Cargo\n3. Empresa\n4. Salario\n5. Renda\n 6. Saldo Mensal\n 7. Poupança")

i = int(escolha)
campo = campos[i]
print(campo)
comando = """
        UPDATE meta
        SET {campo} = %s
        WHERE nome = %s;
    """





     
