# Documentação do Projeto
## DGT2823 - Tecnologias para Desenvolvimento de Soluções de Big Data

### Informações Gerais
**Disciplina:** Tecnologias para desenvolvimento de soluções de big data  
**Tipo:** Trabalho Prático Individual  
**Autor:** Victor Pessoa  
**Data:** Novembro 2025  

---

## 📋 Sumário
1. [Contextualização](#contextualização)
2. [Objetivos](#objetivos)
3. [Estrutura do Projeto](#estrutura-do-projeto)
4. [Microatividades](#microatividades)
5. [Trabalho Prático](#trabalho-prático)
6. [Tecnologias Utilizadas](#tecnologias-utilizadas)
7. [Como Executar](#como-executar)
8. [Resultados Obtidos](#resultados-obtidos)
9. [Conclusões](#conclusões)

---

## 🎯 Contextualização

Como Analista de Dados, este projeto simula o recebimento de um conjunto de dados que precisa ser tratado para que possa ser utilizado em tarefas de mineração e análise de dados. O objetivo principal é demonstrar competências em Python com a biblioteca Pandas para leitura, manipulação e limpeza de dados.

---

## 🎯 Objetivos

### Objetivos das Microatividades:
- **Microatividade 1:** Ler um arquivo CSV usando a biblioteca Pandas
- **Microatividade 2:** Criar subconjuntos de dados a partir de um conjunto existente
- **Microatividade 3:** Configurar número máximo de linhas para visualização
- **Microatividade 4:** Exibir primeiras e últimas N linhas de um conjunto de dados
- **Microatividade 5:** Exibir informações gerais sobre colunas, linhas e dados

### Objetivo do Trabalho Prático:
- Realizar limpeza completa de um conjunto de dados, tornando-o apto para análise
- Tratar dados inconsistentes e valores nulos
- Converter tipos de dados adequadamente
- Documentar todo o processo de limpeza

---

## 📁 Estrutura do Projeto

```
DGT2823 Tecnologias para desenv/
├── dados/
│   └── dados.csv                    # Dataset original com dados inconsistentes
├── microatividades/
│   ├── microatividade_1.py          # Leitura de CSV
│   ├── microatividade_2.py          # Criação de subconjuntos
│   ├── microatividade_3.py          # Configuração de visualização
│   ├── microatividade_4.py          # Visualização de linhas
│   └── microatividade_5.py          # Informações gerais
├── trabalho_pratico/
│   ├── trabalho_pratico_principal.py # Script principal de limpeza
│   └── demonstracao_completa.ipynb   # Notebook demonstrativo
├── documentacao/
│   └── documentacao_projeto.md       # Este documento
└── README.md                         # Instruções de instalação e execução
```

---

## 🔬 Microatividades

### Microatividade 1: Leitura de Arquivo CSV
- **Arquivo:** `microatividades/microatividade_1.py`
- **Objetivo:** Demonstrar como carregar dados de um arquivo CSV
- **Conceitos abordados:**
  - Importação da biblioteca Pandas
  - Uso da função `pd.read_csv()`
  - Parâmetros: separador, engine, encoding
  - Tratamento de erros

### Microatividade 2: Criação de Subconjuntos
- **Arquivo:** `microatividades/microatividade_2.py`
- **Objetivo:** Demonstrar seleção de colunas específicas
- **Conceitos abordados:**
  - Seleção de colunas por nome
  - Criação de novos DataFrames
  - Verificação de dimensões

### Microatividade 3: Configuração de Visualização
- **Arquivo:** `microatividades/microatividade_3.py`
- **Objetivo:** Configurar opções de display do Pandas
- **Conceitos abordados:**
  - `pd.set_option()` e `pd.get_option()`
  - Configuração de `max_rows`
  - Método `to_string()`

### Microatividade 4: Visualização de Linhas
- **Arquivo:** `microatividades/microatividade_4.py`
- **Objetivo:** Utilizar métodos de visualização básica
- **Conceitos abordados:**
  - Método `head(n)` - primeiras N linhas
  - Método `tail(n)` - últimas N linhas
  - Inspeção visual dos dados

### Microatividade 5: Informações Gerais
- **Arquivo:** `microatividades/microatividade_5.py`
- **Objetivo:** Extrair informações estatísticas e estruturais
- **Conceitos abordados:**
  - Método `info()` - informações gerais
  - Propriedade `shape` - dimensões
  - Método `isnull().sum()` - valores nulos
  - Propriedade `dtypes` - tipos de dados
  - Método `memory_usage()` - uso de memória
  - Método `describe()` - estatísticas descritivas

---

## 🛠️ Trabalho Prático

### Arquivo Principal: `trabalho_pratico/trabalho_pratico_principal.py`

O trabalho prático implementa um processo completo de limpeza de dados seguindo estas etapas:

#### Etapa 1: Carregamento dos Dados
- Leitura do arquivo CSV com parâmetros adequados
- Verificação da integridade da importação

#### Etapa 2: Análise Inicial
- Inspeção das primeiras e últimas linhas
- Verificação de informações gerais (tipos, nulos, dimensões)

#### Etapa 3: Criação de Cópia
- Preservação dos dados originais
- Criação de cópia para tratamento

#### Etapa 4: Tratamento de Valores Nulos em 'Calories'
- Identificação de valores NaN
- Substituição por valor padrão (0)
- Verificação das alterações

#### Etapa 5: Tratamento de Valores Nulos em 'Date'
- Substituição inicial por valor temporário
- Correção de formatos inconsistentes

#### Etapa 6: Conversão de Tipos de Dados
- Tratamento de erros de formato
- Conversão para tipo datetime
- Correção de dados malformados ('20201226' → '2020/12/26')

#### Etapa 7: Limpeza Final
- Remoção de registros com valores nulos remanescentes
- Validação do dataset final

### Problemas Tratados:
1. **Valores NaN na coluna 'Calories'** (linhas 18, 28)
2. **Valores NaN na coluna 'Date'** (linha 22)
3. **Formato de data inconsistente** ('20201226' na linha 26)
4. **Aspas simples desnecessárias** nas datas

### Resultado Final:
- Dataset original: 32 registros
- Dataset final: 31 registros (1 registro removido por ter Date = NaN)
- Todos os dados inconsistentes foram tratados adequadamente

---

## 💻 Tecnologias Utilizadas

### Linguagem de Programação:
- **Python 3.8+**

### Bibliotecas Principais:
- **Pandas 1.0+:** Manipulação e análise de dados
- **NumPy 1.18+:** Operações numéricas (para tratamento de NaN)

### Ambiente de Desenvolvimento:
- **VS Code:** Editor de código
- **Jupyter Notebook:** Ambiente interativo (opcional)
- **JupyterLab:** Ambiente avançado (recomendado)

---

## ⚙️ Como Executar

### Pré-requisitos:
```bash
# Instalar Python 3.8 ou superior
# Instalar as dependências
pip install pandas numpy jupyter
```

### Execução das Microatividades:
```bash
# Navegar até a pasta do projeto
cd "C:\Users\User\Desktop\DGT2823 Tecnologias para desenv"

# Executar cada microatividade individualmente
python microatividades/microatividade_1.py
python microatividades/microatividade_2.py
python microatividades/microatividade_3.py
python microatividades/microatividade_4.py
python microatividades/microatividade_5.py
```

### Execução do Trabalho Prático:
```bash
# Script principal
python trabalho_pratico/trabalho_pratico_principal.py

# Notebook interativo (opcional)
jupyter notebook trabalho_pratico/demonstracao_completa.ipynb
```

---

## 📊 Resultados Obtidos

### Dataset Original:
- **Dimensões:** 32 linhas × 6 colunas
- **Colunas:** ID, Duration, Date, Pulse, Maxpulse, Calories
- **Problemas identificados:**
  - 2 valores NaN em 'Calories'
  - 1 valor NaN em 'Date'  
  - 1 formato de data inconsistente

### Dataset Final:
- **Dimensões:** 31 linhas × 6 colunas
- **Qualidade dos dados:** 100% limpos
- **Tipos de dados corretos:**
  - ID: int64
  - Duration: int64
  - Date: datetime64[ns]
  - Pulse: int64
  - Maxpulse: int64
  - Calories: float64

### Transformações Realizadas:
1. ✅ Substituição de 2 valores NaN em 'Calories' por 0
2. ✅ Correção de formato de data ('20201226' → '2020/12/26')
3. ✅ Conversão de coluna 'Date' para tipo datetime
4. ✅ Remoção de 1 registro com data inválida
5. ✅ Validação final de consistência

---

## 📝 Conclusões

### Competências Demonstradas:

1. **Manipulação de Dados com Pandas:**
   - Leitura eficiente de arquivos CSV
   - Configuração de parâmetros de importação
   - Seleção e filtragem de dados

2. **Limpeza e Tratamento de Dados:**
   - Identificação de dados inconsistentes
   - Estratégias de tratamento de valores nulos
   - Conversão de tipos de dados
   - Padronização de formatos

3. **Análise Exploratória:**
   - Inspeção visual dos dados
   - Extração de informações estatísticas
   - Validação de qualidade dos dados

4. **Boas Práticas de Programação:**
   - Código documentado e comentado
   - Tratamento adequado de erros
   - Estruturação lógica do processo
   - Preservação dos dados originais

### Aprendizados Principais:

- A importância da análise inicial para identificar problemas nos dados
- Diferentes estratégias para tratar valores nulos dependendo do contexto
- A necessidade de validação em cada etapa do processo de limpeza
- Como documentar adequadamente o processo de transformação dos dados

### Aplicabilidade:

Este projeto demonstra habilidades essenciais para um Analista de Dados, incluindo:
- Preparação de dados para análise
- Garantia de qualidade dos dados
- Documentação de processos
- Uso eficiente de ferramentas de análise

O dataset resultante está agora pronto para etapas subsequentes de análise, visualização e modelagem de dados.

---

**Nota:** Este projeto foi desenvolvido seguindo rigorosamente as especificações fornecidas no enunciado da disciplina DGT2823, demonstrando domínio das tecnologias necessárias para desenvolvimento de soluções de big data.