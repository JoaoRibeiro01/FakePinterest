#Criar a estrutura do banco de dados
from fakepinterest import database, login_manager
from datetime import datetime
#UserMixin - Diz qual a classe que vai gerenciar o sistema de login
from flask_login import UserMixin

#Essa função recebe um o id do usuario e retorna o quem é esse usuario - essa função é obrigatória dentro de uma estrutura de login
#Ação de função: Buscando uma informação dentro do banco de dados "nome_tabela.query", um exemplo é o "filter_by" que filtra os usuarios.
#get : Encontrando o usuário apartir de uma informação já obtida, exemplo, um usuário que temos o id
@login_manager.user_loader # Com esse decorator estamos "dizendo pra função" que ela carrega um usuário baseado no id.
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))
#Criando as colunas do banco de dados
class Usuario(database.Model, UserMixin):
    #Criando o id Definindo o tipo, e chamando o atributo primary key, que o torna o id de cada usuario exclusivo
    id = database.Column(database.Integer, primary_key=True)
    #Criando a coluna username, definindo o tipo, dizendo que não pode ser nulo e 2 usuários nao podem ter o mesmo nome
    username = database.Column(database.String, nullable=False, unique=True)
    #Criando a coluna email, com as mesmas regras da anterior
    email = database.Column(database.String, nullable=False, unique=True)
    #Criando uma senha com as mesma regras da coluna username, so que as senhas não vao ter valores unicos
    senha = database.Column(database.String, nullable=False)
    #Criando uma relação entre a tabela Usuario e a tabela Post, backref: backref um atributo da tabela criado para especificar a outra parte da relação entre as classes Usuário e Post, no seu caso é a tabela Instrumento.
    #Se torna muito útil na hora de fazer querys no relacionamento, pois a partir dessa declaração, você poderá fazer uma query como Post.usuarios, para saber quais usuários estão associados a um determinado post.
    #lazy = True - Otimiza como a informação é puxada do banco de dados, fazendo buscas no banco de dados de forma eficiente
    fotos = database.relationship("Post", backref="usuario", lazy=True)

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    #Coluna imagem, aqui ela vai se relacionar com a pasta "static" e carregar a imagem de com o nome que está dentro do banco de dados
    imagem = database.Column(database.String, default="default.png")
    #Criando coluna de data e definindo um horário (o momento em que foi criado) padrão em formato internacional
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    #Criando a coluna que vai concretizar a relação entre as duas classes/tabelas. Ou seja o id do usuario
    id_usuario = database.Column(database.Integer, database.ForeignKey("usuario.id"), nullable=False)