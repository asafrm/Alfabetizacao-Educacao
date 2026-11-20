# Motor de Inferência

O motor de inferência é responsável por analisar as respostas inseridas
no sistema e aplicar as regras de produção do tipo **SE... ENTÃO**,
definidas a partir dos critérios presentes na base de conhecimento. Seu
funcionamento utiliza uma abordagem baseada em regras condicionais, nas
quais cada condição verificada corresponde a uma possível hipótese de
escrita, permitindo identificar o nível de alfabetização apresentado
pelo aluno.

## 1. Identificação da hipótese inicial

Primeiramente, o sistema verifica se o aluno informou que realiza apenas
rabiscos, sem utilizar letras ou outros elementos que representem uma
tentativa de escrita. Nesse caso, o motor aplica diretamente a seguinte
regra:

-   **SE** o aluno utiliza apenas rabiscos, **ENTÃO** sua hipótese de
    escrita é classificada como **Pré-silábica**.

## 2. Análise das palavras

Caso contrário, o sistema analisa as palavras escritas pelo aluno,
utilizando um gabarito interno que contém a quantidade de sílabas, os
caracteres aceitos na análise sonora e a quantidade mínima de letras
esperada para a classificação alfabética.

Para cada palavra, o motor verifica o tamanho da escrita e a
correspondência entre as letras utilizadas e os sons esperados. A partir
dessas informações, aplica as seguintes regras:

-   **SE** a quantidade de letras atingir o mínimo estabelecido para a
    palavra e a correspondência sonora for igual ou superior a **70%**,
    **ENTÃO** classifica como **Alfabética**.
-   **SE** a quantidade de letras corresponder exatamente à quantidade
    de sílabas e a correspondência sonora for igual ou superior a
    **50%**, **ENTÃO** classifica como **Silábica com valor sonoro**.
-   **SE** a quantidade de letras corresponder exatamente à quantidade
    de sílabas, mas a correspondência sonora for inferior a **50%**,
    **ENTÃO** classifica como **Silábica sem valor sonoro**.
-   **SE** a quantidade de letras for superior à quantidade de sílabas,
    mas inferior ao mínimo estabelecido para a hipótese alfabética, e a
    correspondência sonora for igual ou superior a **60%**, **ENTÃO**
    classifica como **Silábico-alfabética**.
-   **SE** nenhuma das condições anteriores for atendida, **ENTÃO**
    classifica como **Pré-silábica**.

## 3. Definição da hipótese predominante

Após analisar individualmente as palavras informadas, o motor reúne as
classificações obtidas e utiliza um mecanismo de votação para
identificar a hipótese de escrita mais frequente. Dessa forma, a
classificação final considera a predominância dos resultados encontrados
nas palavras analisadas.

## 4. Consulta à base de conhecimento

Com a hipótese de escrita definida, o motor realiza uma consulta ao
banco de dados SQLite, buscando as informações pedagógicas
correspondentes à classificação identificada. Essa consulta retorna:

-   Habilidades relacionadas à **BNCC**;
-   Intervenções pedagógicas recomendadas;
-   Indicadores de avanço na aprendizagem.

Assim, o motor de inferência transforma as informações inseridas pelo
usuário em uma hipótese de escrita e, posteriormente, associa essa
classificação a orientações pedagógicas, tornando o resultado mais útil
para o acompanhamento do desenvolvimento do aluno.

## 5. Fluxo resumido do funcionamento

1.  **Entrada de dados:** escrita das palavras ou identificação de
    rabiscos.
2.  **Aplicação das regras SE... ENTÃO:** análise da quantidade de
    letras, sílabas e correspondência sonora.
3.  **Votação das hipóteses:** identificação da classificação
    predominante.
4.  **Consulta ao SQLite:** recuperação das habilidades da BNCC e das
    intervenções pedagógicas.
5.  **Resultado da inferência:** apresentação da hipótese de escrita e
    das orientações pedagógicas.

> **Observação técnica:** os percentuais e critérios descritos
> correspondem às condições apresentadas na lógica de implementação. A
> classificação é heurística e indicativa, não substituindo uma
> avaliação pedagógica individualizada.
