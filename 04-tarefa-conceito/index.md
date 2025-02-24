# Conceito de tarefas

## Informações gerais

- Capítulo: [Conceito de tarefas](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-04.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: Gabrielle Fernandes Paiva Pereira
- matrícula: 20241014040003

## Respostas dos exercícios

### 1. O que significa *time-sharing* e qual a sua importância em um sistema operacional?
*Time-sharing* (compartilhamento de tempo) é uma técnica utilizada em sistemas operacionais que permite que múltiplos usuários ou processos compartilhem o mesmo recurso de processamento (CPU) de forma concorrente. Nesse modelo, o tempo de uso da CPU é dividido em pequenos intervalos chamados *quantum* ou fatias de tempo, e cada processo recebe uma dessas fatias em um ciclo contínuo. Isso cria a ilusão de que todos os processos estão sendo executados simultaneamente, mesmo em um sistema com apenas um núcleo de processamento.

A importância do *time-sharing* está na sua capacidade de aumentar a eficiência e a interatividade do sistema. Em ambientes multiusuário, como servidores ou sistemas operacionais modernos, ele garante que nenhum processo monopolize a CPU, permitindo que todos avancem de maneira justa. Além disso, melhora a experiência do usuário ao possibilitar a execução de várias tarefas ao mesmo tempo, como navegar na internet enquanto um programa roda em segundo plano. Esse conceito foi fundamental para a evolução dos sistemas operacionais, especialmente em mainframes e sistemas interativos.

---

### 2. Como e com base em que critérios é escolhida a duração de um *quantum* de processamento?
O *quantum* de processamento é o intervalo de tempo que um processo pode ocupar a CPU antes de ser preemptado (interrompido) para dar lugar a outro processo em um sistema com *time-sharing*. A escolha da duração do *quantum* é um equilíbrio delicado e depende de vários critérios:

- **Natureza das tarefas**: Em sistemas interativos (como desktops), um *quantum* menor (ex.: 10-100 milissegundos) é preferível para garantir respostas rápidas ao usuário. Já em sistemas batch (processamento em lote), um *quantum* maior pode ser usado para maximizar o desempenho de tarefas longas.
- **Overhead de troca de contexto**: Trocar de um processo para outro envolve salvar e restaurar o estado da CPU (contexto), o que consome tempo. Um *quantum* muito curto aumenta esse *overhead*, reduzindo a eficiência geral. Assim, ele deve ser longo o suficiente para justificar o custo da troca.
- **Equidade entre processos**: Um *quantum* adequado evita que processos fiquem esperando excessivamente, garantindo uma distribuição justa do tempo de CPU.
- **Carga do sistema**: Em sistemas com muitos processos, um *quantum* menor pode ser necessário para evitar atrasos perceptíveis, enquanto em sistemas com poucos processos, um *quantum* maior pode ser mais eficiente.

Na prática, o valor é ajustado pelo projetista do sistema operacional com base em testes e no tipo de uso esperado. Por exemplo, no Linux, o escalonador CFS (Completely Fair Scheduler) ajusta dinamicamente o *quantum* com base na carga e nas prioridades dos processos.

---

### 4. Indique se cada uma das transições de estado de tarefas a seguir definidas é possível ou não. Se a transição for possível, dê um exemplo de situação na qual ela ocorre (N: Nova, P: Pronta, E: Executando, S: Suspensa, T: Terminada).

Segue a análise das transições de estado possíveis no ciclo de vida de uma tarefa:

- **N → P**: Possível. Uma tarefa nova (N) torna-se pronta (P) quando o sistema operacional aloca os recursos necessários e a coloca na fila de prontos. *Exemplo*: Um programa é iniciado pelo usuário e aguarda sua vez de usar a CPU.
- **P → E**: Possível. Uma tarefa pronta (P) passa a executando (E) quando o escalonador a seleciona para usar a CPU. *Exemplo*: O sistema escolhe um processo da fila de prontos para rodar.
- **E → T**: Possível. Uma tarefa executando (E) vai para terminada (T) ao completar sua execução. *Exemplo*: Um programa finaliza seu cálculo e encerra.
- **E → S**: Possível. Uma tarefa executando (E) é suspensa (S) se precisa esperar por um evento externo. *Exemplo*: Um processo aguardando a leitura de um arquivo em disco é suspenso.
- **S → P**: Possível. Uma tarefa suspensa (S) volta a pronta (P) quando o evento que ela esperava ocorre. *Exemplo*: O arquivo solicitado é lido, e o processo está pronto para continuar.
- **N → E**: Impossível. Uma tarefa nova (N) não pode pular diretamente para executando (E) sem passar pelo estado pronto (P), pois precisa ser preparada pelo sistema antes.
- **T → P**: Impossível. Uma tarefa terminada (T) não retorna a pronta (P), pois seu ciclo de vida já acabou.
- **S → T**: Possível. Uma tarefa suspensa (S) pode ir para terminada (T) se for encerrada pelo sistema ou usuário antes de voltar a executar. *Exemplo*: Um processo em espera é manualmente finalizado pelo usuário.

---

### 5. Relacione as afirmações abaixo aos respectivos estados no ciclo de vida das tarefas (N: Nova, P: Pronta, E: Executando, S: Suspensa, T: Terminada):

Supondo algumas afirmações típicas (já que elas não foram fornecidas), associei exemplos comuns ao ciclo de vida das tarefas. Se você tiver afirmações específicas, posso ajustá-las:

1. "O processo está aguardando alocação de recursos pelo sistema operacional."  
   - **Estado**: N (Nova).  
   - *Justificativa*: Uma tarefa nova ainda não recebeu os recursos necessários para entrar na fila de prontos.

2. "O processo está na fila, aguardando sua vez de usar a CPU."  
   - **Estado**: P (Pronta).  
   - *Justificativa*: A tarefa está preparada e esperando o escalonador liberá-la para execução.

3. "O processo está atualmente utilizando a CPU."  
   - **Estado**: E (Executando).  
   - *Justificativa*: A tarefa foi escolhida e está em execução ativa na CPU.

4. "O processo está esperando a conclusão de uma operação de entrada/saída."  
   - **Estado**: S (Suspensa).  
   - *Justificativa*: A tarefa foi pausada para aguardar um evento externo, como I/O.

5. "O processo completou sua execução e liberou todos os recursos."  
   - **Estado**: T (Terminada).  
   - *Justificativa*: A tarefa terminou e não voltará a ser executada.

Se você fornecer as afirmações exatas, posso alinhar as respostas diretamente a elas!