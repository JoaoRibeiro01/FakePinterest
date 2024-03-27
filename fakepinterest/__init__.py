from flask import Flask
#Essa importação é a que vai permitir integrar o um banco de dados dentro do flask
from flask_sqlalchemy import SQLAlchemy
#Essas importações sãos que as que vão gerenciar os logins dos usuários
from flask_login import LoginManager
#A Bcrypt em específico faz a criptografia do login
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
#Cria um database de acordo com o valor passado, nesse caso foi criado um database "sqlite".
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")  # Criando um banco de dados Virtual
#Chave de segurança que vai garantir a integridade do app
app.config["SECRET_KEY"] = "87825fbf71cf983a6991c2b12818c6d6"
#Definindo que sempre que uma que o usuário fizer o upload de uma foto, ele vai armazenar na pasta definida abaixo.
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage" #Aqui será passado qual rota que vai gerenciar o login, ou seja o link que o usuario vai fazer o login, eu poderia criar um link só pra isso, ou aproveitar um link ja existente.

from fakepinterest import routes