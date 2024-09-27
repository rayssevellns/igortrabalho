from flask import Flask
from controller import filme_controllers

app = Flask(__name__)
app.register_blueprint(filme_controllers)

if __name__ == "__main__":
    app.run(debug=True)
