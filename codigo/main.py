#Imports de outras classes
import funcoes
import variaveis
import autopep8
from UncSoftwareAPI import unc_funcs as unc
from flask_cors import CORS
from rotas_api import app  # Importe o objeto Flask e as rotas do arquivo rotas_api.py

CORS(app)
'''
cors = CORS(
    app,
    resources={r"/api/*": {"origins": "http://localhost:3000"}},
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)'''

if __name__ == '__main__':
    app.run()


        



