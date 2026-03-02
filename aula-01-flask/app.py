# flask = pacote // Flask = classe
from flask import Flask, render_template

# declarando variavel do flask como 'app'
app = Flask(__name__, template_folder='views')
# app = Flask(app.py)
# variaveis com __ são variaveis de ambiente do python que ja existem
# __name__ representa o nome da aplicaçao

# criando rota principal e função (o @ liga as duas)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/games')
def games():
    jogo = "Portal 2"
    ano = "2011"
    genero = "Puzzle"
    
    return render_template('games.html')

@app.route('/consoles')
def consoles():
    return render_template('consoles.html')

# iniciar servidor na porta 5000, verificando se o arquivo é o main
if __name__ == '__main__':
    app.run(port=5000, debug=True)

