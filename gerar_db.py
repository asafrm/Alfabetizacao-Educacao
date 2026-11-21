import sqlite3

script_sql = """
DROP TABLE IF EXISTS niveis_alfabetizacao;

CREATE TABLE niveis_alfabetizacao (
    id_nivel INTEGER PRIMARY KEY AUTOINCREMENT,
    hipotese TEXT NOT NULL,
    habilidade_bncc TEXT,
    intervencao_pedagogica TEXT,
    indicador_avanco TEXT
);

INSERT INTO niveis_alfabetizacao (hipotese, habilidade_bncc, intervencao_pedagogica, indicador_avanco)
VALUES 
('Pré-silábica', '(EI03EF09), (EI03EF01), (EF01LP04), (EF01LP05)', 'Trabalhar nome próprio, crachás, bingo de letras, alfabeto móvel, jogos de memória e atividades lúdicas de consciência fonológica.', 'Abandona o Realismo Nominal e percebe que a escrita representa a fala.'),
('Silábica sem valor sonoro', '(EI03EF09), (EF01LP06), (EF01LP07)', 'Bater palmas para cada sílaba pronunciada, contar os pedaços das palavras e usar alfabeto móvel focado nas vogais.', 'Passa a utilizar letras que representam sons pertinentes à sílaba.'),
('Silábica com valor sonoro', '(EI03EF03), (EF01LP08), (EF01LP09)', 'Auto ditado com alfabeto móvel a partir de imagens, brincadeira de forca, adedonha, preguicinha e encaixe de sílabas.', 'Percebe a necessidade de mais de uma letra para representar cada sílaba.'),
('Silábico-alfabética', '(EI03EF07), (EF01LP13), (EF02LP02), (EF02LP03)', 'Cartão conflito para completar letras faltantes nas sílabas, palavras cruzadas, ordenação de sílabas e caça-palavras em textos.', 'Realiza análise sonora completa, grafando todos os fonemas da palavra.'),
('Alfabética', '(EI03EF08), (EI03EF06), (EF01LP02), (EF02LP04), (EF02LP05), (EF03LP01), (EF03LP03)', 'Caderno exclusivo para produção e revisão de pequenos textos, uso do dicionário, banco de palavras e bingo com sílabas complexas.', 'Consolida a fluência de leitura e o domínio das convenções ortográficas.');
"""

conexao = sqlite3.connect('alfabetizacao.db')
cursor = conexao.cursor()
cursor.executescript(script_sql)
conexao.commit()
conexao.close()

print("Banco SQLite binário gerado e atualizado com sucesso!")