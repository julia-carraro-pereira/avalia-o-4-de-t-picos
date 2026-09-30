from config import *
from models.livro import Livro

def criar_livro(data):
    # criar um livro
    livro = Livro(
        titulo=data['titulo'],
        autores=data['autores'],
        editora=data['editora'],
        edicao=data['edicao'],
        ano=data.get('ano')
    )
    
    # salvar no banco de dados
    db.session.add(livro)
    db.session.commit()
    
    return livro

def retornar_livro():
    # buscar todas os livros no 
    # banco de dados
    livro = Livro.query.all()
    
    return livro
