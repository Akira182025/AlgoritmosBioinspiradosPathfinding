# Comparação de Algoritmos Bioinspirados para Pathfinding em Ambiente 2D

**Disciplina:** Algoritmos Bioinspirados

**Equipe:** Akira Higa, Fernando de Souza Batista

## Problema

Agentes autônomos, personagens de jogos e sistemas de navegação precisam encontrar caminhos entre uma posição inicial e um destino, muitas vezes em ambientes que possuem obstáculos e restrições de movimentação.

Em um ambiente representado por uma grade bidimensional, encontrar um caminho válido pode parecer simples em mapas pequenos. Entretanto, conforme a quantidade de posições possíveis e obstáculos aumenta, o espaço de busca também cresce, tornando interessante a utilização de técnicas de otimização e busca.

O problema deste projeto consiste em fazer com que um agente encontre um caminho entre um ponto inicial e um ponto objetivo em uma grade 2D com obstáculos, buscando minimizar o custo do percurso.

Essa abordagem permite analisar diferentes algoritmos bioinspirados sob as mesmas condições e observar como cada método se comporta diante de um problema de otimização discreta.

Entre os principais desafios estão:

* encontrar um caminho válido entre origem e destino;
* evitar obstáculos;
* minimizar o número de movimentos;
* reduzir colisões e movimentos inválidos;
* explorar diferentes possibilidades de caminho;
* evitar convergência prematura;
* comparar diferentes estratégias de otimização;
* analisar a velocidade de convergência;
* avaliar a estabilidade dos resultados;
* comparar qualidade das soluções e tempo de execução.

## Proposta

Desenvolver uma aplicação capaz de utilizar diferentes algoritmos bioinspirados para solucionar um problema de pathfinding em uma grade bidimensional contendo obstáculos.

O projeto utilizará o **Ant Colony Optimization (ACO)** como principal algoritmo, acompanhado pelos algoritmos **Cuckoo Search** e **Grey Wolf Optimizer (GWO)**.

Além dos algoritmos bioinspirados, serão utilizados **Genetic Algorithm (GA)**, **Particle Swarm Optimization (PSO)** e **Random Search** como métodos de comparação.

A aplicação permitirá executar os algoritmos individualmente, visualizar os caminhos encontrados, realizar múltiplas execuções para obtenção de resultados estatísticos e gerar gráficos para comparação.

A ideia central é verificar como diferentes estratégias de busca e otimização se comportam diante do mesmo problema, considerando fatores como qualidade da solução, taxa de sucesso, convergência e tempo de execução.

O projeto também contará com uma representação visual utilizando **Pygame**, permitindo observar o agente percorrendo o caminho encontrado no mapa.

## Objetivo geral

Desenvolver e avaliar uma solução computacional baseada em algoritmos bioinspirados para encontrar caminhos em um ambiente 2D com obstáculos, comparando diferentes técnicas de otimização por meio de métricas de desempenho, qualidade das soluções e análise estatística.

## Objetivos específicos

* Representar um ambiente 2D por meio de uma grade.
* Definir uma posição inicial e uma posição objetivo.
* Inserir obstáculos no ambiente de busca.
* Implementar uma função de avaliação para medir a qualidade dos caminhos.
* Implementar o algoritmo Ant Colony Optimization (ACO).
* Implementar o algoritmo Cuckoo Search.
* Implementar o algoritmo Grey Wolf Optimizer (GWO).
* Implementar um Genetic Algorithm (GA) como baseline.
* Implementar Particle Swarm Optimization (PSO) como baseline.
* Implementar Random Search como baseline.
* Utilizar uma representação baseada em movimentos discretos.
* Permitir que os algoritmos encontrem caminhos entre origem e destino.
* Penalizar caminhos que não atingem o objetivo.
* Penalizar colisões e movimentos inválidos.
* Medir o comprimento dos caminhos encontrados.
* Calcular a taxa de sucesso de cada algoritmo.
* Medir o tempo de execução.
* Analisar a convergência dos algoritmos.
* Executar múltiplas rodadas para reduzir a influência da aleatoriedade.
* Calcular média e desvio padrão dos resultados.
* Utilizar testes estatísticos para comparar os resultados.
* Gerar gráficos de comparação.
* Disponibilizar uma visualização do caminho utilizando Pygame.
* Analisar as limitações e características de cada abordagem.

## Algoritmos utilizados

O projeto utiliza seis métodos para realizar a comparação.

### Ant Colony Optimization — ACO

O **Ant Colony Optimization (ACO)** é o principal algoritmo utilizado no projeto.

Sua inspiração vem do comportamento de colônias de formigas durante a busca por caminhos entre o formigueiro e uma fonte de alimento.

Durante o processo de busca, as formigas depositam feromônio nos caminhos percorridos. Caminhos considerados melhores recebem maior reforço, aumentando a probabilidade de serem escolhidos posteriormente.

No projeto, o feromônio é associado às possíveis transições entre células da grade.

O algoritmo utiliza:

* feromônio;
* evaporação;
* reforço dos melhores caminhos;
* informação heurística baseada na distância até o objetivo;
* seleção probabilística dos movimentos.

O ACO é particularmente adequado para este problema porque trabalha naturalmente com decisões de caminho em um espaço discreto.

### Cuckoo Search

O **Cuckoo Search** é inspirado no comportamento de algumas espécies de cucos e na estratégia de deposição de ovos em ninhos hospedeiros.

O algoritmo utiliza movimentos baseados em **Lévy flights**, permitindo realizar saltos de diferentes magnitudes no espaço de busca.

No projeto, essa característica é utilizada para aumentar a exploração de diferentes soluções e evitar que a busca fique limitada a uma região muito pequena do espaço de soluções.

### Grey Wolf Optimizer — GWO

O **Grey Wolf Optimizer** é inspirado na estrutura social e no comportamento de caça de lobos-cinzentos.

As soluções são organizadas de acordo com sua qualidade e as três melhores soluções assumem os papéis de:

* Alpha;
* Beta;
* Delta.

As demais soluções atualizam suas posições utilizando informações dessas três soluções líderes.

O objetivo é equilibrar exploração e aproveitamento das regiões promissoras do espaço de busca.

### Genetic Algorithm — GA

O **Genetic Algorithm** é utilizado como uma das abordagens de comparação.

O algoritmo utiliza conceitos inspirados na evolução biológica, trabalhando com uma população de soluções.

As principais operações utilizadas são:

* seleção;
* elitismo;
* crossover;
* mutação.

Cada indivíduo representa uma sequência de movimentos que pode ser utilizada pelo agente para tentar chegar ao objetivo.

### Particle Swarm Optimization — PSO

O **Particle Swarm Optimization** é inspirado no comportamento coletivo de grupos de partículas.

Cada partícula representa uma possível solução e utiliza informações relacionadas à sua melhor posição encontrada e à melhor posição encontrada pelo grupo.

No projeto, o PSO trabalha com uma representação contínua que posteriormente é convertida em movimentos discretos da grade.

### Random Search

O **Random Search** é utilizado como baseline.

Nesse método, soluções são geradas aleatoriamente sem utilizar mecanismos de aprendizagem ou informação histórica.

Sua função no projeto é fornecer uma referência simples para avaliar se os algoritmos de otimização conseguem obter resultados melhores do que uma busca puramente aleatória.

## Representação do problema

O ambiente é representado por uma grade bidimensional de:

```text
20 x 20
```

A posição inicial é:

```text
(0, 0)
```

O objetivo é:

```text
(19, 19)
```

As células do ambiente podem representar:

* posição livre;
* obstáculo;
* posição inicial;
* objetivo;
* caminho encontrado.

A movimentação do agente utiliza quatro ações:

```text
0 = direita
1 = esquerda
2 = baixo
3 = cima
```

Dessa forma, uma solução pode ser representada como uma sequência de movimentos.

Por exemplo:

```text
[0, 0, 2, 2, 0, 2, 0]
```

representa uma sequência de movimentos realizados pelo agente.

## Função de Fitness

A função de fitness é utilizada para medir a qualidade de cada solução.

Neste projeto, **quanto menor o fitness, melhor a solução**.

Quando o agente consegue chegar ao objetivo, o fitness considera principalmente o número de passos necessários para completar o caminho.

Também são consideradas colisões.

Quando o agente não consegue alcançar o objetivo dentro do limite estabelecido, são aplicadas penalizações.

A avaliação considera:

* quantidade de movimentos;
* distância restante até o objetivo;
* colisões;
* movimentos inválidos;
* chegada ou não ao objetivo.

Para soluções que não alcançam o destino, uma penalização adicional é aplicada para garantir que soluções válidas sejam favorecidas.

## Critérios de sucesso

Uma solução é considerada bem-sucedida quando o agente:

1. inicia na posição definida;
2. realiza uma sequência válida de movimentos;
3. evita os obstáculos;
4. alcança a posição objetivo dentro do limite de movimentos.

O sistema registra se a solução foi capaz de atingir o objetivo por meio da variável:

```text
success
```

## Métricas

Para comparar os algoritmos, serão utilizadas diferentes métricas.

### Fitness

Representa o custo total da solução.

Quanto menor o valor, melhor.

### Comprimento do caminho

Representa a quantidade de movimentos necessários para alcançar o objetivo.

Caminhos menores são considerados soluções com menor custo de deslocamento.

### Taxa de sucesso

Representa a porcentagem de execuções em que o algoritmo conseguiu encontrar um caminho até o objetivo.

A métrica é calculada como:

```text
Taxa de sucesso =
(execuções com sucesso / total de execuções) × 100
```

### Tempo de execução

Mede o tempo necessário para o algoritmo executar sua busca.

O tempo é registrado utilizando o relógio de alta precisão disponível no Python.

### Convergência

A convergência permite observar como o melhor fitness encontrado evolui ao longo das gerações ou iterações.

Um algoritmo que reduz rapidamente o fitness pode apresentar uma convergência mais rápida, enquanto outro pode precisar de mais iterações para atingir soluções semelhantes.

## Experimentos

Para reduzir a influência da aleatoriedade, cada algoritmo será executado várias vezes.

O benchmark padrão utiliza:

```text
30 execuções
```

Cada execução utiliza:

```text
30 indivíduos
```

e:

```text
60 gerações
```

A utilização de múltiplas execuções permite observar não apenas uma solução isolada, mas o comportamento do algoritmo ao longo de diferentes execuções.

Os resultados são armazenados em:

```text
results/results.csv
```

## Análise estatística

Após a execução do benchmark, os resultados são consolidados para calcular estatísticas descritivas.

São calculados:

* média do fitness;
* desvio padrão do fitness;
* média do tempo;
* desvio padrão do tempo;
* taxa de sucesso;
* média do comprimento do caminho;
* desvio padrão do comprimento do caminho.

Também é utilizado o teste de **Mann-Whitney U** para realizar comparações estatísticas entre pares de algoritmos.

O teste permite verificar diferenças entre as distribuições dos resultados obtidos pelas diferentes técnicas.

Os resultados estatísticos são armazenados em:

```text
results/statistical_tests.csv
```

## Visualização

O projeto possui duas formas principais de visualização.

### Mapa no terminal

O mapa pode ser exibido diretamente no terminal utilizando caracteres.

A representação utiliza:

```text
S = início
G = objetivo
# = obstáculo
* = caminho
. = espaço livre
```

Exemplo:

```text
S . . . # . . . . .
. . . . # . . . . .
. . . . # . . . . .
. . . . # . . . . .
. . . . . . . . . .
. . . . . . . . . .
```

### Pygame

O projeto também possui uma visualização gráfica utilizando Pygame.

Na visualização:

* o início é representado em verde;
* o objetivo é representado em vermelho;
* os obstáculos são representados em cinza;
* o caminho encontrado é representado em azul;
* o agente é representado em preto.

A visualização permite acompanhar o agente percorrendo o caminho encontrado pelo algoritmo.

## Gráficos

Os resultados dos experimentos podem ser apresentados por meio de gráficos.

O projeto gera gráficos relacionados a:

* fitness médio;
* taxa de sucesso;
* tempo médio de execução;
* convergência.

Os arquivos são armazenados em:

```text
results/graphs/
```

Os gráficos gerados são:

```text
fitness_medio.png
taxa_sucesso.png
tempo_medio.png
convergencia.png
```

## Tecnologias utilizadas

### Python

Linguagem principal utilizada no desenvolvimento do projeto.

### NumPy

Utilizado para operações numéricas, geração de soluções e manipulação dos vetores utilizados pelos algoritmos.

### Pygame

Utilizado para a visualização gráfica do agente e do caminho encontrado.

### Matplotlib

Utilizado para geração dos gráficos dos experimentos.

### SciPy

Utilizado para realização dos testes estatísticos.

### Pandas

Utilizado para leitura, processamento e organização dos resultados experimentais.

## Estrutura do projeto

```text
projeto_algoritmos_bioinspirados/
│
├── main.py
├── config.py
├── grid.py
├── fitness.py
├── utils.py
├── requirements.txt
├── README.md
│
├── algorithms/
│   ├── __init__.py
│   ├── aco.py
│   ├── cuckoo.py
│   ├── gwo.py
│   ├── ga.py
│   ├── pso.py
│   └── random_search.py
│
├── experiments/
│   ├── __init__.py
│   ├── benchmark.py
│   └── statistics.py
│
├── visualization/
│   ├── __init__.py
│   ├── game.py
│   └── plots.py
│
└── results/
```

## Organização dos módulos

### `main.py`

Responsável pelo menu principal e pela integração dos componentes do projeto.

Permite:

* mostrar o mapa;
* executar algoritmos;
* executar benchmark;
* gerar estatísticas;
* gerar gráficos;
* abrir a visualização Pygame.

### `config.py`

Centraliza os parâmetros utilizados no projeto.

Contém:

* dimensões da grade;
* início;
* objetivo;
* obstáculos;
* número máximo de passos;
* tamanho da população;
* número de gerações;
* número de execuções;
* penalizações;
* sementes aleatórias.

### `grid.py`

Implementa a estrutura da grade.

É responsável por:

* verificar posições;
* identificar obstáculos;
* verificar movimentos válidos;
* retornar vizinhos;
* exibir o mapa.

### `fitness.py`

Implementa a simulação do agente e a função de avaliação das soluções.

### `utils.py`

Contém funções auxiliares para geração e manipulação das soluções.

### `algorithms/`

Contém as implementações dos algoritmos utilizados no projeto.

### `experiments/`

Contém os módulos responsáveis pelo benchmark e pela análise estatística.

### `visualization/`

Contém os módulos responsáveis pela visualização Pygame e pelos gráficos.

## Execução

Primeiramente, é necessário instalar as dependências.

No terminal do VS Code:

```bash
python -m pip install -r requirements.txt
```

No Windows, caso necessário:

```bash
py -m pip install -r requirements.txt
```

Depois:

```bash
python main.py
```

ou:

```bash
py main.py
```

## Menu da aplicação

Ao executar o programa, será apresentado:

```text
======================================================================
   ALGORITMOS BIOINSPIRADOS - PATHFINDING
======================================================================

1 - Mostrar mapa
2 - Executar um algoritmo
3 - Executar benchmark
4 - Gerar estatísticas e testes
5 - Gerar gráficos
6 - Abrir demonstração Pygame
0 - Sair
```

### Opção 1 — Mostrar mapa

Exibe a grade no terminal.

### Opção 2 — Executar um algoritmo

Permite selecionar um dos seis algoritmos e executar uma busca individual.

Ao final são apresentados:

* fitness;
* sucesso;
* passos;
* colisões;
* avaliações;
* caminho encontrado.

### Opção 3 — Executar benchmark

Executa os seis algoritmos durante as 30 rodadas definidas na configuração.

Os resultados são armazenados no arquivo:

```text
results/results.csv
```

### Opção 4 — Gerar estatísticas e testes

Processa os resultados do benchmark e gera:

```text
results/summary.csv
```

e:

```text
results/statistical_tests.csv
```

### Opção 5 — Gerar gráficos

Gera os gráficos de comparação e convergência.

### Opção 6 — Abrir demonstração Pygame

Permite selecionar um algoritmo e visualizar o caminho encontrado em uma interface gráfica.

## Fluxo recomendado

Para utilizar o projeto, recomenda-se seguir a sequência:

```text
1. Mostrar mapa
       ↓
2. Executar um algoritmo
       ↓
3. Testar a visualização Pygame
       ↓
4. Executar benchmark
       ↓
5. Gerar estatísticas
       ↓
6. Gerar gráficos
```

## Resultados esperados

A análise experimental permitirá observar diferenças entre os algoritmos em relação a:

* qualidade dos caminhos;
* quantidade de soluções bem-sucedidas;
* quantidade de movimentos;
* número de colisões;
* tempo de execução;
* comportamento de convergência;
* variabilidade entre diferentes execuções.

Os resultados obtidos serão utilizados para discutir as características de cada algoritmo no contexto específico do problema de pathfinding.

A comparação será baseada nos dados experimentais obtidos pelas execuções, evitando conclusões baseadas em apenas uma execução individual.

## Reprodutibilidade

O projeto utiliza sementes aleatórias para permitir maior reprodutibilidade dos experimentos.

A configuração principal utiliza:

```text
SEED = 42
```

Além disso, diferentes sementes são utilizadas entre as execuções do benchmark para permitir que os algoritmos sejam avaliados em diferentes condições aleatórias.

## Considerações sobre a representação

O problema utiliza uma representação baseada em uma grade discreta porque o objetivo é trabalhar diretamente com decisões de movimentação entre células.

Essa representação é especialmente adequada ao ACO, uma vez que o algoritmo trabalha naturalmente com transições entre posições e reforço de caminhos por meio de feromônio.

Alguns dos demais algoritmos utilizam uma representação contínua internamente, sendo posteriormente realizada uma conversão para movimentos discretos.

Essa diferença deve ser considerada durante a interpretação dos resultados, pois diferentes algoritmos possuem mecanismos internos distintos de representação e exploração do espaço de busca.

## Limitações

O projeto possui algumas limitações que devem ser consideradas na análise.

* O ambiente utilizado possui tamanho fixo.
* Os obstáculos são definidos previamente.
* O agente possui um número máximo de movimentos.
* O problema utiliza apenas quatro direções de movimento.
* Os algoritmos possuem mecanismos de busca diferentes.
* A representação contínua utilizada por alguns algoritmos é convertida posteriormente para movimentos discretos.
* Os resultados dependem da aleatoriedade presente nos algoritmos.
* Um único mapa não é suficiente para generalizar o comportamento dos algoritmos para todos os problemas de pathfinding.
* O tempo de execução pode variar de acordo com o hardware e o ambiente de execução.

Dessa forma, os resultados devem ser interpretados dentro do cenário experimental definido pelo projeto.

## Possíveis trabalhos futuros

Como evolução do projeto, podem ser implementadas novas funcionalidades, como:

* utilização de diferentes mapas;
* geração automática de obstáculos;
* diferentes tamanhos de grade;
* comparação com algoritmos clássicos como A* e Dijkstra;
* utilização de diferentes funções de fitness;
* visualização da evolução das populações;
* visualização das trilhas de feromônio do ACO;
* animação das gerações;
* execução de experimentos com diferentes parâmetros;
* análise de sensibilidade dos hiperparâmetros;
* inclusão de novas métricas de convergência;
* execução de experimentos em diferentes ambientes;
* comparação com outras técnicas de otimização.

## Conclusão

O projeto propõe a aplicação de algoritmos bioinspirados ao problema de pathfinding em um ambiente bidimensional com obstáculos.

A utilização de diferentes técnicas permite observar como estratégias inspiradas em comportamentos naturais podem ser utilizadas para explorar um espaço de busca e encontrar soluções para problemas de otimização.

O ACO é utilizado como principal abordagem devido à sua relação direta com problemas de caminhos e grafos, enquanto Cuckoo Search e GWO representam estratégias alternativas de exploração e aproveitamento do espaço de busca.

GA, PSO e Random Search são utilizados como referências adicionais para ampliar a comparação experimental.

A partir dos benchmarks, métricas, gráficos e testes estatísticos, o projeto busca fornecer uma análise experimental estruturada sobre o comportamento dessas diferentes técnicas no problema proposto.
