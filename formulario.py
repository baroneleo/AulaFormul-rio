import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('formulario.html')

# Rota de inserção de dados no Banco

@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome'] # Lê do formulário o valor nome
    cpf = request.form['cpf'] # Lê do formulário o cpf
    endereco = request.form['endereco'] # Lê do formulário o e-mail
    senha = request.form['senha'] # Obtem do formulário a senha
    if nome and cpf and endereco and senha: # verifica se o valor de nenhum for nulo
        conn = mysql.connect() # Estabelece a conexão com mysql
        cursor = conn.cursor() # Cria um cursor de uma sessão de comunicação com o banco
        cursor.execute('insert into dados_user (user_nome, user_cpf, user_endereco, user_password) VALUES (%s, %s, %s, %s)', (nome, cpf, endereco, senha)) # Cria o comando "insert" pra inserir dados no banco" referenciando os dados com as variáveis (%s é passar parametro do tipo string)
        conn.commit() # Executa o comando
    return render_template('formulario.html') # Faz a volta da comunicação

# Rota de resposta da pesquisa no banco

@app.route('/listar', methods= ['POST', 'GET'])
def listar():
    conn = mysql.connect() # Estabelece a conexão com o banco de dados
    cursor = conn.cursor() # Cria a sessão por meio de um cursor
    conn.execute('select user_nome, user_cpf, user_endereco from dados_user') # Cria o comando "select" para realizar busca de dados na tabela informada -> (dados_user)
    data = cursor.fetchall() # Faz o comando "fetchall" para fazer a recuperação de dados / Atribuindo o resultado pra variável "data"
    conn.commit() # Executa o comando
    return render_template('lista.html', datas = data) # Retorna pro arquivo chamado "lista.html" na pasta de templates / com a variável data com o nome datas que é o nome que ela está sendo referenciado pelo jinja no arquivo lista.html

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5008))
    app.run(host='0.0.0.0', port = port)