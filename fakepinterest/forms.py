# Criar os formulários do site
#Essa importação é que vai permitir criar as estrutas para os formulários
from flask_wtf import FlaskForm
#Essa importação cria os campos dos formulários de "Login" e "Senha" e o botão que clica para executar o login, "FileField" - Permite o usuário enviar um arquivo
from wtforms import StringField, PasswordField, SubmitField, FileField
#Importando os validators
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
#DataRequired - Exige que o usuário preencha um campo
#Email - Valida se o email existe ou se já está cadastrado
#Equalto - Verifica se um campo é igual ao outro, muito import no campo de senhas
#Length - Exige um número minimo de caracteres que foi definido. para o usuário
# ValidationError - Quando der um erro ele vai exibir a mensagem "ValidationError", para o usuário
from fakepinterest.models import Usuario


#Sobre os validators, é preciso passar uma lista dos validators que será necessário aplicar para aquele campo
class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email(message='')])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("Usuário não encontrado, crie uma conta.")

    def validata_senha(self, senha, usuario):
        usuario = Usuario.query.filter_by(email=email.data).first()
        senha = senha.data
        if usuario.senha.encode("utf-8") != senha:
            raise ValidationError("Usuário ou senha inválidos")


class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6, 20)])
    confirma_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha", message="As Senhas devem corresponder")])
    botao_confirmacao = SubmitField("Criar Conta")

    #Essa função vai validar o campo de email, obs: É preciso colocar no nome da função após o "validate", o nome do campo que você quer validar
    def validate_email(self, email):
        #Fazendo uma busca no banco de dados "query" | Filtrando/Verificando na tabela se o e-mail que foi digitado no campo, é o mesmo e-mail que está no banco de dados "filter_by" | Pegando o primeiro item pois esse método cria uma lista de 1 item ".first()"
        #Passando para variável e-mail, as informações que estão dentro do campo email, "email.data".
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar.")

    def validate_username(self, username):
        usuario = Usuario.query.filter_by(username=username.data).first()
        if usuario:
            raise ValidationError("Nome de Usuário já cadastrado")


class FormFoto(FlaskForm):
    foto = FileField("Foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")