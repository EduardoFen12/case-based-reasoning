from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from recuperacaoCasos import *

app = Flask(__name__)

conn = sqlite3.connect('BDprotocolos.db')
cursor = conn.cursor()

resposta = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        global resposta

        nome = request.form['nome']
        idade = int(request.form['idade'])
        peso = int(request.form['peso'])
        altura = int(request.form['altura'])
        genero = request.form['genero']
        objetivo = request.form['objetivo']
        musculoAlvo = int(request.form['musculoAlvo'])
        
        # Aqui você pode processar os dados, salvar no banco de dados, etc.
        print(f'Nome: {nome}, Idade: {idade}, Peso: {peso}, Altura: {altura}, Genero: {genero}, Objetivo: {objetivo}, Musculo Alvo: {musculoAlvo}')
        
        resposta = recuperacaoCasos(musculoAlvo, [idade, peso, altura, genero, objetivo])
        
        # idProtocoloResposta = recuperacaoCasos(musculoAlvo, [nome, idade, peso, altura, genero, objetivo])
        
        # sql = f"SELECT * FROM TBProtocolo WHERE PkIdPro = {idProtocoloResposta}"
        
        # cursor.execute(sql)

        # tabela = cursor.fetchall()
        
        # Redireciona para uma página de sucesso ou exibe uma mensagem
        return redirect(url_for(f'sucesso'))
    
    return render_template('form.html')

@app.route('/sucesso')
def sucesso():
    return f"<h1>Formulário enviado com sucesso!</h1><p>{resposta}</p>"
    # return  render_template('sucesso.html')


if __name__ == '__main__':
    app.run(debug=True)
