from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Pega os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        
        # Aqui você pode processar os dados, salvar no banco de dados, etc.
        print(f'Nome: {nome}, Email: {email}')
        
        # Redireciona para uma página de sucesso ou exibe uma mensagem
        return redirect(url_for('sucesso'))
    
    return render_template('form.html')

@app.route('/sucesso')
def sucesso():
    # return "<h1>Formulário enviado com sucesso!</h1>"
    return  render_template('sucesso.html')


if __name__ == '__main__':
    app.run(debug=True)
