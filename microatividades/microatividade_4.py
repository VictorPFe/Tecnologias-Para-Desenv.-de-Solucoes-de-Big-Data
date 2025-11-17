"""
Microatividade 4: Exibir primeiras e últimas N linhas

Objetivo: Descrever como exibir as primeiras e últimas "N" linhas de um conjunto 
de dados usando a biblioteca Pandas (Python)

Autor: Victor Pessoa
Data: Novembro 2025
Disciplina: Tecnologias para desenvolvimento de soluções de big data
"""

# Importar a biblioteca pandas
import pandas as pd

def microatividade_4():
    """
    Função que implementa a Microatividade 4
    Exibe as primeiras e últimas N linhas do conjunto de dados
    """
    print("=== MICROATIVIDADE 4 ===")
    print("Objetivo: Exibir as primeiras e últimas N linhas do conjunto de dados")
    print()
    
    # Ler o conjunto de dados original
    try:
        dados = pd.read_csv('../dados/dados.csv', 
                           sep=';', 
                           engine='python', 
                           encoding='utf-8')
        
        print("✅ Dados carregados com sucesso!")
        print(f"📊 Total de registros no dataset: {len(dados)}")
        print()
        
        # Imprimir as primeiras 10 linhas
        print("📋 PRIMEIRAS 10 LINHAS do conjunto de dados:")
        print("=" * 80)
        primeiras_10 = dados.head(10)
        print(primeiras_10)
        print("=" * 80)
        print()
        
        # Imprimir as últimas 10 linhas
        print("📋 ÚLTIMAS 10 LINHAS do conjunto de dados:")
        print("=" * 80)
        ultimas_10 = dados.tail(10)
        print(ultimas_10)
        print("=" * 80)
        print()
        
        # Informações adicionais sobre os métodos utilizados
        print("ℹ️  INFORMAÇÕES SOBRE OS MÉTODOS:")
        print("• head(n): Retorna as primeiras n linhas do DataFrame")
        print("• tail(n): Retorna as últimas n linhas do DataFrame")
        print("• Se n não for especificado, o padrão é 5 linhas")
        
        return dados, primeiras_10, ultimas_10
        
    except FileNotFoundError:
        print("❌ Erro: Arquivo CSV não encontrado!")
        print("Verifique se o arquivo 'dados.csv' está na pasta '../dados/'")
        return None, None, None
    except Exception as e:
        print(f"❌ Erro ao processar os dados: {str(e)}")
        return None, None, None

if __name__ == "__main__":
    # Executar a microatividade
    dataset, primeiras, ultimas = microatividade_4()