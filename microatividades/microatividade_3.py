"""
Microatividade 3: Configurar número máximo de linhas para visualização

Objetivo: Descrever como configurar o número máximo de linhas a serem exibidas 
na visualização de um conjunto de dados usando a biblioteca Pandas (Python)

Autor: Victor Pessoa
Data: Novembro 2025
Disciplina: Tecnologias para desenvolvimento de soluções de big data
"""

# Importar a biblioteca pandas
import pandas as pd

def microatividade_3():
    """
    Função que implementa a Microatividade 3
    Configura o número máximo de linhas para visualização
    """
    print("=== MICROATIVIDADE 3 ===")
    print("Objetivo: Configurar número máximo de linhas para visualização")
    print()
    
    # Ler o conjunto de dados original
    try:
        dados = pd.read_csv('../dados/dados.csv', 
                           sep=';', 
                           engine='python', 
                           encoding='utf-8')
        
        print("✅ Dados carregados com sucesso!")
        print()
        
        # Verificar configuração atual do max_rows
        configuracao_atual = pd.get_option('display.max_rows')
        print(f"📋 Configuração atual de max_rows: {configuracao_atual}")
        
        # Definir novo valor para a propriedade "max_rows"
        pd.set_option('display.max_rows', 9999)
        
        print("⚙️  Configuração alterada: max_rows = 9999")
        
        # Verificar se a configuração foi aplicada
        nova_configuracao = pd.get_option('display.max_rows')
        print(f"✅ Nova configuração de max_rows: {nova_configuracao}")
        print()
        
        # Imprimir o conjunto de dados usando o método to_string()
        print("📋 Dataset completo usando to_string():")
        print("=" * 80)
        print(dados.to_string())
        print("=" * 80)
        
        return dados
        
    except FileNotFoundError:
        print("❌ Erro: Arquivo CSV não encontrado!")
        print("Verifique se o arquivo 'dados.csv' está na pasta '../dados/'")
        return None
    except Exception as e:
        print(f"❌ Erro ao processar os dados: {str(e)}")
        return None

if __name__ == "__main__":
    # Executar a microatividade
    dataset = microatividade_3()