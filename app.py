from flask import Flask, render_template, request, jsonify
from collections import Counter
import sqlite3
import unicodedata

app = Flask(__name__)

# Gabarito das palavras: número de sílabas, letras aceitas foneticamente e mínimo para alfabética
GABARITO = {
    "borboleta": {"silabas": 4, "sons": set("BORLETAU"), "min_alfabetica": 7},
    "cavalo":    {"silabas": 3, "sons": set("CKAVLUO"),  "min_alfabetica": 5},
    "gato":      {"silabas": 2, "sons": set("GATUO"),    "min_alfabetica": 4},
}

def limpar_texto(texto):
    texto = unicodedata.normalize('NFD', texto.upper().strip())
    return ''.join(c for c in texto if c.isalpha())

def classificar_palavra(escrita, regra):
    palavra = limpar_texto(escrita)
    tamanho = len(palavra)
    silabas = regra["silabas"]
    sons = regra["sons"]

    if tamanho == 0:
        return "Pré-silábica"

    acertos_sonoros = sum(1 for letra in palavra if letra in sons)
    taxa_sonora = acertos_sonoros / tamanho

    # 1. Alfabética: tamanho próximo da palavra completa e alta correspondência sonora
    if tamanho >= regra["min_alfabetica"] and taxa_sonora >= 0.7:
        return "Alfabética"

    # 2. Silábica: 1 letra por sílaba
    if tamanho == silabas:
        if taxa_sonora >= 0.5:
            return "Silábica com valor sonoro"
        return "Silábica sem valor sonoro"

    # 3. Silábico-alfabética: transição (mais letras que sílabas, mas incompleta)
    if silabas < tamanho < regra["min_alfabetica"] and taxa_sonora >= 0.6:
        return "Silábico-alfabética"

    # 4. Pré-silábica: letras aleatórias sem correspondência sonora
    return "Pré-silábica"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/motor', methods=['POST'])
def motor_de_inferencia():
    dados = request.get_json()

    if dados.get('apenas_rabiscos'):
        hipotese = "Pré-silábica"
    else:
        palavras = dados.get('palavras', {})
        votos = []
        for chave, regra in GABARITO.items():
            escrita = palavras.get(chave, "")
            if escrita:
                votos.append(classificar_palavra(escrita, regra))

        hipotese = Counter(votos).most_common(1)[0][0] if votos else "Pré-silábica"

    resultado_pedagogico = buscar_banco_conhecimento(hipotese)
    return jsonify(resultado_pedagogico)

def buscar_banco_conhecimento(hipotese):
    conexao = sqlite3.connect('alfabetizacao.db')
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT habilidade_bncc, intervencao_pedagogica 
        FROM niveis_alfabetizacao 
        WHERE hipotese = ?
    """, (hipotese,))

    linha = cursor.fetchone()
    conexao.close()

    if linha:
        return {
            "hipotese": hipotese,
            "bncc": linha[0],
            "intervencao": linha[1]
        }
    return {"erro": "Hipótese não mapeada"}

if __name__ == '__main__':
    app.run(debug=True, port=5000)