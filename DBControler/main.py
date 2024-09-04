import sqlite3

# Conecta ao banco de dados
conn = sqlite3.connect('BDprotocolos.db')
cursor = conn.cursor()

# Consulta para listar todas as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

print("Tabelas e suas colunas no banco de dados:")

# Itera sobre cada tabela e exibe suas colunas
for tabela in tabelas:
    tabela_nome = tabela[0]
    print(f"\nTabela: {tabela_nome}")

    # Consulta para obter informações sobre as colunas da tabela
    cursor.execute(f"PRAGMA table_info({tabela_nome});")
    colunas = cursor.fetchall()

    # Exibe as colunas
    for coluna in colunas:
        nome_coluna = coluna[1]  # Nome da coluna
        tipo_coluna = coluna[2]  # Tipo de dados
        print(f"Coluna: {nome_coluna}, Tipo: {tipo_coluna}")
        
cursor.execute('SELECT * FROM TBObjetivo')
tabela = cursor.fetchall()
for linha in tabela:
    print(linha)
cursor.execute('SELECT * FROM TBMusculosAlvo')
tabela = cursor.fetchall()
for linha in tabela:
    print(linha)

# Fecha a conexão
conn.close()
