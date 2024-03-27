README - Réplica do Pinterest
Este projeto é uma réplica simplificada do Pinterest, desenvolvido com Python e Flask. Ele permite aos usuários criar uma conta, fazer login, postar fotos em seus perfis, navegar pelo feed e visualizar fotos de outros usuários.

Funcionalidades
Cadastro de Usuário: Os usuários podem criar uma conta fornecendo informações básicas como nome de usuário, senha e e-mail.

Login: Os usuários podem fazer login em suas contas usando seu nome de usuário e senha.

Postagem de Fotos: Os usuários podem postar fotos em seus perfis para compartilhar com outros usuários.

Navegação pelo Feed: Os usuários podem navegar pelo feed para ver as fotos postadas por outros usuários.

Visualização de Fotos de Outros Usuários: Os usuários podem visualizar as fotos postadas por outros usuários ao acessar seus perfis.

Como Executar o Projeto
Para executar este projeto localmente, siga estas etapas:

Clone o Repositório: Clone este repositório em sua máquina local usando o seguinte comando:

git clone https://github.com/JoaoRibeiro01/FakePinterest.git
Instale as Dependências: Navegue até o diretório raiz do projeto e instale as dependências necessárias usando o seguinte comando:

pip install -r requirements.txt
Configuração do Banco de Dados: Configure o banco de dados de acordo com as instruções fornecidas no arquivo de configuração.

Execute o Aplicativo: No terminal, execute o seguinte comando para iniciar o servidor Flask:

python app.py
Acesse o Aplicativo: Abra um navegador da web e acesse o aplicativo digitando o seguinte URL na barra de endereço:

http://localhost:5000

Tecnologias Utilizadas:
    Python: Linguagem de programação principal.
    Flask: Framework web utilizado para construir a aplicação.
    Banco de Dados: SQLite,SQLAlchemy
    Autenticação: Flask-Security para gerenciamento de autenticação e autorização, utilizando o bcrypt para criptografia de senha.

Contribuição:
    Contribuições são bem-vindas! Se você deseja contribuir para este projeto, sinta-se à vontade para enviar pull requests ou abrir issues relatando problemas ou sugestões de melhorias.

Licença:
    Este projeto está licenciado sob a Licença MIT. Sinta-se livre para usar, modificar e distribuir o código conforme necessário.