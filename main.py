import sqlite3
import json

def diagnosticar_hipotese(payload_respostas):
    # O payload_respostas é um JSON vindo da interface
    usa_letras = payload_respostas.get("usa_letras") # Booleano
    uma_letra_por_silaba = payload_respostas.get("uma_letra_por_silaba") # Booleano
    tem_valor_sonoro = payload_respostas.get("tem_valor_sonoro") # Booleano
    mapeia_todos_fonemas = payload_respostas.get("mapeia_todos_fonemas") # Booleano
    oscila_escrita = payload_respostas.get("oscila_escrita") # Booleano

    # Motor de Regras (If-Then baseado na matriz)
    if mapeia_todos_fonemas:
        hipotese_resultado = "Alfabética"
    elif oscila_escrita:
        hipotese_resultado = "Silábico-alfabética"
    elif uma_letra_por_silaba and tem_valor_sonoro:
        hipotese_resultado = "Silábica com valor sonoro"
    elif uma_letra_por_silaba and not tem_valor_sonoro:
        hipotese_resultado = "Silábica sem valor sonoro"
    else:
        # Engloba garatujas, letras aleatórias e realismo nominal
        hipotese_resultado = "Pré-silábica"

    return buscar_dados_intervencao(hipotese_resultado)

def buscar_dados_intervencao(hipotese):
    conexao = sqlite3.connect('alfabetizacao.db')
    cursor = conexao.cursor()
    
    cursor.execute("SELECT * FROM niveis_alfabetizacao WHERE hipotese = ?", (hipotese,))
    resultado = cursor.fetchone()
    conexao.close()
    
    # Retorna um dicionário montado para ser enviado de volta à interface
    return {
        "hipotese_diagnosticada": resultado[1],
        "habilidades_bncc": resultado[2],
        "intervencao": resultado[3],
        "proximo_passo": resultado[4]
    }