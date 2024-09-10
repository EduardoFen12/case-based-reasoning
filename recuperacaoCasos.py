import sqlite3

# nome, idade, peso, altura, genero, objetivo,
def recuperacaoCasos(musculoAlvo):

    conn = sqlite3.connect('BDprotocolos.db')
    cursor = conn.cursor()

    sql = "SELECT FkIdObj, FkIdMA, GeneroCas, PesoCas, AlturaCas, IdadeCas, NomeCas, PkIdCas, FkIdPro FROM TBCasos"

    cursor.execute(sql)

    tabela = cursor.fetchall() 
    # GUIA:
    # linha[0] = FkIdObj 
    # linha[1] = FkIdMA 
    # linha[2] = GeneroCas 
    # linha[3] = PesoCas 
    # linha[4] = AlturaCas 
    # linha[5] = IdadeCas 
    # linha[6] = NomeCas
    # linha[7] = PkIdCas  
    # linha[8] = FkIdPro

    for linha in tabela:

        if linha[1] == musculoAlvo:
            
            print(linha[1])

    conn.close()
    
    # return pkIdProtocolo

recuperacaoCasos(1)