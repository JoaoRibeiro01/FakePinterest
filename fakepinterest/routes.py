# Criar as rotas do site (os links)
from flask import render_template, url_for, redirect
from fakepinterest import app, database, bcrypt
#Essa importação exige que a pessoa tenha um login na plataforma, para abrir outras rotas além da homepage que é a rota padrão inicial no primeiro momento em que a pessoa vai entrar no site.
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormLogin, FormCriarConta, FormFoto
from fakepinterest.models import Usuario, Post
import os
#Importação para deixar o nome de um arquivo seguro
from werkzeug.utils import secure_filename

#Como essa rota-link nela existe um formulário que possui o method='POST', então aqui, precisamos definir dentro da rota, methdos=['GET', 'POST']
@app.route("/", methods=['GET', 'POST'])
def homepage():      #Passando para a função da rota principal o formulário de login
    formulario_login = FormLogin()
    if formulario_login.validate_on_submit():
        #Encontrando/Verificando o usuário no banco de dados
        usuario = Usuario.query.filter_by(email=formulario_login.email.data).first()
        # Verificando se a senha do usuário está certa ou não.
        # São passados 2 argumentos, pega a senha verdadeira e compara com a senha que se encontra dentro do campo de senha do formulário, caso seja verdeira, permite o login.
        if usuario and bcrypt.check_password_hash(usuario.senha, formulario_login.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("homepage.html", form=formulario_login)
    #form.csrf_token - Trava de segurança contra ataques cibernéticos. - Garante que o formulário vai ser sempre validado antes de enviar qualquer informação ao banco de dados.
    #form.nome_do_campo.label() Poe o nome do titulo do campo no próprio campo

@app.route("/criar-conta", methods=['GET', 'POST'])
def criarconta():      #Passando para a rota de criar conta, o formulário de criar conta
    formulario_criarconta = FormCriarConta()
    #Faz uma validação do formulário, após o usuário de um "Submit" no formulário.
    if formulario_criarconta.validate_on_submit():
        #A variável "senha" Está recebendo com valor uma criptografia de senha ou seja, se o usuario der submit no formulário, sua senha vai ser criptografada
        #Outra funcionalidade poderia ser "bcrypt.check_password_hash()", Essa função consegue verificar se a senha criptografada é realmente a senha do usuário.
        senha = bcrypt.generate_password_hash(formulario_criarconta.senha.data)
        usuario = Usuario(username=formulario_criarconta.username.data,
                          email= formulario_criarconta.email.data , senha= senha )

        #database.session.add(usuario) = Salvando os dados do usuário dentro do banco de dados.
        database.session.add(usuario)
        #database.session.commit() = Salvando as alterações feitas no banco de dados
        database.session.commit()
        login_user(usuario) #Faz o login automaticamente o login do usuário ao criar conta, "remember=True" : Deixa gravado o login do usuário
        #redirect : Como o próprio nome diz, o usuário é redirecionado para uma a página especificada após realizar a criação da conta
        return redirect(url_for("perfil", id_usuario= usuario.id))
    return render_template("criarconta.html", form=formulario_criarconta)


#login_required - Diz que essa rota só pode ser acessada após o usuário estar logado.
@app.route("/perfil/<id_usuario>", methods=['GET', 'POST'])
@login_required
def perfil(id_usuario):
    #Esse parametro permite o site receber um arquivo e não ocorrer nenhum tipo de erro enctype="multipart/form-data"

    #Quando o usuário tiver olhando o próprio perfil, eu vou passar o formulário de enviar foto com valor, caso ele esteja olhando o perfil de outro usuário o formulário vai receber None.

    #Essa condição foi feita para diferenciar os usuários.
    if int(id_usuario) == int(current_user.id):
        form_foto = FormFoto()
        #O usuário ta vendo o perfil dele
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            #Deixando o arquivo seguro
            nome_seguro = secure_filename(arquivo.filename)
            #Salvar o arquivo na pasta fotos_posts
                        #Pegando o local onde o esse arquivo está com o codigo abaixo
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   app.config["UPLOAD_FOLDER"], nome_seguro)
            arquivo.save(caminho)
            #Registrar arquivo no banco de dados
            foto = Post(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto)
            database.session.commit()
        return render_template("perfil.html", usuario=current_user, form=form_foto)
    else:
        #O usuário aqui está vendo o perfil de outro usuário
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario, form=None)

#Rota que vai fazer o logout do usuário e redireciona-lo para a tela de login
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/feed")
@login_required
def feed():
    #Ordenando toda a consulta no banco de dados baseado na data "order_by" | Pegando todos os itens dessa consulta ".all()" | Se quiser limitar q qtde de fotos que aparece pro usuário é só fazer ".all()[100]"
    #"desc()" - Ordena do menor para maior, baseado na data.
    fotos = Post.query.order_by(Post.data_criacao.desc()).all()
    return render_template("feed.html", fotos=fotos)