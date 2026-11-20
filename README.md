# Problema do Troco (Coin Change)

Projeto desenvolvido para a disciplina de **Projeto e Análise de Algoritmos**, do curso de Bacharelado em Sistemas de Informação do Instituto Federal de Minas Gerais (IFMG) – Campus Ouro Branco.

## Integrantes

- Felipe Alexandre Vieira Mendes
- Arthur Ribeiro

## 1. Descrição do Problema

O Problema do Troco (*Coin Change Problem*) consiste em determinar a combinação de moedas necessária para formar um determinado valor, utilizando a menor quantidade possível de moedas.

Neste projeto, serão implementadas e comparadas duas abordagens algorítmicas:

- **Algoritmo Guloso (Greedy):** escolhe, a cada etapa, a maior moeda possível sem ultrapassar o valor restante.
- **Programação Dinâmica (Dynamic Programming):** avalia diferentes combinações de moedas para encontrar a solução com a menor quantidade possível.

O objetivo é analisar o comportamento das duas estratégias, considerando a correção das soluções, o desempenho e a complexidade computacional.

## 2. Objetivos

- Implementar o algoritmo guloso e o algoritmo de programação dinâmica.
- Comparar os resultados produzidos pelas duas abordagens.
- Verificar a quantidade de moedas utilizada em diferentes valores de entrada.
- Analisar a complexidade de tempo e espaço dos algoritmos.
- Realizar experimentos com entradas de diferentes tamanhos.
- Medir os tempos de execução e coletar métricas de desempenho.
- Construir gráficos e tabelas para apresentar os resultados obtidos.

## 3. Estrutura do Projeto

```text
Problema-do-Troco/
│
├── src/
│   ├── __init__.py
│   ├── guloso.py
│   └── programacao_dinamica.py
│
├── tests/
│   ├── __init__.py
│   └── test_algoritmos.py
│
├── experimentos/
│
├── resultados/
│   ├── graficos/
│   └── tabelas/
│
├── apresentacao/
│
├── main.py
├── README.md
└── .gitignore
```

*Observação: a estrutura será atualizada conforme a integração das implementações e a organização dos experimentos.*

## 4. Abordagens Algorítmicas

### 4.1. Algoritmo Guloso

O algoritmo guloso utiliza uma estratégia de escolha local. Em cada etapa, seleciona a maior denominação de moeda que não ultrapasse o valor restante.

A implementação considera as moedas em ordem decrescente e utiliza a operação `divmod()` para calcular a quantidade de moedas de cada denominação.

**Conjunto de moedas utilizado:**

```python
[100, 50, 25, 10, 5, 1]
```

Os valores são representados em centavos para evitar problemas de precisão com números decimais.

A implementação também realiza validações para impedir valores negativos, denominações inválidas e conjuntos de moedas fora da ordem esperada.

**Complexidade:**

- Tempo: O(N), considerando N denominações de moedas previamente ordenadas.
- Espaço auxiliar: O(1), desconsiderando a estrutura utilizada para armazenar a resposta.

### 4.2. Programação Dinâmica

A programação dinâmica será utilizada para encontrar a quantidade mínima de moedas necessária para formar determinado valor.

A estratégia consiste em decompor o problema em subproblemas menores, armazenando os resultados já calculados para evitar operações repetidas.

**Complexidade esperada:**

- Tempo: O(V × N).
- Espaço: O(V).

Onde:
- V representa o valor do troco em centavos.
- N representa a quantidade de denominações de moedas.

*A implementação e a validação dessa abordagem serão integradas ao projeto após sua conclusão.*

## 5. Testes e Validação

A implementação do algoritmo guloso possui testes automatizados utilizando a biblioteca `unittest` do Python.

Os testes realizados verificam:

- Formação de um troco de 185 centavos.
- Quantidade de moedas utilizadas.
- Formação de valores específicos.
- Comportamento para valor igual a zero.
- Tratamento de valores negativos.
- Validação da ordem das denominações.
- Comportamento em um conjunto de moedas no qual a estratégia gulosa não encontra a solução ótima.

**Resultado atual:** 8 testes automatizados executados com sucesso.

Para executar os testes, utilize:

```bash
python -m unittest discover -s tests -v
```

## 6. Exemplo de Execução

A implementação atual do algoritmo guloso pode ser executada com:

```bash
python main.py
```

Exemplo para o valor de 185 centavos:

```text
PROBLEMA DO TROCO - ALGORITMO GULOSO
------------------------------------
Valor solicitado: R$ 1.85

Moedas utilizadas:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
1 moeda(s) de R$ 0.25
1 moeda(s) de R$ 0.10

Quantidade total de moedas: 4
```

## 7. Comparação entre as Abordagens

Um dos objetivos centrais do projeto é comparar o comportamento do algoritmo guloso com o da programação dinâmica.

Além dos testes utilizando as moedas brasileiras, será utilizado um conjunto de moedas não canônico para demonstrar uma situação em que a estratégia gulosa não encontra a solução ótima.

**Exemplo:**

- Moedas disponíveis: `[4, 3, 1]`
- Valor desejado: `6`

| Abordagem | Combinação | Quantidade |
|---|---|---:|
| Guloso | 4 + 1 + 1 | 3 moedas |
| Programação Dinâmica | 3 + 3 | 2 moedas |

Esse exemplo demonstra que o algoritmo guloso não garante a solução ótima para qualquer conjunto de denominações.

## 8. Experimentos e Análise de Desempenho

Após a integração das duas implementações, serão realizados experimentos com diferentes valores de entrada.

Serão coletadas informações como:

- Valor do troco utilizado.
- Quantidade de moedas disponíveis.
- Quantidade mínima de moedas encontrada.
- Tempo de execução de cada algoritmo.
- Comparação dos resultados obtidos.

Os dados serão organizados em tabelas e gráficos, permitindo analisar o crescimento do custo computacional conforme o tamanho da entrada aumenta.

Os resultados experimentais serão apresentados nesta seção após a execução dos testes comparativos.

## 9. Tecnologias Utilizadas

- Python 3.
- Biblioteca `unittest` para testes automatizados.
- Git e GitHub para controle de versão e colaboração.
- Bibliotecas de visualização de dados a serem definidas na etapa de experimentação.

## 10. Considerações Finais

O projeto busca compreender, na prática, as diferenças entre duas estratégias clássicas de resolução de problemas: algoritmo guloso e programação dinâmica.

A comparação permitirá observar não apenas o desempenho das implementações, mas também as condições em que cada abordagem consegue produzir uma solução ótima.

Ao final, serão apresentados os resultados experimentais, os gráficos comparativos e a análise das complexidades dos algoritmos.

---

**Instituição:** Instituto Federal de Minas Gerais – IFMG  
**Campus:** Ouro Branco  
**Curso:** Bacharelado em Sistemas de Informação  
**Disciplina:** Projeto e Análise de Algoritmos
