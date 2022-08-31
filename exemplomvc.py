from crypt import methods
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
    return render_template('exemplomvc.html')

@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['Seu Nome']
    email = request.form['email']
    senha = request.form['senha']
    if nome and email and senha: # se não for valor nulo
        conn = mysql.connect() # cria conexão com mysql
        cursor = conn.cursor() # cria um cursos que conecta no banco
        cursor.execute('insert into tbl_user (user_seunome, user_username, user_password) VALUES (%s, %s, %s)', (nome, email, senha))
        conn.commit()
    return render_template('exemplomvc.html')

