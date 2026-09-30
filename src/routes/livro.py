from config import *
from models.livro import Livro
import services.livro as livro_service


'''
--------------
LISTAR LIVROS
--------------
'''

'''
TESTE DE ROTA - Livro - GET

curl localhost:5000/livro
{
  "detalhes": [
    {
      "titulo": "para sempre seu",
      "id": 1,
      "editora": "arqueiro",
      "edicao": "2026",
      "autores": "Abby Jimenez",
      "ano": "2025"
    }
  ],
  "resultado": "ok"
}

'''

# rota para listar livros
# rota liberada para listagem pública :-) não requer JWT
@app.route('/livro', methods=['GET'])
def retornar_livro():

    # buscar os livro
    livros = livro_service.retornar_livro()
    
    # retornar a lista de pessoas em JSON
    return jsonify({
        "resultado":"ok",
        "detalhes":[livro.json() for livro in livros]
    })







'''
--------------
INCLUIR LIVROS
--------------
'''

'''
TESTE DE ROTA - Livro - POST

curl http://localhost:5000/pessoa -X POST -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc4NDU4NDIwNCwianRpIjoiNDE0NWNhOTUtYzA0NS00Mjk2LThjZjctNjUxNzliZTA5ZTMzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3ODQ1ODQyMDQsImNzcmYiOiJhMmMxNTU4Yy1lNjI0LTQ2OTYtOWRlZi0wZGY5YTg4Mjc0MzMiLCJleHAiOjE3ODQ1ODUxMDR9.C2ZOz5K7Dm90QCXsiGC7BslmHn-DGYsVYRUtmmaPWsI" -H "Content-Type:application/json" -d '{"titilo":"Para sempre seu", "autores":"Abby jeminez","editora":"arqueiro", "edicao":"2025","":"2025"}'
{"detalhes":{"":"titulo": "para sempre seu",
      "id": 1,
      "editora": "arqueiro",
      "edicao": "2026",
      "autores": "Abby Jimenez",
      "ano": "2025"},"resultado":"ok"}

'''

# rota para inserir um livro
@app.route('/livro', methods=['POST'])
@jwt_required()  # exige que o usuário esteja autenticado para acessar esta rota
def criar_livro():
    # ler os dados em json
    dados = request.json
    
    # se faltou algum dado obrigatório...
    if not dados or not dados.get('titulo') or not dados.get('autores') or not dados.get('editora') or not dados.get('edicao') or not dados.get('ano'):
        # retorna erro
        return jsonify({"resultado":"erro", "detalhes":"Titulo, autores, editora, edição e ano são obrigatórios"}), 400
    
    # chama o serviço de criação de um livro
    livro = livro_service.criar_livro(dados)    
    
    # retornar mensagem de sucesso :-)
    return jsonify({
        "resultado":"ok", 
        "detalhes":livro.json()
    }), 201

