from flask import Flask, render_template

# Criação de uma instância do Flask
app = Flask(__name__)

# Definição de uma rota
@app.route('/')
def ola_mundo():
 return render_template('login.html')

@app.route('/cadastro')
def cadastro_cliente():
 return 'Cadastro de Clientes'

@app.route('/tela_principal')
def tela_principal():
 nomeTeste = 'Izabel'
 return render_template('tela_principal.html', nome=nomeTeste)

#Inicia o servidor de desenvolvimento.
if __name__ == '__main__':
 app.run()