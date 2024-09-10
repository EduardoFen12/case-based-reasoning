import sqlite3

def exibirProtocolo(pkIdPro):
    conn = sqlite3.connect('BDprotocolos.db')
    cursor = conn.cursor()

    query = '''
    SELECT 
        t.NomeTre AS Treino,
        e.DescricaoExe AS Exercicio
    FROM TBProtocolo p
    JOIN TBRelTP rtp ON p.PkIdPro = rtp.FkIdPro
    JOIN TBTreinos t ON rtp.FkIdTre = t.PkIdTre
    JOIN TBRelET ret ON t.PkIdTre = ret.FkIdTre
    JOIN TBExercicios e ON ret.FkIdExe = e.PkIdExe
    WHERE p.PkIdPro = ?
    ORDER BY t.PkIdTre;
    '''
    
    cursor.execute(query, (pkIdPro,))
    resultados = cursor.fetchall()

    html = ""

    if resultados:
        html += f"<h1>Protocolo {pkIdPro}:</h1><p>"
        treino_atual = None
        exercicio_atual = None
        for treino, exercicio in resultados:
            if treino != treino_atual:
                treino_atual = treino
                html += f"<br> &nbsp;&nbsp;&nbsp;&nbsp;<strong>{treino}:</strong><br>"
            
            if exercicio != exercicio_atual:
                exercicio_atual = exercicio
                html += f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{exercicio}: 3x 8 à 12<br>"
        
        html += "</p>"
    else:
        html += f"Nenhum treino encontrado para o Protocolo {pkIdPro} </p>"

    conn.close()

    return html