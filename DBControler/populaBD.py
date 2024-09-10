import sqlite3

# Conecta ao banco de dados (o arquivo .db será criado se não existir)
conn = sqlite3.connect('BDprotocolos.db')
cursor = conn.cursor()

querysBD = [
    '''INSERT INTO TBPesos (ValorPes, NomeIndexPes) VALUES (4, 'Objetivo');''',
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
    
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    '''INSERT INTO TBProtocolo VALUES (NULL);''',
    
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Superior 1');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Superior 2');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Superior 3');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Superior 4');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Superior 5');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Inferior 1');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Inferior 2');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Inferior 3');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Inferior 4');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Inferior 5');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Ambos Superior 1');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Ambos Superior 2');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Ambos Superior 3');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Ambos Inferior 1');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Ambos Inferior 2');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Ambos Inferior 3');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Ambos Superior Foco 1');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Ambos Superior Foco 2');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Ambos Inferior Foco 1');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Ambos Inferior Foco 2');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Superior Com Foco 1');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Superior Com Foco 2');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Inferior Com Foco 1');",
    "INSERT INTO TBTreinos (NomeTre) VALUES ('Treino Inferior Com Foco 2');",

    # Protocolo 1: Associação de exercícios com o "Treino Superior 1"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino reto'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino inclinado'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador inverso'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Cross over polia alta'));",

    # Protocolo 2: Associação de exercícios com o "Treino Inferior 1"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Cadeira extensora'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Cadeira flexora'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Mesa flexora'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento livre'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Stiff'));",

    # Protocolo 3: Associação de exercícios com o "Treino Ambos Superior 1"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino reto'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino inclinado'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador inverso'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Cross over polia alta'));",

    # Protocolo 4: Associação de exercícios com o "Treino Ambos Inferior 1"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Cadeira extensora'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Cadeira flexora'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Mesa flexora'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento livre'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Stiff'));",

    # Protocolo 5: Associação de exercícios com o "Treino Inferior Com Foco 1"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento no smith'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Elevação de quadril'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento livre'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Stiff'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Mesa flexora'));",

    # Protocolo 6: Associação de exercícios com o "Treino Inferior Com Foco 2"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento no smith'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Elevação de quadril'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento livre'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Stiff'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Mesa flexora'));",

    # Protocolo 7: Associação de exercícios com o "Treino Superior Com Foco 1"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino reto'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino inclinado'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador inverso'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Cross over polia alta'));",

    # Protocolo 8: Associação de exercícios com o "Treino Superior Com Foco 2"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino reto'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino inclinado'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador inverso'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 2'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Cross over polia alta'));",

    # Protocolo 9: Associação de exercícios com o "Treino Inferior Com Foco 3"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento no smith'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Elevação de quadril'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento livre'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Stiff'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Mesa flexora'));",

    # Protocolo 10: Associação de exercícios com o "Treino Superior Com Foco 3"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino reto'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino inclinado'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador inverso'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Cross over polia alta'));",

    # Protocolo 11: Associação de exercícios com o "Treino Inferior Com Foco 4"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento no smith'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Elevação de quadril'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento livre'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Stiff'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Superior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Mesa flexora'));",

    # Protocolo 12: Associação de exercícios com o "Treino Superior Com Foco 4"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino reto'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino inclinado'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador inverso'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Ambos Inferior 3'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Cross over polia alta'));",

    # Protocolo 13: Associação de exercícios com o "Treino Inferior Com Foco 5"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 5'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento no smith'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 5'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Elevação de quadril'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 5'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento livre'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 5'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Stiff'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 5'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Mesa flexora'));",

    # Protocolo 14: Associação de exercícios com o "Treino Superior Com Foco 5"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 5'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino reto'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 5'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino inclinado'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 5'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 5'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador inverso'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 5'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Cross over polia alta'));",

    # Protocolo 15: Associação de exercícios com o "Treino Inferior Com Foco 6"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior Com Foco 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento no smith'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior Com Foco 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Elevação de quadril'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior Com Foco 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Agachamento livre'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior Com Foco 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Stiff'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior Com Foco 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Mesa flexora'));",

    # Protocolo 16: Associação de exercícios com o "Treino Superior Com Foco 6"
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior Com Foco 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino reto'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior Com Foco 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Supino inclinado'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior Com Foco 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior Com Foco 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Voador inverso'));",
    "INSERT INTO TBRelET (FkIdTre, FkIdExe) VALUES ((SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior Com Foco 1'), (SELECT PkIdExe FROM TBExercicios WHERE DescricaoExe = 'Cross over polia alta'));",

    # Protocolo 1
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (1, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (1, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (1, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 3'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (1, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 4'));''',
    # Protocolo 2
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (2, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (2, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (2, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 3'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (2, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 4'));''',
    # Protocolo 3
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (3, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (3, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (3, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (3, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'));''',
    # Protocolo 4
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (4, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (4, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (4, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 3'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (4, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 4'));''',
    # Protocolo 5
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (5, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (5, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (5, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (5, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (5, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 3'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (5, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 3'));''',
    # Protocolo 6
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (6, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (6, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (6, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 3'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (6, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 4'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (6, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 5'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (6, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'));''',
    # Protocolo 7
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (7, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (7, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (7, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 3'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (7, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 4'));''',
    # Protocolo 8
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (8, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (8, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (8, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (8, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (8, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 3'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (8, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 3'));''',
    # Protocolo 9
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (9, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (9, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (9, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 3'));''',
    # Protocolo 10
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (10, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (10, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (10, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 3'));''',
    # Protocolo 11
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (11, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (11, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (11, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (11, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'));''',
    # Protocolo 12
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (12, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (12, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (12, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (12, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (12, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 3'));''',
    # Protocolo 13
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (13, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (13, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (13, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'));''',
    # Protocolo 14
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (14, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (14, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (14, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'));''',
    # Protocolo 15
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (15, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (15, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (15, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (15, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'));''',
    # Protocolo 16
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (16, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (16, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Superior 2'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (16, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 1'));''',
    '''INSERT INTO TBRelTP (FkIdPro, FkIdTre) VALUES (16, (SELECT PkIdTre FROM TBTreinos WHERE NomeTre = 'Treino Inferior 2'));''',
    
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (1, 'm', 'Carlos', 30, 85, 178, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Superiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 1));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (1, 'f', 'Maria', 24, 60, 165, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Inferiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 2));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (1, 'm', 'João', 29, 77, 180, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Ambos com foco em superiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 3));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (1, 'f', 'Ana', 22, 68, 170, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Ambos com foco em inferiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 4));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (1, 'm', 'Pedro', 32, 90, 175, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Superiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 5));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (1, 'f', 'Juliana', 27, 72, 168, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Inferiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 6));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (1, 'm', 'Ricardo', 34, 80, 182, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Ambos com foco em superiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 7));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (1, 'f', 'Fernanda', 28, 64, 160, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Ambos com foco em inferiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 8));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (2, 'f', 'Luciana', 25, 70, 162, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Superiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 9));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (2, 'm', 'Felipe', 29, 78, 177, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Inferiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 10));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (2, 'm', 'Lucas', 33, 88, 183, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Ambos com foco em superiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 11));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (2, 'f', 'Claudia', 26, 66, 169, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Ambos com foco em inferiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 12));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (2, 'm', 'Marcos', 31, 82, 179, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Superiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 13));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (2, 'f', 'Isabela', 23, 62, 167, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Inferiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 14));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (2, 'm', 'Renato', 28, 75, 172, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Ambos com foco em superiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 15));",
    "INSERT INTO TBCasos (FkIdObj, GeneroCas, NomeCas, IdadeCas, PesoCas, AlturaCas, FkIdMA, FkIdPro) VALUES (2, 'f', 'Lúcia', 30, 68, 174, (SELECT PkIdMA FROM TBMusculosAlvo WHERE DescricaoMA = 'Ambos com foco em inferiores'), (SELECT PkIdPro FROM TBProtocolo WHERE PkIdPro = 16));",

]

# Cria as tabelas
for query in querysBD:
    cursor.execute(query)

# Salva as mudanças e fecha a conexão
conn.commit()
conn.close()

print("Banco de dados e tabelas populados com sucesso!")