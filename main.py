'''
Esse codigo ainda será atualizado, está em teste.

-- Atualizações previstas:
.Mais verificações para desempenho;
.Otimizar todo o codigo.

'''
import mysql.connector
from zinfo import userInfoRequest, User, add, userInfo, users
 # type: ignore
import os



while True:
    os.system("cls")
    user = userInfoRequest()
    parar = input("Deseja adicionar mais algum usuário?\n 's' para SIM ou 'n' para NÃO" )
    if parar.lower() == "s":
        print(users)
        continue
    else:
        break





     
