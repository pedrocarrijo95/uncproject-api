import autopep8

codigo = """
for i in range(5):
print(i)
"""

codigo_identado = autopep8.fix_code(codigo)

print(codigo_identado)

def func1():
    resp = ""
    for i in range(5):
        for j in range(3):
            resp += str(i)+"/"+str(j)
    for i in range (2):
        resp += " for externo: "+str(i)

    return resp

print(func1())
