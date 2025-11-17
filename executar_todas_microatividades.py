"""
Script Executor de Todas as Microatividades
DGT2823 - Tecnologias para desenvolvimento de soluções de big data

Este script executa todas as microatividades em sequência para demonstração completa.

Autor: Victor Pessoa
Data: Novembro 2025
"""

import os
import sys

def executar_microatividade(numero, descricao):
    """
    Executa uma microatividade específica
    """
    print("=" * 80)
    print(f"🎯 EXECUTANDO MICROATIVIDADE {numero}")
    print(f"📋 {descricao}")
    print("=" * 80)
    
    try:
        # Importar e executar a microatividade
        if numero == 1:
            from microatividades.microatividade_1 import microatividade_1
            resultado = microatividade_1()
        elif numero == 2:
            from microatividades.microatividade_2 import microatividade_2
            resultado = microatividade_2()
        elif numero == 3:
            from microatividades.microatividade_3 import microatividade_3
            resultado = microatividade_3()
        elif numero == 4:
            from microatividades.microatividade_4 import microatividade_4
            resultado = microatividade_4()
        elif numero == 5:
            from microatividades.microatividade_5 import microatividade_5
            resultado = microatividade_5()
        
        print(f"\n✅ Microatividade {numero} executada com sucesso!")
        return resultado
        
    except ImportError as e:
        print(f"❌ Erro de importação: {str(e)}")
        print("Verifique se os arquivos das microatividades existem.")
        return None
    except Exception as e:
        print(f"❌ Erro na execução: {str(e)}")
        return None
    finally:
        print("\n" + "=" * 80)
        input("Pressione ENTER para continuar...")
        print("\n")

def main():
    """
    Função principal que executa todas as microatividades
    """
    print("🎓 EXECUÇÃO COMPLETA DAS MICROATIVIDADES")
    print("📚 DGT2823 - Tecnologias para desenvolvimento de soluções de big data")
    print()
    
    # Lista das microatividades
    microatividades = [
        (1, "Leitura de arquivo CSV usando Pandas"),
        (2, "Criação de subconjunto de dados"),
        (3, "Configuração do número máximo de linhas"),
        (4, "Exibição das primeiras e últimas N linhas"),
        (5, "Informações gerais sobre o conjunto de dados")
    ]
    
    resultados = {}
    
    # Executar cada microatividade
    for numero, descricao in microatividades:
        resultado = executar_microatividade(numero, descricao)
        resultados[numero] = resultado
    
    # Resumo final
    print("🎉 EXECUÇÃO COMPLETA!")
    print("=" * 80)
    print("📊 RESUMO DOS RESULTADOS:")
    print()
    
    for numero, descricao in microatividades:
        status = "✅ Sucesso" if resultados[numero] is not None else "❌ Falhou"
        print(f"Microatividade {numero}: {status}")
    
    print("\n" + "=" * 80)
    print("🔗 PRÓXIMOS PASSOS:")
    print("1. Execute o trabalho prático principal:")
    print("   python trabalho_pratico/trabalho_pratico_principal.py")
    print()
    print("2. Ou abra o notebook demonstrativo:")
    print("   jupyter notebook trabalho_pratico/demonstracao_completa.ipynb")
    print("=" * 80)

if __name__ == "__main__":
    main()