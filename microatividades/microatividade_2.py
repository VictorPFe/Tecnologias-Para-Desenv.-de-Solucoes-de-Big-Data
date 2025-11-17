"""
Microatividade 2: Criar um subconjunto de dados usando Pandas

Objetivo: Descrever como criar um subconjunto de dados a partir de um conjunto 
existente usando a biblioteca Pandas (Python)

Autor: Victor Pessoa
Data: Novembro 2025
Disciplina: Tecnologias para desenvolvimento de soluções de big data
"""

# Importar a biblioteca pandas
import pandas as pd

def microatividade_2():
    """
    Função que implementa a Microatividade 2
    Cria um subconjunto de dados a partir do conjunto original
    """
    print("=== MICROATIVIDADE 2 ===")
    print("Objetivo: Criar um subconjunto de dados a partir de um conjunto existente")
    print()
    
    # Ler o conjunto de dados original (mesmo processo da Microatividade 1)
    try:
        dados_originais = pd.read_csv('../dados/dados.csv', 
                                    sep=';', 
                                    engine='python', 
                                    encoding='utf-8')
        
        print("✅ Dados originais carregados com sucesso!")
        print(f"📊 Dataset original: {dados_originais.shape[0]} linhas e {dados_originais.shape[1]} colunas")
        print(f"🏷️  Colunas disponíveis: {list(dados_originais.columns)}")
        print()
        
        # Criar uma nova variável para o subconjunto
        # Selecionando 3 colunas conforme recomendação: ID, Duration e Pulse
        subconjunto_dados = dados_originais[['ID', 'Duration', 'Pulse']]
        
        print("📋 Subconjunto criado com as colunas: ID, Duration, Pulse")
        print(f"📊 Subconjunto: {subconjunto_dados.shape[0]} linhas e {subconjunto_dados.shape[1]} colunas")
        print()
        
        # Exibir os dados da nova variável (subconjunto)
        print("📋 Conteúdo do subconjunto de dados:")
        print(subconjunto_dados)
        
        return dados_originais, subconjunto_dados
        
    except FileNotFoundError:
        print("❌ Erro: Arquivo CSV não encontrado!")
        print("Verifique se o arquivo 'dados.csv' está na pasta '../dados/'")
        return None, None
    except Exception as e:
        print(f"❌ Erro ao processar os dados: {str(e)}")
        return None, None

if __name__ == "__main__":
    # Executar a microatividade
    dados_orig, subconjunto = microatividade_2()