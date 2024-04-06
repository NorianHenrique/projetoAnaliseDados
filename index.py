import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Função para ler arquivo dependendo da extensão
def ler_arquivo(arquivo):
    if arquivo.endswith('.csv'):
        return pd.read_csv(arquivo)
    elif arquivo.endswith(('.xls', '.xlsx')):
        return pd.read_excel(arquivo)
    else:
        raise ValueError("Formato de arquivo não suportado.")
    
    
# Função para realizar análise estatística e gerar gráficos
def analisar_dados(df):
     # Gerando estatísticas descritivas
     print(df.describe())
     
     # Gerando uma matriz de correlação
     correlacao = df.corr()
     print(correlacao)
     
     # Visualização de gráficos
     sns.pairplot(df)
     plt.show()
     
     # Mapa de calor da correlação entre variáveis
     sns.heatmap(correlacao,annot=True,fmt='.2f',cmap='coolwarm')
     plt.show()
     
#Execução principal
def main():
    # Pede ao usuário o caminho até o arquivo
    arquivo = input("Insira o caminho completo do arquivo CSV/Excel para análise: ")
    if not os.path.isfile(arquivo):
        print("Arquivo não encontrado. Por favor, verifique o caminho e tente novamente.")
        return
    
    try:
        df = ler_arquivo(arquivo)
        analisar_dados(df)
    except ValueError as e:
        print(e)
    except Exception as e:
        print("Ocorreu um erro ao ler o arquivo ou analisar os dados.")
        print(e)

if __name__ == '__main__':
    main()