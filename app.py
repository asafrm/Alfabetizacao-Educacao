from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#O Motor de Inferência 
@app.route('/motor', methods=['POST'])
def motor_de_inferencia():
    dados = request.get_json()
    
    #Aplicação das Regras 
    if not dados.get('usa_letras'):
        hipotese = "Pré-silábica"
    elif dados.get('mapeia_todos_fonemas'):
        hipotese = "Alfabética"
    elif dados.get('uma_letra_por_silaba'):
        if dados.get('letras_correspondem_som'):
            hipotese = "Silábica com valor sonoro"
        else:
            hipotese = "Silábica sem valor sonoro"
    else:
        hipotese = "Silábico-alfabética"

    #Busca na Base de Conhecimento
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