from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from model import Filme, addFilme, getFilmes, autenticar

filme_controllers = Blueprint("filme", __name__)

@filme_controllers.before_request
def before_request():
    print(f"Método da Requisição: {request.method} | Caminho da Requisição: {request.path}")

@filme_controllers.after_request
def after_request(response):
    response.set_cookie('visited', 'true')
    return response

@filme_controllers.route("/")
def index():
    filmes = getFilmes()
    username = session.get('username')
    visited = request.cookies.get('visited')
    return render_template('index.html', filmes=filmes, username=username, visited=visited)

@filme_controllers.route("/add", methods=["POST"])
def add():
    descricao = request.form["descricao"]
    addFilme(descricao)
    return redirect(url_for('filme.index'))

@filme_controllers.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        senha = request.form['senha']
        
        autenticado = autenticar(user, senha)
        if autenticado:
            session['username'] = user
            flash(f'Bem-vindo, {autenticado}!', 'success')
            return redirect(url_for('filme.welcome'))
        else:
            flash('Usuário ou senha inválidos.', 'danger')  
    return render_template('login.html')

@filme_controllers.route("/welcome")
def welcome():
    username = session.get('username')
    if username == "admin":
        message = "Bem-vindo, ADMIN!"
    else:
        message = "Bem-vindo, USER!"
    return render_template('welcome.html', username=username, message=message)

@filme_controllers.route("/logout")
def logout():
    session.pop('username', None)
    flash('Você foi desconectado.', 'info')
    return redirect(url_for('filme.login'))
