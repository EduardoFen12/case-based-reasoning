import sqlite3

# Conecta ao banco de dados (o arquivo .db será criado se não existir)
conn = sqlite3.connect('BDprotocolos.db')
cursor = conn.cursor()

querysCriacaoBD = [
    '''CREATE TABLE IF NOT EXISTS TBCasos (
        PkIdCas INTEGER PRIMARY KEY AUTOINCREMENT,
        FkIdObj INTEGER NOT NULL,
        GeneroCas CHAR(1) NOT NULL,
        IdadeCas INTEGER NOT NULL,
        NomeCas TEXT,
        PesoCas INTEGER NOT NULL,
        AlturaCas INTEGER NOT NULL,
        HorasDiaCas INTEGER,
        DiasSemanaCas INTEGER,
        FlgExperienciaCas BOOLEAN,
        FkIdMA INTEGER NOT NULL,
        FkIdPro INTEGER NOT NULL,
        FkIdRes INTEGER NOT NULL,
        FOREIGN KEY (FkIdObj) REFERENCES TBObjetivo (PkIdObj),
        FOREIGN KEY (FkIdMA) REFERENCES TBMusculosAlvo (PkIdMA),
        FOREIGN KEY (FkIdPro) REFERENCES TBProtocolo (PkIdPro),
        FOREIGN KEY (FkIdRes) REFERENCES TBTelTP (PkIdTP)
    )''',
    '''
    CREATE TABLE IF NOT EXISTS TBProtocolo (
        PkIdPro INTEGER PRIMARY KEY AUTOINCREMENT
    )''',
    '''CREATE TABLE IF NOT EXISTS TBRelTP (
        PkIdTP INTEGER PRIMARY KEY AUTOINCREMENT,
        FkIdPro INTEGER NOT NULL,
        FkIdTre INTEGER NOT NULL,
        FOREIGN KEY (FkIdPro) REFERENCES TBProtocolo (PkIdPro),
        FOREIGN KEY (FkIdTre) REFERENCES TBTreinos (PkIdTre)
    )''',
    '''CREATE TABLE IF NOT EXISTS TBTreinos (
        PkIdTre INTEGER PRIMARY KEY AUTOINCREMENT,
        NomeTre TEXT NOT NULL
    )''',
    '''CREATE TABLE IF NOT EXISTS TBRelET (
        PkIdET INTEGER PRIMARY KEY AUTOINCREMENT,
        FkIdTre INTEGER NOT NULL,
        FkIdExe INTEGER NOT NULL,
        FOREIGN KEY (FkIdTre) REFERENCES TBTreinos (PkIdTre),
        FOREIGN KEY (FkIdExe) REFERENCES TBExercicios (PkIdExe)
    )''',
    '''CREATE TABLE IF NOT EXISTS TBExercicios (
        PkIdExe INTEGER PRIMARY KEY AUTOINCREMENT,
        DescricaoExe TEXT NOT NULL,
        AparelhoExe TEXT NOT NULL,
        FkIdMA INTEGER NOT NULL,
        FOREIGN KEY (FkIdMA) REFERENCES TBMusculosAlvo (PkIdMA)
    )''',
    '''CREATE TABLE IF NOT EXISTS TBMusculosAlvo (
        PkIdMA INTEGER PRIMARY KEY AUTOINCREMENT,
        DescricaoMA TEXT NOT NULL
    )''',
    '''CREATE TABLE IF NOT EXISTS TBObjetivo (
        PkIdObj INTEGER PRIMARY KEY AUTOINCREMENT,
        NomeObj TEXT NOT NULL,
        RecomendacaoObj TEXT NOT NULL
    )''',
]

# Ativa a verificação de chaves estrangeiras
cursor.execute('PRAGMA foreign_keys = ON;')

# Cria as tabelas
for query in querysCriacaoBD:
    cursor.execute(query)

# Salva as mudanças e fecha a conexão
conn.commit()
conn.close()

print("Banco de dados e tabelas criados com sucesso!")
