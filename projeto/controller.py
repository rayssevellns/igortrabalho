from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import Filme, addFilme, getFilmes

filme_controllers = Blueprint("filme", __name__)

@filme_controllers.route("/")
def index():
    filmes = getFilmes()
    username = session.get('username')  
    return render_template('index.html', filmes=filmes, username=username)

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
        
        session['username'] = user 
        flash(f'Bem-vindo, {user}!', 'success') 
        return redirect(url_for('filme.welcome'))  
    return render_template('login.html')  

@filme_controllers.route("/welcome")
def welcome():
    username = session.get('username')
    return render_template('welcome.html', username=username)

@filme_controllers.route("/logout")
def logout():
    session.pop('username', None)  
    flash('Você foi desconectado.', 'info')  
    return redirect(url_for('filme.login'))  
