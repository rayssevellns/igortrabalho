class Filme:
    def __init__(self, id, descricao, completo=False):
        self.id = id
        self.descricao = descricao
        self.completo = completo

listaFilmes = []

def addFilme(descricao):
    id = len(listaFilmes) + 1  
    novo_filme = Filme(id, descricao)
    listaFilmes.append(novo_filme)

def getFilmes():
    return listaFilmes  
