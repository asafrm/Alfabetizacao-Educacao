# Motor de Inferência

O motor de inferência é responsável por processar os dados informados pelo usuário, aplicar as regras de classificação definidas no código e determinar a hipótese de escrita predominante do aluno. A implementação utiliza regras condicionais do tipo **SE... ENTÃO**, executadas de forma sequencial para cada palavra analisada.

## 1. Recebimento dos fatos de entrada

O sistema recebe os dados enviados pela interface, que podem incluir:

- A indicação de que o aluno utiliza apenas rabiscos (`apenas_rabiscos`);
- As escritas informadas para as palavras **BORBOLETA**, **CAVALO** e **GATO**.

Antes da análise, o sistema normaliza cada escrita: converte as letras para maiúsculas, remove espaços nas extremidades, elimina acentos e desconsidera caracteres que não sejam letras.

## 2. Aplicação das regras SE... ENTÃO...

Quando a opção de que o aluno utiliza apenas rabiscos está marcada:

- **SE** `apenas_rabiscos` for verdadeiro, **ENTÃO** o sistema define diretamente a hipótese como **Pré-silábica**.

Caso contrário, o motor analisa cada palavra preenchida. Para isso, consulta um gabarito interno que informa a quantidade de sílabas, o conjunto de letras consideradas na verificação sonora e a quantidade mínima de letras esperada para a classificação alfabética.

As regras são verificadas nesta ordem:

1. **Regra da hipótese alfabética**
   - **SE** a quantidade de letras for igual ou superior ao mínimo definido para a palavra **E** a taxa de correspondência sonora for igual ou superior a **70%**, **ENTÃO** classifica a escrita como **Alfabética**.

2. **Regra da hipótese silábica**
   - **SE** a quantidade de letras for igual à quantidade de sílabas **E** a taxa de correspondência sonora for igual ou superior a **50%**, **ENTÃO** classifica como **Silábica com valor sonoro**.
   - **SE** a quantidade de letras for igual à quantidade de sílabas **E** a taxa de correspondência sonora for inferior a **50%**, **ENTÃO** classifica como **Silábica sem valor sonoro**.

3. **Regra da hipótese silábico-alfabética**
   - **SE** a quantidade de letras for maior que a quantidade de sílabas **E** menor que o mínimo definido para a hipótese alfabética **E** a taxa de correspondência sonora for igual ou superior a **60%**, **ENTÃO** classifica como **Silábico-alfabética**.

4. **Regra padrão da hipótese pré-silábica**
   - **SE** nenhuma das condições anteriores for atendida, **ENTÃO** classifica como **Pré-silábica**.
   - **SE** a escrita estiver vazia após a limpeza do texto, **ENTÃO** também classifica aquela palavra como **Pré-silábica**.

A taxa de correspondência sonora é calculada pela proporção de letras da escrita que pertencem ao conjunto de letras aceitas no gabarito daquela palavra.

## 3. Definição da hipótese predominante

Depois de classificar individualmente as palavras preenchidas, o motor reúne os resultados e utiliza uma contagem de ocorrências (votação) para identificar a hipótese mais frequente.

- **SE** houver classificações para as palavras informadas, **ENTÃO** o sistema seleciona a hipótese que recebeu mais ocorrências.
- **SE** nenhuma palavra tiver sido preenchida, **ENTÃO** o sistema define a hipótese como **Pré-silábica**.

Na implementação atual, se houver empate na quantidade de ocorrências, é escolhida a primeira hipótese encontrada na ordem em que os resultados foram contabilizados.

## 4. Consulta à base de conhecimento

Depois de determinar a hipótese, o motor consulta o banco de dados SQLite, na tabela `niveis_alfabetizacao`, procurando o registro correspondente. A consulta recupera:

- A habilidade relacionada à **BNCC**;
- A intervenção pedagógica recomendada.

O campo `indicador_avanco` também existe na tabela do banco de dados, mas não é recuperado pela consulta utilizada atualmente pelo motor.

## 5. Exemplo do fluxo de inferência

Considere que o usuário informe uma escrita para uma ou mais das palavras disponíveis. O motor executa o seguinte processo:

1. Recebe as escritas enviadas pela interface.
2. Verifica se a opção **apenas rabiscos** foi selecionada.
3. Se não foi selecionada, analisa cada palavra preenchida e aplica, na ordem, as condições de classificação.
4. Reúne as hipóteses obtidas e conta quantas vezes cada uma aparece.
5. Seleciona a hipótese predominante.
6. Consulta o SQLite para obter a habilidade da BNCC e a intervenção pedagógica associadas.
7. Retorna o resultado à interface.

## 6. Características da implementação

O motor utiliza uma estratégia de **encadeamento de regras orientado pelos dados de entrada**: recebe os fatos, verifica as condições e produz uma classificação. Não se trata de encadeamento para trás, pois o sistema não parte de uma hipótese final para investigar quais fatos a comprovam.

A implementação também não registra uma trilha detalhada das regras acionadas. Os campos de palavras não preenchidos são ignorados na votação; não existe um mecanismo específico que represente ou preserve valores desconhecidos com o símbolo `?`.

> **Observação:** a classificação produzida é uma indicação baseada nas regras heurísticas implementadas e nos dados fornecidos. Ela serve como apoio ao acompanhamento pedagógico e não substitui a avaliação individual realizada por profissionais da educação.
