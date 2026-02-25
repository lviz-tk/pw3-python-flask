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

@app.route('/lista')
def lista():
    return render_template('lista.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

# iniciar servidor na porta 5000, verificando se o arquivo é o main
if __name__ == '__main__':
    app.run(port=5000, debug=True)

