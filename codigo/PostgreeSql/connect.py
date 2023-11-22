import psycopg2

# Estabelecer a conexão com o banco de dado
'''
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1244"
) '''

'''conn = psycopg2.connect(
    host="bubble.db.elephantsql.com",
    database="hrorkafw",
    user="hrorkafw",
    password="OFqWGZvmdxiUwI7xekUdIAXkPHBJLS5D"
)
'''
def conectarBanco():
    conn = psycopg2.connect(
        host="4.180.124.44",
        database="DB_AI",
        user="root",
        password="@‌AI+UNC23102023"
    )
    return conn
