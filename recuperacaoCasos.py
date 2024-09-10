import sqlite3
import math


def distancia_personalizada(caso1, novoCaso, pesos):
    soma_diferencas = 0
    
    # Para cada atributo
    for i, (a, b) in enumerate(zip(caso1, novoCaso)):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            # Atributos numéricos (idade, peso, altura)
            diferenca = (a - b) ** 2
        else:
            # Atributos categóricos (gênero, objetivo)
            diferenca = 1 if a != b else 0
        
        # Multiplica pela importância (peso)
        soma_diferencas += pesos[i] * diferenca
    
    # Retorna a raiz quadrada da soma ponderada
    return math.sqrt(soma_diferencas)



def encontrar_vizinhos_proximos(casos, novoCaso, pesos, k=3):
    # Ordena os casos com base na nova função de distância
    casos_ordenados = sorted(casos, key=lambda caso: distancia_personalizada(caso[:-1], novoCaso, pesos))
    
    # Retorna os 'k' casos mais próximos
    return casos_ordenados[:k]



# nome, idade, peso, altura, genero, objetivo,
def recuperacaoCasos(musculoAlvo, novoCaso):

    conn = sqlite3.connect('BDprotocolos.db')
    cursor = conn.cursor()

    sql = "SELECT FkIdObj, FkIdMA, GeneroCas, PesoCas, AlturaCas, IdadeCas, NomeCas, PkIdCas, FkIdPro FROM TBCasos"
    cursor.execute(sql)
    tbCasos = cursor.fetchall() 

    sql = "SELECT ValorPes FROM TBPesos"
    cursor.execute(sql)
    tbPesos = cursor.fetchall() 
    listaPesos = []

    for peso in tbPesos:
        listaPesos.append(int(peso[0]))

    casos = []

    for caso in tbCasos:

        atributosCaso = []

        if caso[1] == musculoAlvo:

            atributosCaso.append(caso[0])  # FkIdObj
            atributosCaso.append(caso[2])  # GeneroCas
            atributosCaso.append(caso[3])  # PesoCas
            atributosCaso.append(caso[4])  # AlturaCas
            atributosCaso.append(caso[5])  # IdadeCas

            atributosCaso.append(caso[8])  # FkIdPro

            casos.append(atributosCaso)

    vizinhos = encontrar_vizinhos_proximos(casos, novoCaso, listaPesos, k=1)
    pkProtocolo = vizinhos[0][-1]  # O último valor é o FkIdPro
            
    conn.close()
    
    return pkProtocolo