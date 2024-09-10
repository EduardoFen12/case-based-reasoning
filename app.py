from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from recuperacaoCasos import *

app = Flask(__name__)

conn = sqlite3.connect('BDprotocolos.db')
cursor = conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Pega os dados do formulário
        nome = request.form['nome']
        idade = request.form['idade']
        peso = request.form['peso']
        altura = request.form['altura']
        genero = request.form['genero']
        objetivo = request.form['objetivo']
        musculoAlvo = request.form['musculoAlvo']
        
        # Aqui você pode processar os dados, salvar no banco de dados, etc.
        print(f'Nome: {nome}, Idade: {idade}, Peso: {peso}, Altura: {altura}, Genero: {genero}, Objetivo: {objetivo}, Musculo Alvo: {musculoAlvo}')
        
        idProtocoloResposta = recuperacaoCasos(nome, idade, peso, altura, genero, objetivo, musculoAlvo)
        
        sql = f"SELECT * FROM TBProtocolo WHERE PkIdPro = {idProtocoloResposta}"
        
        cursor.execute(sql)

        tabela = cursor.fetchall()
        
        # Redireciona para uma página de sucesso ou exibe uma mensagem
        return redirect(url_for('sucesso'))
    
    return render_template('form.html')

@app.route('/sucesso')
def sucesso():
    # return "<h1>Formulário enviado com sucesso!</h1>"
    return  render_template('sucesso.html')


if __name__ == '__main__':
    app.run(debug=True)
