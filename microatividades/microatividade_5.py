"""
Microatividade 5: Exibir informações gerais sobre o conjunto de dados

Objetivo: Descrever como exibir informações gerais sobre as colunas, linhas e dados 
de um conjunto de dados usando a biblioteca Pandas (Python)

Autor: Victor Pessoa
Data: Novembro 2025
Disciplina: Tecnologias para desenvolvimento de soluções de big data
"""

# Importar a biblioteca pandas
import pandas as pd

def microatividade_5():
    """
    Função que implementa a Microatividade 5
    Exibe informações gerais sobre o conjunto de dados
    """
    print("=== MICROATIVIDADE 5 ===")
    print("Objetivo: Exibir informações gerais sobre colunas, linhas e dados")
    print()
    
    # Ler o conjunto de dados original
    try:
        dados = pd.read_csv('../dados/dados.csv', 
                           sep=';', 
                           engine='python', 
                           encoding='utf-8')
        
        print("✅ Dados carregados com sucesso!")
        print()
        
        # Imprimir informações gerais sobre o conjunto de dados
        print("📋 INFORMAÇÕES GERAIS DO CONJUNTO DE DADOS:")
        print("=" * 80)
        dados.info()
        print("=" * 80)
        print()
        
        # Extrair informações específicas solicitadas
        total_linhas = dados.shape[0]
        total_colunas = dados.shape[1]
        dados_nulos = dados.isnull().sum()
        tipos_dados = dados.dtypes
        memoria_utilizada = dados.memory_usage(deep=True).sum()
        
        print("📊 RESUMO DAS INFORMAÇÕES EXTRAÍDAS:")
        print(f"• Total de linhas: {total_linhas}")
        print(f"• Total de colunas: {total_colunas}")
        print()
        
        print("🔍 QUANTIDADE DE DADOS NULOS POR COLUNA:")
        for coluna, nulos in dados_nulos.items():
            if nulos > 0:
                print(f"• {coluna}: {nulos} valores nulos")
            else:
                print(f"• {coluna}: Sem valores nulos")
        print()
        
        print("🏷️  TIPO DE DADO DE CADA COLUNA:")
        for coluna, tipo in tipos_dados.items():
            print(f"• {coluna}: {tipo}")
        print()
        
        print(f"💾 QUANTIDADE DE MEMÓRIA UTILIZADA: {memoria_utilizada:,.2f} bytes")
        print(f"💾 QUANTIDADE DE MEMÓRIA UTILIZADA: {memoria_utilizada/1024:.2f} KB")
        print()
        
        # Informações adicionais sobre estatísticas descritivas
        print("📈 ESTATÍSTICAS DESCRITIVAS (colunas numéricas):")
        print("=" * 80)
        print(dados.describe())
        print("=" * 80)
        
        return dados, {
            'total_linhas': total_linhas,
            'total_colunas': total_colunas,
            'dados_nulos': dados_nulos,
            'tipos_dados': tipos_dados,
            'memoria_utilizada': memoria_utilizada
        }
        
    except FileNotFoundError:
        print("❌ Erro: Arquivo CSV não encontrado!")
        print("Verifique se o arquivo 'dados.csv' está na pasta '../dados/'")
        return None, None
    except Exception as e:
        print(f"❌ Erro ao processar os dados: {str(e)}")
        return None, None

if __name__ == "__main__":
    # Executar a microatividade
    dataset, informacoes = microatividade_5()