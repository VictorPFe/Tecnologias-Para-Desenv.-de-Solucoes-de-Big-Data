"""
Microatividade 1: Ler um arquivo CSV usando a biblioteca Pandas

Objetivo: Descrever como ler um arquivo CSV usando a biblioteca Pandas (Python)

Autor: Victor Pessoa
Data: Novembro 2025
Disciplina: Tecnologias para desenvolvimento de soluções de big data
"""

# Importar a biblioteca pandas
import pandas as pd

def microatividade_1():
    """
    Função que implementa a Microatividade 1
    Lê um arquivo CSV e exibe seu conteúdo
    """
    print("=== MICROATIVIDADE 1 ===")
    print("Objetivo: Ler um arquivo CSV usando a biblioteca Pandas")
    print()
    
    # Criar uma variável para armazenar os dados
    dados = None
    
    try:
        # Ler o conteúdo do arquivo CSV
        # Parâmetros utilizados:
        # - sep=';' : Define o separador de colunas como ponto e vírgula
        # - engine='python' : Especifica o engine de parsing
        # - encoding='utf-8' : Define a codificação dos caracteres
        dados = pd.read_csv('../dados/dados.csv', 
                           sep=';', 
                           engine='python', 
                           encoding='utf-8')
        
        print("✅ Arquivo CSV carregado com sucesso!")
        print(f"📊 Dimensões do dataset: {dados.shape[0]} linhas e {dados.shape[1]} colunas")
        print()
        
        # Exibir os dados da variável
        print("📋 Conteúdo do arquivo CSV:")
        print(dados)
        
    except FileNotFoundError:
        print("❌ Erro: Arquivo CSV não encontrado!")
        print("Verifique se o arquivo 'dados.csv' está na pasta '../dados/'")
    except Exception as e:
        print(f"❌ Erro ao ler o arquivo: {str(e)}")
    
    return dados

if __name__ == "__main__":
    # Executar a microatividade
    dataset = microatividade_1()