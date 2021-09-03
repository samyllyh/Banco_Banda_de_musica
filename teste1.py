# configurando para ter acesso ao bd
from unittest import case

import psycopg2
import psycopg2 as db

conn = db.connect(host='localhost', dbname='SistemaBandaMusica', user='postgres', password='190318')

host = 'localhost'
dbname = 'finalmente'
user = 'postgres'
password = '190318'

# string para repassar dados p/biblioteca
conn_string = 'host={0} user={1} dbname={2} password={3}'.format(host, user, dbname, password)
# print(conn_string)

# abrir uma conexão com o banco
conn = psycopg2.connect(conn_string)
# print('conectado')

# cursor para utilizar comandos em SQL
cursor = conn.cursor()


# esta consulta mostra o nome dos integrantes que utilizam o suporte para instrumento(sup_ins)
def consultar_suporte_instrumento():
    cursor.execute(
        "select sup_ins, nome from equipamento_suporte inner join integrante on ((integrante.cpf = equipamento_suporte.cpf) and (equipamento_suporte.sup_ins = '1') );")
    return cursor.fetchall()


# função insere novos intrumentos
def inserir_instrumento(nome_ins, afinação, marca):
    cursor.execute("insert into instrumento(nome_ins, afinação, marca) values (%s, %s,%s);",
                   (nome_ins, afinação, marca,))
    cursor.execute("SELECT * FROM instrumento;")
    return cursor.fetchall()


# função para alterar o nome dos instrumentos
def alterar_nome_instrumento(num_serie, nome_ins):
    cursor.execute("UPDATE instrumento SET nome_ins = %s WHERE num_serie = %s;", (nome_ins, num_serie,))
    cursor.execute("SELECT * FROM instrumento;")
    return cursor.fetchall()


# função para deletar um evento caso seja cancelado
def deletar_evento(chave_evento):
    cursor.execute("DELETE FROM eventos WHERE chave_evento = %s", (chave_evento,))
    cursor.execute("SELECT * FROM eventos;")
    return cursor.fetchall()


# função menu
def function1():
    print('1 - buscar')
    print('2 - inserir')
    print('3 - alterar')
    print('4 - deletar')


function1()
num = input("digite o numero que deseja")

# condições para saber oq o cliente quer
if num == '1':
    bus = consultar_suporte_instrumento()
    print(bus)
elif num == '2':
    aux1 = input("digite o nome do instrumento: ")
    aux2 = input("digite a afinação do instrumento: ")
    aux3 = input("digite o nome da marca do instrumento: ")
    bus2 = inserir_instrumento(aux1, aux2, aux3)
    print(bus2)
elif num == '3':
    aux4 = input("digite o numero de serie do instrumento: ")
    aux5 = input("digite o novo nome do instrumento: ")
    bus3 = alterar_nome_instrumento(aux4, aux5)
    print(bus3)
elif num == '4':
    aux6 = input("digite a chave do evento: ")
    bus4 = deletar_evento(aux6)
    print(bus4)
else:
    print('erro: digite um numero valido de 1 a 4')



# comandos pra atualizar e fechar o bd
conn.commit()
cursor.close()
conn.close()
