import psycopg2

# Estabelecer a conexão com o banco de dado
'''
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1244"
) '''

conn = psycopg2.connect(
    host="bubble.db.elephantsql.com",
    database="hrorkafw",
    user="hrorkafw",
    password="OFqWGZvmdxiUwI7xekUdIAXkPHBJLS5D"
)


'''
# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Executar uma consulta
cursor.execute("INSERT INTO intencoes (intencao,enunciados) VALUES ('nome intencao', 'teste,teste,teste')")
conn.commit()

# Recuperar os resultados da consulta
#results = cursor.fetchall()

# Exibir os resultados
#for row in results:
    #print(row)

# Fechar o cursor e a conexão
cursor.close()
conn.close()'''
