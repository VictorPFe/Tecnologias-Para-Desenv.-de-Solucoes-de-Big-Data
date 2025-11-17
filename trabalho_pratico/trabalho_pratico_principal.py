"""
TRABALHO PRÁTICO: Limpeza e Tratamento de Dados com Pandas

Disciplina: DGT2823 - Tecnologias para desenvolvimento de soluções de big data
Objetivo: Realizar a limpeza de um conjunto de dados para torná-lo apto 
          para tarefas de mineração/análise de dados

Autor: Victor Pessoa
Data: Novembro 2025

Contextualização:
Como Analista de Dados, você recebeu um conjunto de dados que precisa ser
tratado para que possa ser utilizado para descoberta de conhecimento através
de análise e interpretação posterior.
"""

import pandas as pd
import numpy as np

def trabalho_pratico():
    """
    Função principal que implementa todo o processo de limpeza e tratamento dos dados
    conforme especificado no roteiro de prática
    """
    print("=" * 80)
    print("TRABALHO PRÁTICO: LIMPEZA E TRATAMENTO DE DADOS")
    print("=" * 80)
    print()
    
    # PASSO 1: Ler o conteúdo do CSV
    print("📖 PASSO 1: Lendo o arquivo CSV...")
    try:
        dados_originais = pd.read_csv('../dados/dados.csv', 
                                    sep=';', 
                                    engine='python', 
                                    encoding='utf-8')
        print("✅ Arquivo CSV carregado com sucesso!")
        print(f"📊 Dimensões: {dados_originais.shape[0]} linhas x {dados_originais.shape[1]} colunas")
        print()
    except Exception as e:
        print(f"❌ Erro ao carregar o arquivo: {str(e)}")
        return None
    
    # PASSO 2: Verificar se os dados foram importados adequadamente
    print("🔍 PASSO 2: Verificando a importação dos dados...")
    print("\n📋 Informações gerais sobre o conjunto de dados:")
    print("-" * 50)
    dados_originais.info()
    print("-" * 50)
    
    print(f"\n📈 Primeiras 5 linhas:")
    print(dados_originais.head())
    
    print(f"\n📉 Últimas 5 linhas:")
    print(dados_originais.tail())
    print()
    
    # PASSO 3: Criar uma cópia do conjunto de dados original
    print("📝 PASSO 3: Criando uma cópia dos dados originais...")
    dados_tratados = dados_originais.copy()
    print("✅ Cópia criada com sucesso!")
    print()
    
    # PASSO 4: Substituir valores nulos da coluna 'Calories' por 0
    print("🔧 PASSO 4: Tratando valores nulos na coluna 'Calories'...")
    print(f"Valores nulos antes do tratamento: {dados_tratados['Calories'].isnull().sum()}")
    
    dados_tratados['Calories'] = dados_tratados['Calories'].fillna(0)
    
    print(f"Valores nulos após o tratamento: {dados_tratados['Calories'].isnull().sum()}")
    print("✅ Valores nulos em 'Calories' substituídos por 0")
    print("\n📋 Verificação das mudanças:")
    print(dados_tratados[dados_tratados['Calories'] == 0])
    print()
    
    # PASSO 5: Substituir valores nulos da coluna 'Date' por '1900/01/01'
    print("🔧 PASSO 5: Tratando valores nulos na coluna 'Date'...")
    print(f"Valores nulos antes do tratamento: {dados_tratados['Date'].isnull().sum()}")
    
    dados_tratados['Date'] = dados_tratados['Date'].fillna('1900/01/01')
    
    print(f"Valores nulos após o tratamento: {dados_tratados['Date'].isnull().sum()}")
    print("✅ Valores nulos em 'Date' substituídos por '1900/01/01'")
    print("\n📋 Verificação das mudanças:")
    print(dados_tratados[dados_tratados['Date'] == '1900/01/01'])
    print()
    
    # PASSO 6: Tentar transformar coluna 'Date' em datetime (primeiro erro esperado)
    print("🔧 PASSO 6: Primeira tentativa de conversão para datetime...")
    try:
        dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'], format='%Y/%m/%d')
        print("✅ Conversão realizada com sucesso!")
    except Exception as e:
        print(f"⚠️  Erro esperado encontrado: {str(e)}")
        print("Motivo: O valor '1900/01/01' não está no formato correto")
        print()
    
    # PASSO 7: Substituir '1900/01/01' por NaN
    print("🔧 PASSO 7: Corrigindo o valor '1900/01/01' para NaN...")
    dados_tratados['Date'] = dados_tratados['Date'].replace('1900/01/01', np.nan)
    print("✅ Valor '1900/01/01' substituído por NaN")
    
    # PASSO 8: Tentar novamente a conversão para datetime (segundo erro esperado)
    print("\n🔧 PASSO 8: Segunda tentativa de conversão para datetime...")
    try:
        dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'], format='%Y/%m/%d')
        print("✅ Conversão realizada com sucesso!")
    except Exception as e:
        print(f"⚠️  Segundo erro esperado encontrado: {str(e)}")
        print("Motivo: O valor '20201226' não está no formato '%Y/%m/%d'")
        print()
    
    # PASSO 9: Corrigir o valor problemático '20201226'
    print("🔧 PASSO 9: Corrigindo o valor '20201226'...")
    
    # Localizar e corrigir o valor problemático
    mask = dados_tratados['Date'] == '20201226'
    if mask.any():
        print("Valor problemático encontrado na linha:", dados_tratados[mask].index.tolist())
        # Converter '20201226' para '2020/12/26'
        dados_tratados.loc[mask, 'Date'] = '2020/12/26'
        print("✅ Valor '20201226' corrigido para '2020/12/26'")
    
    # PASSO 10: Conversão final para datetime
    print("\n🔧 PASSO 10: Conversão final para datetime...")
    try:
        dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'], format='%Y/%m/%d', errors='coerce')
        print("✅ Conversão para datetime realizada com sucesso!")
        print(f"Tipo de dados da coluna 'Date': {dados_tratados['Date'].dtype}")
    except Exception as e:
        print(f"❌ Erro na conversão final: {str(e)}")
    
    print("\n📋 Verificação das datas após conversão:")
    print(dados_tratados['Date'].head(10))
    print()
    
    # PASSO 11: Remover registros com valores nulos
    print("🔧 PASSO 11: Removendo registros com valores nulos...")
    print(f"Registros antes da remoção: {len(dados_tratados)}")
    print(f"Registros com Date nulo: {dados_tratados['Date'].isnull().sum()}")
    
    # Identificar linhas com valores nulos em Date
    linhas_nulas = dados_tratados[dados_tratados['Date'].isnull()]
    if not linhas_nulas.empty:
        print(f"Linhas que serão removidas (índices): {linhas_nulas.index.tolist()}")
        print("Dados das linhas que serão removidas:")
        print(linhas_nulas)
    
    # Remover linhas com valores nulos
    dados_limpos = dados_tratados.dropna(subset=['Date'])
    
    print(f"\nRegistros após a remoção: {len(dados_limpos)}")
    print(f"Registros removidos: {len(dados_tratados) - len(dados_limpos)}")
    print("✅ Registros com valores nulos removidos com sucesso!")
    print()
    
    # PASSO 12: Verificação final
    print("🎯 PASSO 12: Verificação final do dataset limpo...")
    print("=" * 60)
    print(f"📊 Dimensões finais: {dados_limpos.shape[0]} linhas x {dados_limpos.shape[1]} colunas")
    print("\n📋 Informações finais do dataset:")
    dados_limpos.info()
    print("\n📈 Dataset final:")
    print(dados_limpos)
    print("=" * 60)
    
    # Resumo das transformações realizadas
    print("\n📝 RESUMO DAS TRANSFORMAÇÕES REALIZADAS:")
    print("=" * 60)
    print("1. ✅ Carregamento do arquivo CSV com separador ';'")
    print("2. ✅ Criação de cópia dos dados originais")
    print("3. ✅ Substituição de valores nulos em 'Calories' por 0")
    print("4. ✅ Tratamento de valores nulos em 'Date'")
    print("5. ✅ Correção do formato de data '20201226' para '2020/12/26'")
    print("6. ✅ Conversão da coluna 'Date' para tipo datetime")
    print("7. ✅ Remoção de registros com valores nulos em 'Date'")
    print(f"8. ✅ Dataset final: {len(dados_limpos)} registros válidos")
    print("=" * 60)
    
    return dados_originais, dados_limpos

if __name__ == "__main__":
    # Executar o trabalho prático
    dados_orig, dados_final = trabalho_pratico()