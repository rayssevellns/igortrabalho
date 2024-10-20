
class Filme:
    def __init__(self, id, descricao, completo=False):
        self.id = id
        self.descricao = descricao
        self.completo = completo

listaFilmes = []

usuarios = {
    "user": "1234",
    "admin": "5678"
}

def addFilme(descricao):
    id = len(listaFilmes) + 1  
    novo_filme = Filme(id, descricao)
    listaFilmes.append(novo_filme)

def getFilmes():
    return listaFilmes

def autenticar(user, senha):

    if user in usuarios:
        if usuarios[user] == senha:
            return user
    return None
