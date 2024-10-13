from flask import Flask
from controllers import filme_controllers

app = Flask(__name__)

app.secret_key = 'sua_chave_secreta_aqui' 

app.register_blueprint(filme_controllers)

if __name__ == "__main__":
    app.run(debug=True)
