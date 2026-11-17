CREATE TABLE niveis_alfabetizacao (
    id_nivel INTEGER PRIMARY KEY AUTOINCREMENT,
    hipotese TEXT NOT NULL,
    habilidade_bncc TEXT,
    intervencao_pedagogica TEXT,
    indicador_avanco TEXT
);

INSERT INTO niveis_alfabetizacao (hipotese, habilidade_bncc, intervencao_pedagogica, indicador_avanco)
VALUES 
('Pré-silábica', '(EI03EF09), (EI03EF01)', 'Trabalhar bingo de letras, alfabeto móvel...', 'Abandona o Realismo Nominal'),
('Silábica sem valor sonoro', '(EI03EF09)', 'Bater palmas para cada sílaba...', 'Utiliza vogais pertinentes à sílaba'),
('Silábica com valor sonoro', '(EI03EF03)', 'Auto ditado com alfabeto móvel...', 'Percebe necessidade de mais letras por sílaba'),
('Silábico-alfabética', '(EI03EF07)', 'Cartão conflito para completar letras...', 'Análise sonora completa'),
('Alfabética', '(EI03EF08), (EI03EF06)', 'Caderno exclusivo para produção de texto...', 'Fluência e domínio ortográfico');