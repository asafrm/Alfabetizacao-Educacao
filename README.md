# Sistema Especialista - Alfabetização

Aplicação web de apoio pedagógico para realizar uma sondagem de escrita e apresentar uma hipótese de alfabetização, habilidades da BNCC e sugestões de intervenção pedagógica.

> **Aviso:** o sistema oferece uma estimativa automatizada baseada em regras simples e em um conjunto limitado de palavras. Não substitui a avaliação e o acompanhamento de um profissional da educação.

## Funcionalidades

- Orientações para aplicação individual da sondagem de escrita.
- Transcrição das palavras escritas pela criança.
- Opção de indicar que a produção foi composta apenas por rabiscos, garatujas ou desenhos.
- Classificação automatizada em hipóteses de escrita:
  - Pré-silábica
  - Silábica sem valor sonoro
  - Silábica com valor sonoro
  - Silábico-alfabética
  - Alfabética
- Consulta ao banco de dados SQLite para apresentar habilidades BNCC e intervenções pedagógicas associadas à hipótese.
- Destaque visual de materiais de apoio recomendados.

## Tecnologias

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript

## Estrutura do projeto

```text
Sistema Nível de Alfabetização/
├── app.py
├── gerar_db.py
├── alfabetizacao.db
├── BNCC_EDUCAÇÃO BASICA.pdf
├── Orientações - psicogênese.pdf
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## Requisitos

- Python 3 instalado
- pip (gerenciador de pacotes do Python)

## Instalação e execução

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. Acesse a pasta do projeto:

   ```bash
   cd "Sistema Nível de Alfabetização"
   ```

3. (Opcional, recomendado) Crie e ative um ambiente virtual:

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **Linux/macOS:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Instale o Flask:

   ```bash
   pip install Flask
   ```

5. Se necessário, gere/recrie o banco de dados:

   ```bash
   python gerar_db.py
   ```

   **Atenção:** o script `gerar_db.py` apaga a tabela existente `niveis_alfabetizacao` e a recria com os dados definidos no script.

6. Inicie a aplicação:

   ```bash
   python app.py
   ```

7. Acesse no navegador:

   [http://localhost:5000](http://localhost:5000)

## Como utilizar

1. Leia as orientações apresentadas na tela inicial para aplicar a sondagem no papel.
2. Dite as palavras sugeridas, sem separar artificialmente as sílabas ou corrigir a criança durante a escrita.
3. Solicite que a criança leia o que escreveu, apontando para a produção.
4. Na aplicação, avance para a tela de transcrição.
5. Preencha os dados da criança e transcreva as respostas.
6. Clique em **Analisar Nível**.
7. Consulte a hipótese apresentada, as habilidades BNCC, a intervenção sugerida e os materiais destacados.

## Como funciona a classificação

O motor de inferência está implementado em `app.py`. Ele normaliza as respostas (remove espaços, acentos e caracteres não alfabéticos) e aplica regras heurísticas às palavras **BORBOLETA**, **CAVALO** e **GATO**, considerando o comprimento da escrita e a correspondência com conjuntos de letras definidos no código.

As classificações das palavras são reunidas e o sistema escolhe a hipótese mais frequente (voto majoritário). Se não houver respostas consideradas, ou se a opção de rabiscos/garatujas estiver marcada, o resultado padrão é **Pré-silábica**.

Após a classificação, o sistema consulta `alfabetizacao.db`, que relaciona hipóteses a habilidades BNCC e intervenções pedagógicas.

## Banco de dados

O banco SQLite contém a tabela `niveis_alfabetizacao`, com os campos:

| Campo | Descrição |
|---|---|
| `id_nivel` | Identificador do registro (chave primária) |
| `hipotese` | Hipótese de escrita |
| `habilidade_bncc` | Códigos de habilidades relacionados |
| `intervencao_pedagogica` | Sugestões de atividades e estratégias |
| `indicador_avanco` | Indicador de avanço (armazenado no banco) |

Os dados iniciais são definidos no arquivo `gerar_db.py`.

## Materiais e referências

O projeto inclui documentos de referência relacionados à BNCC e às orientações sobre psicogênese, além de sugestões de materiais exibidas na interface.

## Limitações conhecidas

- A classificação é heurística e usa um conjunto restrito de palavras e regras; não representa uma avaliação pedagógica completa.
- Embora a interface solicite a transcrição de **RÃ**, o motor de inferência atualmente não utiliza essa resposta na classificação.
- A frase final indicada nas orientações não é transcrita nem avaliada pelo motor.
- Os dados de nome, idade e série são utilizados para exibição do resultado na interface, mas não fazem parte das regras de classificação.
- O resultado é uma hipótese automatizada e deve ser interpretado com cautela, considerando contexto, observações e outras produções da criança.

## Licença

Consulte o arquivo `LICENSE` para informações sobre a licença do projeto.
