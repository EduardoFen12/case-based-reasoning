from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from recuperacaoCasos import *
from protocolo import *

app = Flask(__name__)

conn = sqlite3.connect('BDprotocolos.db')
cursor = conn.cursor()

idProtocoloResposta = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        global idProtocoloResposta

        nome = request.form['nome']
        idade = int(request.form['idade'])
        peso = int(request.form['peso'])
        altura = int(request.form['altura'])
        genero = request.form['genero']
        objetivo = request.form['objetivo']
        musculoAlvo = int(request.form['musculoAlvo'])
        
        # print(f'Nome: {nome}, Idade: {idade}, Peso: {peso}, Altura: {altura}, Genero: {genero}, Objetivo: {objetivo}, Musculo Alvo: {musculoAlvo}')
        
        idProtocoloResposta = recuperacaoCasos(musculoAlvo, [idade, peso, altura, genero, objetivo])
        
        return redirect(url_for(f'sucesso'))
    
    return render_template('form.html')

@app.route('/sucesso')
def sucesso():

    global idProtocoloResposta
    html = exibirProtocolo(idProtocoloResposta)

    return f"{html}"
    # return  render_template('sucesso.html')


if __name__ == '__main__':
    app.run(debug=True)
