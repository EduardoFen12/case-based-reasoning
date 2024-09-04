import sqlite3

# Conecta ao banco de dados (o arquivo .db será criado se não existir)
conn = sqlite3.connect('BDprotocolos.db')
cursor = conn.cursor()

querysBD = [
    '''INSERT INTO TBMusculosAlvo (DescricaoMA) VALUES ('Superiores');''',
    '''INSERT INTO TBMusculosAlvo (DescricaoMA) VALUES ('Inferiores');''',
    '''INSERT INTO TBMusculosAlvo (DescricaoMA) VALUES ('Ambos');''',
    '''INSERT INTO TBMusculosAlvo (DescricaoMA) VALUES ('Ambos com foco em superiores');''',
    '''INSERT INTO TBMusculosAlvo (DescricaoMA) VALUES ('Ambos com foco em inferiores');''',
    '''INSERT INTO TBObjetivo (NomeObj, RecomendacaoObj) VALUES ('Perder Gordura', 'Você PRECISA estar em deficit calórico (consumir menos calorias do que você gasta) e manter uma dieta rica em proteinas, frutas, verduras e legumes');''',
    '''INSERT INTO TBObjetivo (NomeObj, RecomendacaoObj) VALUES ('Ganhar Musculo', 'Você PRECISA estar em superávit calórico (consumir mais calorias do que você gasta) e manter uma dieta rica em proteinas, carboidratos, frutas, verduras e legumes');''',
]

# Cria as tabelas
for query in querysBD:
    cursor.execute(query)

# Salva as mudanças e fecha a conexão
conn.commit()
conn.close()

print("Banco de dados e tabelas populados com sucesso!")