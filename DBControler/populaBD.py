import sqlite3

# Conecta ao banco de dados (o arquivo .db será criado se não existir)
conn = sqlite3.connect('BDprotocolos.db')
cursor = conn.cursor()

querysBD = [
    '''INSERT INTO TBPesos (ValorPes, NomeIndexPes) VALUES (4, 'Objetivo');''',
    '''INSERT INTO TBPesos (ValorPes, NomeIndexPes) VALUES (5, 'MusculoAlvo');''',
    '''INSERT INTO TBPesos (ValorPes, NomeIndexPes) VALUES (3, 'Genero');''',
    '''INSERT INTO TBPesos (ValorPes, NomeIndexPes) VALUES (1, 'Peso');''',
    '''INSERT INTO TBPesos (ValorPes, NomeIndexPes) VALUES (1, 'Altura');''',
    '''INSERT INTO TBPesos (ValorPes, NomeIndexPes) VALUES (2, 'idade');''',
    
    '''INSERT INTO TBMusculosAlvo (DescricaoMA) VALUES ('Superiores');''',
    '''INSERT INTO TBMusculosAlvo (DescricaoMA) VALUES ('Inferiores');''',
    '''INSERT INTO TBMusculosAlvo (DescricaoMA) VALUES ('Ambos');''',
    '''INSERT INTO TBMusculosAlvo (DescricaoMA) VALUES ('Ambos com foco em superiores');''',
    '''INSERT INTO TBMusculosAlvo (DescricaoMA) VALUES ('Ambos com foco em inferiores');''',
    
    '''INSERT INTO TBObjetivo (NomeObj, RecomendacaoObj) VALUES ('Perder Gordura', 'Você PRECISA estar em deficit calórico (consumir menos calorias do que você gasta) e manter uma dieta rica em proteinas, frutas, verduras e legumes');''',
    '''INSERT INTO TBObjetivo (NomeObj, RecomendacaoObj) VALUES ('Ganhar Musculo', 'Você PRECISA estar em superávit calórico (consumir mais calorias do que você gasta) e manter uma dieta rica em proteinas, carboidratos, frutas, verduras e legumes');''',
   
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Supino reto', 'Halteres', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Supino inclinado', 'Halteres', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Voador', 'Peck deck', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Voador inverso', 'Peck deck', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Cross over polia alta', 'Cross over', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Elevação lateral', 'Halteres', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Elevação frontal', 'Halteres', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Desenvolvimento', 'Halteres', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Puxada alta', 'Lat Pulldown', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Remada curvada', 'Barra', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Remada baixa triangulo', 'Leg Curl Machine', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Serrote', 'Halteres', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Rosca direta', 'Halteres', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Rosca scott', 'Maquina scott', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Rosca martelo', 'Halteres', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Triceps corda', 'Roldana', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Triceps pulley', 'Roldana', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Triceps frances', 'Halteres', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Triceps paralelas', 'Paralelas', 1)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Cadeira extensora', 'Cadeira extensora', 2)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Cadeira flexora', 'Cadeira flexora', 2)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Mesa flexora', 'Mesa flexora', 2)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Agachamento livre', 'Barra', 2)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Stiff', 'Barra', 2)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Agachamento no smith', 'Smith', 2)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Elevação de quadril', 'Barra', 2)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Abdominal na paralela', 'Paralelas', 3)''',
    '''INSERT INTO TBExercicios (DescricaoExe, AparelhoExe, FkIdMA) VALUES ('Abdominal na maquina', 'Ab roller', 3)''',
]

# Cria as tabelas
for query in querysBD:
    cursor.execute(query)

# Salva as mudanças e fecha a conexão
conn.commit()
conn.close()

print("Banco de dados e tabelas populados com sucesso!")