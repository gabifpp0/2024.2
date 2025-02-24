# 2024.2 Avaliação do 1o período de Sistemas Operacionais

## Informações gerais
- **Objetivo do repositório**: Avaliação do 1o bimestre da Disciplina de sistemas operacionais do curso de TADS do IFRN-CNAT
- **Público alvo**: alunos da disciplina de SO (Sistemas Operacionais) do curso de TADS (Superior em Tecnologia em Análise e Desenvolvimento de Sistemas) no CNAT-IFRN (Instituto Federal de Educação, Ciência e Tecnologia do Rio Grande do Norte - Campus Natal-Central).
- disciplina: **SO** Sistemas Operacionais
- professor: [Leonardo A. Minora](https://github.com/leonardo-minora)
- aluno: Gabrielle Fernandes Paiva Pereira

## Avaliação
- **Lembre de fazer o fork deste repositório**
- As questões foram construídas com o auxílio do [copilot](https://copilot.microsoft.com/)

# Questão 1. Introdução a sistemas operacionais

Considere as funções e objetivos principais de um sistema operacional conforme discutido no texto. Explique como um sistema operacional gerencia os recursos de hardware e software de um computador para garantir eficiência e segurança. Em sua resposta, aborde os seguintes pontos:

- Gerenciamento de processos

O gerenciamento de processos é uma das funções mais essenciais de um sistema operacionais. 

Um processo é um programa em execução para se organizar ele possui estados de processo como: Novo, pronto, em exeução, bloqueado e finalizado. 

O sistema usa uma tabela de processos, para conseguir armazenar as informações de cada processos. Ele usa bloco de controle de processos (BCP) que contém as informações do processo e seu PID. Com essa tabela, o sistema operacional consegue controlar todos os processos e fornecer infomações de cada um para o escalonamento.

Ele usa mecanismos escalonamento para decidir qual processo será executado pela CPU.


- Gerenciamento de memória

O gerenciamento de memória se faz na memória principal e das interações de cache e memória secundária. Já os registardores é feito pelo compilador. Basicamente, o gerenciamento de memória é o controle de quais dados vão para a memória e de que forma vão ser armazenados.

O gerenciamento de memória mapeia os endereços de disco para endereçoes de memória através de mecanismos de endereçamento. 


- Gerenciamento de dispositivos de entrada e saída




- Gerenciamento de arquivos

O gerenciamento de arquivos é responsável pelo gerenciamento do conteúdo dos discos do sistema.

Ele mapeia quais blocos pertencem a quais arquivos. 




**Dica**: Pense em exemplos práticos de como o sistema operacional realiza essas tarefas no dia a dia de um usuário.

**Copilot informa**: Essa questão incentiva os alunos a explorarem os conceitos fundamentais e a aplicarem o conhecimento teórico em situações práticas. Se precisar de mais alguma coisa, estou aqui para ajudar!

**Resposta**:




# Questão 2. Estrutura de sistemas operacionais

## Texto informativo
### Estrutura de Sistemas Operacionais: Custo de Desenvolvimento e Segurança da Informação

A estrutura de um sistema operacional (SO) é fundamental para determinar tanto o custo de desenvolvimento e manutenção quanto a segurança da informação. Existem várias arquiteturas de SO, como monolítica, microkernel e em camadas, cada uma com suas próprias implicações em termos de custo e segurança.

#### Custo de Desenvolvimento e Manutenção

1. **Arquitetura Monolítica**:
   - **Desenvolvimento**: Geralmente, mais rápida de desenvolver inicialmente, pois todos os componentes do SO são integrados em um único bloco de código.
   - **Manutenção**: Pode ser mais complexa e cara, pois qualquer alteração em um componente pode afetar todo o sistema, exigindo testes extensivos e cuidadosos.

2. **Arquitetura Microkernel**:
   - **Desenvolvimento**: Pode ser mais demorada e cara inicialmente, pois envolve a criação de um núcleo mínimo e a implementação de serviços adicionais como processos separados.
   - **Manutenção**: Mais fácil e menos custosa, já que os componentes são isolados. Atualizações e correções podem ser feitas em módulos específicos sem impactar o núcleo do sistema.

3. **Arquitetura em Camadas**:
   - **Desenvolvimento**: Moderadamente complexa, pois cada camada deve ser bem definida e interagir corretamente com as outras.
   - **Manutenção**: Relativamente fácil, pois problemas podem ser isolados e corrigidos em camadas específicas sem afetar o restante do sistema.

#### Segurança da Informação

1. **Arquitetura Monolítica**:
   - **Segurança**: Pode ser mais vulnerável, pois uma falha em qualquer parte do sistema pode comprometer todo o SO. A integração de todos os componentes em um único bloco de código pode dificultar a implementação de medidas de segurança robustas.

2. **Arquitetura Microkernel**:
   - **Segurança**: Geralmente mais segura, pois isola os serviços em processos separados. Isso limita o impacto de uma falha ou ataque a um único componente, protegendo o núcleo do sistema e outros serviços.

3. **Arquitetura em Camadas**:
   - **Segurança**: Oferece um bom equilíbrio, pois cada camada pode implementar suas próprias medidas de segurança. No entanto, a comunicação entre camadas deve ser cuidadosamente gerenciada para evitar vulnerabilidades.

### Conclusão

A escolha da arquitetura de um sistema operacional tem um impacto significativo tanto no custo de desenvolvimento e manutenção quanto na segurança da informação. Arquiteturas monolíticas podem ser mais rápidas e baratas de desenvolver inicialmente, mas podem acarretar custos de manutenção mais altos e maiores riscos de segurança. Por outro lado, arquiteturas microkernel e em camadas podem exigir um investimento inicial maior, mas oferecem vantagens em termos de manutenção e segurança.

## Questão
Com base no texto sobre a estrutura de sistemas operacionais, analise como as diferentes arquiteturas (monolítica, microkernel e camadas) impactam o custo com a equipe de desenvolvimento e a segurança do sistema operacional. Em sua resposta, considere os seguintes pontos:
- Complexidade de implementação e manutenção
- Necessidade de especialização da equipe
- Potenciais vulnerabilidades de segurança
- Facilidade de atualização e correção de falhas


**Resposta**:
- Monlítica:
Complexidade: A arquitetura monolítica possuí uma complexidade baixa de implementação pois a maioria dos componentes do sistemas operacinal são integrados em um único bloco. Mas possui uma complexidade alta de manutenção pois a alteração de um módulo pode afetar todo o sistema.
Necessidade de espacialização: A necessidade de especialização por equipe são altas para desenvolver um alto nível de especialização para identificar problemas e realizar alterações sem causar grandes impactos no sistema.
Segurança: Há grandes vulnerabilidades de segurança pelo fato dos módulos não possuírem isoloamento entre eles. Uma falha em módulo pode afetar todo o sistema.
- Facilidade de atualização e correção de falhas: A facilidade de atualização de correção de falhas são baixas pois qualquer correção ou atualização exige a recompilação e redistribuição de todo o sistema.

- Microkernel:
Complexidade: A arquitetura microkernel possui uma complexidade alta pois se faz necessário a separação dos serviços do sistema operacional em processos independentes. Já para a manutenção a complexidade é baixa já que os serviços são isolados assim permitindo um manuseio sem grande impacto no sistema.
Necessidade de espacialização: A necessidade de especialização por equipe são altas para o manuseio de interprocessos e garantir o desempemho e estabilidade do sistema.
Segurança: Não há grandes vulnerabilidades de segurança devido ao isolamento entre os serviços, assim o manuseio de um módulo não afeta outro ou o sistema num geral.
- Facilidade de atualização e correção de falhas: A facilidade de atualização de correção de falhas são altas pois os serviços podem ser atualizados isoladamente.                         

- Em camadas
Complexidade: A arquitetura monolítica possuí uma complexidade moderada de implementação pois demanda de um planejamento mais estruturado. Já a manutenção ela pode ser considerada simples pois a alterações podem ser feitas isoladamente.
Necessidade de espacialização: A necessidade de especialização por equipe é moderada, a especialização é menor do que a do microkernel mas maior que a monolítica. Se tem a necessidade de especialização em interação entre camadas.
Segurança: Há um vulnerabilidade moderada de segurança mas o manuseio entre camadas deve ser gerenciada com cuidado para evitar falhas.            
- Facilidade de atualização e correção de falhas: 


**Dica:** Utilize exemplos de sistemas operacionais reais que adotam essas arquiteturas para ilustrar sua análise.

**Copilot informa**: Essa questão incentiva os alunos a considerarem tanto os aspectos econômicos quanto os de segurança ao avaliar diferentes arquiteturas de sistemas operacionais.

# Questão 3. Introdução à Segurança de Sistemas Operacionais

## Texto informativo

A segurança de um sistema operacional é um aspecto crucial que visa proteger os recursos do sistema contra acessos não autorizados, ataques maliciosos e falhas. Um sistema operacional seguro deve garantir a integridade, confidencialidade e disponibilidade dos dados e serviços. Para alcançar esses objetivos, várias técnicas e mecanismos são implementados, incluindo:

1. **Controle de Acesso**: Define quem pode acessar o sistema e quais recursos podem ser utilizados. Isso é feito através de autenticação (verificação de identidade) e autorização (permissão de acesso).

2. **Criptografia**: Utilizada para proteger dados em trânsito e em repouso, garantindo que apenas usuários autorizados possam acessar informações sensíveis.

3. **Auditoria e Monitoramento**: Registra atividades do sistema para detectar e responder a comportamentos suspeitos ou anômalos.

4. **Isolamento de Processos**: Garante que os processos sejam executados em ambientes isolados, evitando que um processo comprometa a segurança de outro.

5. **Atualizações e Patches**: Manter o sistema operacional atualizado é essencial para corrigir vulnerabilidades conhecidas e proteger contra novas ameaças.


## Questão

Considerando os mecanismos de segurança discutidos, analise como a implementação de controles de acesso e criptografia pode impactar a performance e a usabilidade de um sistema operacional. Em sua resposta, aborde os seguintes pontos:
- Benefícios e desafios de cada mecanismo
- Impacto na experiência do usuário
- Exemplos de situações onde esses mecanismos são críticos


 **Resposta**:
- Controle de acesso:
Benefícios: Os benefícios do controle de acesso são uma segurança mais aprimorada e redução de riso de ataques maliciosos
Desafios: Um dos principais desafios são a complexidade de implementar 
Impacto: Um impacto que pode ser gerado é uma certa frustração no uso dos usuários
Exemplos: Um exemplo de situação onde esses mecanismos podem ser críticos, é quandom se tem o manuseio de quando quantidades de dados sensíveis

- Cripitografia:
Benefícios: Um dos maiores benefícios da criptografia é sua confencialidade de dados, onde se protege dados armazenados contra acesso não autorizado
Desafios: Um dos grandes desafios da criptografia é se mal configurada a chave pode ser perdida ou comprometida. E outro desafio é o alto consumo de recursos.
Impacto: Um dos impactos prováveis é a redução de desempenho 
Exemplos: Comunicação segura entre clientes e servidores


**Dica:** Pense em como esses mecanismos são aplicados em sistemas operacionais que você utiliza no dia a dia, como Windows, Linux ou macOS.

**Copilot informa**: Essa questão incentiva os alunos a refletirem sobre o equilíbrio entre segurança, performance e usabilidade, aplicando conceitos teóricos a contextos práticos.


# Questão 4. Custo de Processamento versus Algoritmo Ótimo de Escalonamento

## Texto informativo

O escalonamento de processos é uma função crítica de um sistema operacional, responsável por determinar a ordem em que os processos são executados pelo processador. O objetivo é maximizar a eficiência do sistema, garantindo que os recursos sejam utilizados de maneira justa e eficaz. No entanto, encontrar o algoritmo de escalonamento ótimo envolve um equilíbrio delicado entre o custo de processamento e a eficiência do escalonamento.

### Custo de Processamento

O custo de processamento refere-se ao tempo e aos recursos necessários para executar um algoritmo de escalonamento. Algoritmos mais complexos podem oferecer melhores resultados em termos de tempo de resposta e utilização do processador, mas também podem exigir mais recursos computacionais para tomar decisões de escalonamento. Isso pode incluir tempo de CPU, memória e outras operações de sistema.

### Algoritmo Ótimo de Escalonamento

Um algoritmo ótimo de escalonamento é aquele que maximiza a eficiência do sistema operacional, minimizando o tempo de espera dos processos, o tempo de resposta e o tempo de retorno. Alguns dos algoritmos de escalonamento mais comuns incluem:

- **First-Come, First-Served (FCFS)**: Simples e fácil de implementar, mas pode levar a longos tempos de espera para processos curtos.
- **Shortest Job Next (SJN)**: Minimiza o tempo médio de espera, mas pode ser difícil de implementar devido à necessidade de prever o tempo de execução dos processos.
- **Round Robin (RR)**: Oferece uma abordagem justa, atribuindo fatias de tempo iguais a todos os processos, mas pode resultar em maior sobrecarga de contexto.
- **Priority Scheduling**: Processos com maior prioridade são executados primeiro, mas pode levar à inanição de processos de baixa prioridade.

## Questão

Considerando os conceitos de custo de processamento e algoritmo ótimo de escalonamento, analise como diferentes algoritmos de escalonamento podem impactar a performance de um sistema operacional em termos de tempo de resposta, tempo de espera e utilização do processador. Em sua resposta, aborde os seguintes pontos:
- Vantagens e desvantagens de pelo menos dois algoritmos de escalonamento
- Impacto do custo de processamento na escolha do algoritmo
- Exemplos de situações onde um algoritmo pode ser preferível a outro

**Resposta**:
-Firts-Come, First-Served:
Vantagens: Facilidade de implementação e baixo custo de processamento
Desvantagens: Pode haver um atraso de execução por processos longos
Custo de processamento: Baixo custo de processamento pois o algoritmo se baseia suas decisões pela ordem de chegada
Exemplos; Impressora em lote

-Shortest Job Next
Vantagens: Tem uma ótima utilização do processador e seu tempo de execução
Desvantagens:
Custo de processamento: Consideravelmente alto, dependendo do método em processamento
Exemplo: Gerenciamento de pequenas requisições HTTP


**Dica:** Pense em como esses algoritmos são aplicados em diferentes cenários, como sistemas de tempo real, servidores web e sistemas operacionais de uso geral.

**Copilot informa**: Essa questão incentiva os alunos a refletirem sobre a complexidade e os trade-offs envolvidos na escolha de um algoritmo de escalonamento, aplicando conceitos teóricos a contextos práticos.

# Questão 5. Aplicativo em python vs aplicativos em c

## Questão

Explique o caminho que as instruções seguem desde um aplicativo escrito em Python e um aplicativo escrito em linguagem C até serem executadas pelo hardware. Em sua resposta, considere os seguintes pontos:
- O papel do interpretador no caso do Python
- O processo de compilação no caso do C
- A interação entre o kernel do sistema operacional e os drivers de dispositivo
- A tradução final das instruções para o formato binário (0 e 1) executado pelo hardware

**Resposta**: 
Aplicativo em Python:
1. O interpretador lê o código fonte e converte as instruções em bytecode
2. Esse bytecode é armazenado em um arquivo .pyc 
3. Esse arquivo será processado pelo interpretador na execução
4. O interpretador pytohn ele age como uma máquina virtual
5. Ele interaje diretamente com o kernel do sistema operacional
6. As intruções do kernel são convertidas em código binário

Aplicativo em C:
1.O código é processado pelo compilador.
2. Ele traduz o código para a linguagem mais próxima das instruções da máquina.
3. Ele converte o código em código objeto.
4. Junta os arquivos objeto e com isso gera um arquivo executável.
5. Quando o programa é iniciado, o S.O carrega o executável na memória.
6. O kernerl e os drivers convertem as chamadas do programa em instruções.
7. Essas instruções são executadas pela CPU


**Dica:** Compare e contraste os dois processos, destacando as principais diferenças e semelhanças na forma como as instruções são processadas e executadas.

**Copilot informa**: Essa questão incentiva os alunos a refletirem sobre os diferentes caminhos que as instruções seguem em linguagens interpretadas e compiladas, aplicando conceitos teóricos a contextos práticos.
