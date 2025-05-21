from flask import Flask, render_template, url_for
from controllers import auth_controller
from models.user_model import Usuario
from config import SHOW_LOGS

Usuario.criar_tabelas()

app = Flask(__name__)

# Rotas de Exibição

@app.route('/')
def home():
    if SHOW_LOGS == True: print("/nFunção home ativada")
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return auth_controller.mostrar_cadastro()

# Rotas de Processamento

@app.route('/p_cadastro', methods=['POST'])
def cadastrar_usuario():
    return auth_controller.processar_cadastro()

if __name__ == '__main__':
    app.run(debug=True)