from flask import Blueprint, render_template, request, redirect, url_for
from model import Filme, addFilme, getFilmes

filme_controllers = Blueprint("filme", __name__)

@filme_controllers.route("/")
def index():
    filmes = getFilmes() 
    return render_template('index.html', filmes=filmes)

@filme_controllers.route("/add", methods=["POST"])
def add():
    descricao = request.form["descricao"]
    addFilme(descricao) 
    return redirect(url_for('filme.index'))
