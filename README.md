# Problema do Troco (Coin Change)

Projeto desenvolvido para a disciplina de **Projeto e Análise de Algoritmos**, do curso de Bacharelado em Sistemas de Informação do Instituto Federal de Minas Gerais (IFMG) – Campus Ouro Branco.

O objetivo é implementar e comparar duas abordagens de resolução do Problema do Troco: **Algoritmo Guloso (Greedy)** e **Programação Dinâmica (PD)**, analisando suas estratégias, complexidades e desempenhos.

## Integrantes

- **Felipe Alexandre Vieira Mendes**
- **Arthur Ribeiro**

## Sobre o Projeto

O Problema do Troco consiste em determinar a menor quantidade de moedas necessária para representar um determinado valor, considerando um conjunto de denominações disponíveis.

Por exemplo, considerando as moedas de R$ 1,00, R$ 0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01, o objetivo é encontrar a combinação que represente o valor solicitado utilizando a menor quantidade possível de moedas.

O projeto utiliza esse problema clássico para estudar e comparar duas estratégias fundamentais de desenvolvimento de algoritmos.

## Abordagens Implementadas

### 1. Algoritmo Guloso (Greedy)

O algoritmo guloso escolhe, a cada etapa, a maior moeda possível que não ultrapasse o valor restante do troco.

Essa estratégia busca construir uma solução por meio de escolhas locais, sem reconsiderar as decisões anteriores.

### 2. Programação Dinâmica (PD)

A programação dinâmica resolve o problema dividindo-o em subproblemas menores.

A solução é construída gradualmente, armazenando os resultados já calculados para evitar a repetição de operações. Dessa forma, encontra-se a quantidade mínima de moedas necessária para cada valor até alcançar o troco desejado.

## Objetivos

- Implementar o Problema do Troco utilizando Algoritmo Guloso e Programação Dinâmica.
- Compreender as diferenças entre as estratégias utilizadas.
- Comparar os resultados obtidos pelas duas implementações.
- Analisar a complexidade de tempo e espaço dos algoritmos.
- Realizar experimentos com diferentes valores de entrada.
- Medir o tempo de execução e outras métricas relevantes.
- Gerar gráficos para representar e comparar o desempenho das implementações.

## Análise de Complexidade

Considerando:

- **V:** valor do troco, representado em centavos.
- **N:** quantidade de denominações de moedas disponíveis.

| Algoritmo | Complexidade de tempo | Complexidade de espaço |
|---|---|---|
| Guloso | O(N), com moedas previamente ordenadas | O(1) |
| Programação Dinâmica | O(V × N) | O(V) |

As complexidades consideram uma implementação gulosa que percorre as denominações uma única vez, utilizando divisão e resto para determinar a quantidade de cada moeda.

## Experimentos e Comparações

Serão realizados testes com diferentes valores de entrada para avaliar o comportamento dos algoritmos.

As análises considerarão:

- Quantidade de moedas utilizadas.
- Tempo de execução.
- Crescimento do tempo conforme o aumento da entrada.
- Complexidade teórica e desempenho experimental.
- Comparação entre os resultados das duas abordagens.

Os resultados serão apresentados por meio de tabelas e gráficos, permitindo visualizar as diferenças de desempenho.

## Conjunto de Moedas

Para os experimentos principais, será utilizado o sistema monetário brasileiro, considerando as seguintes denominações em centavos:

`100, 50, 25, 10, 5, 1`

Esse conjunto permite comparar as duas abordagens obtendo uma solução ótima para os valores inteiros de troco considerados.

Também é importante observar que o algoritmo guloso não garante uma solução ótima para qualquer conjunto arbitrário de moedas.

## Tecnologias Utilizadas

As tecnologias e ferramentas utilizadas no desenvolvimento, execução dos experimentos e geração dos gráficos serão documentadas conforme a implementação do projeto.

## Disciplina

**Projeto e Análise de Algoritmos**

Bacharelado em Sistemas de Informação  
Instituto Federal de Minas Gerais (IFMG)  
Campus Ouro Branco

---

*Projeto acadêmico desenvolvido como atividade prática da disciplina de Projeto e Análise de Algoritmos.*
