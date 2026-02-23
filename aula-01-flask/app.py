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

@app.route('/gays')
def gays():
    return render_template('gays.html')

@app.route('/yaois')
def yaois():
    return render_template('yaois.html')

# iniciar servidor na porta 5000, verificando se o arquivo é o main
if __name__ == '__main__':
    app.run(port=5000, debug=True)

