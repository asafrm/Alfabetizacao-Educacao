# Ética e Impactos da Inteligência Artificial

Análise ética do projeto Sistema Especialista – Alfabetização.

---

## 1. Análise ética do projeto

| Aspecto | Pergunta para orientar a análise |
| --- | --- |
| **Privacidade e dados** | Quais dados são utilizados? Podem identificar pessoas? É possível alcançar a finalidade com menos dados? |
| **Viés e equidade** | As regras, os dados ou os rótulos podem prejudicar algum grupo? Como a equipe verificará isso? |
| **Transparência** | Como a pessoa saberá que recebeu uma saída de IA? Que informações ajudarão a entender a recomendação? |
| **Supervisão e responsabilidade** | Quem revisa uma saída inadequada? Como a pessoa pode corrigir dados ou contestar a recomendação? |
| **Impacto social** | Quem se beneficia? Quem pode ser prejudicado se a recomendação estiver errada ou for tratada como definitiva? |

### Privacidade e dados

> Quais dados são utilizados? Podem identificar pessoas? É possível alcançar a finalidade com menos dados?

O sistema usa as respostas escritas pela criança em quatro palavras (ou a marcação de “apenas rabiscos”) e, no formulário, nome, idade e série, só para exibir o resultado. O servidor não grava esses dados: o banco `alfabetizacao.db` guarda apenas a base de conhecimento (hipóteses, habilidades da BNCC e intervenções). A análise em si não exige dado pessoal. As regras seguem as hipóteses de escrita de Ferreiro e Teberosky e as habilidades da BNCC da Educação Infantil. Reduzir as quatro palavras prejudicaria a classificação, porque o sistema compara o resultado entre palavras de tamanhos diferentes. Já o nome pode ser dispensado ou usado só na tela, sem ser enviado ao servidor.

### Viés e equidade

> As regras, os dados ou os rótulos podem prejudicar algum grupo? Como a equipe verificará isso?

As regras podem prejudicar crianças cuja escrita foge do padrão esperado. Isso inclui sotaques e variações regionais (por exemplo “borboleti” ou “cavalu”, cujas letras I e U o sistema nem sempre aceita), crianças bilíngues, com deficiência auditiva ou da fala, e com atraso motor. A faixa de idade e série não entra no cálculo, o que evita rotular por perfil. Outro risco é que resposta vazia vira “Pré-silábica” por padrão, e empates entre hipóteses são decididos de forma arbitrária. A equipe verificará isso testando o motor com grafias reais de turmas diferentes e conferindo com a avaliação do professor. Também deve ajustar os limites e letras aceitas por palavra quando houver divergência.

### Transparência

> Como a pessoa saberá que recebeu uma saída de IA? Que informações ajudarão a entender a recomendação?

O resultado aparece como “hipótese” e vem com explicação em linguagem simples, as habilidades da BNCC e a intervenção sugerida. O texto do sistema informa que ele é apoio à observação e não substitui o professor ou outros profissionais da educação.

### Supervisão e responsabilidade

> Quem revisa uma saída inadequada? Como a pessoa pode corrigir dados ou contestar a recomendação?

Quem decide é o professor, que revisa o resultado antes de qualquer ação e pode refazer a análise corrigindo a transcrição. A equipe responsável pelo sistema analisa saídas inadequadas relatadas pelos professores e corrige as regras.

### Impacto social

> Quem se beneficia? Quem pode ser prejudicado se a recomendação estiver errada ou for tratada como definitiva?

Beneficiam-se os professores, que ganham apoio para observar a escrita e planejar atividades, e as crianças, que podem receber intervenções mais adequadas. Podem ser prejudicadas as crianças classificadas de forma errada: um nível subestimado leva a atividades abaixo do que sabem, e um nível superestimado deixa passar dificuldades. Há risco maior se o resultado for tratado como definitivo, usado para rotular, comparar crianças ou informar famílias sem avaliação do professor. Por isso o sistema se apresenta como hipótese e orienta aplicar o teste periodicamente (o material de orientações indica bimestralmente) e não só uma vez.

---

## 2. Declaração de uso de sistemas de IA

### IA incorporada ao projeto

> O sistema não possui IA incorporada ao projeto

### IA utilizada na elaboração do trabalho

> Utilizei Claude para construção do frontend e material de apoio. Aproveitei o ditado de apoio (texto, lista de palavras com as regras ortográficas e gabarito), e arquivos index.html e style.css após ler o ditado e verifiquei a grafia e as regras de cada palavra com apoio de uma pedagoga. Assumo a responsabilidade pelas escolhas, verificações e conteúdo da entrega.
