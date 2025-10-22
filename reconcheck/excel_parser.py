import pandas as pd

def carregar_excel(caminho):
    dados_apolice_vida = pd.read_excel(caminho, na_values=['N/A', 'sem dados', '-'])
    return dados_apolice_vida

def exibir_dados_sem_vazios(dados_apolice_vida):
    apolice_sem_dados_vazios = dados_apolice_vida.dropna()
    return apolice_sem_dados_vazios

def conversao_tipos_dados(dados_apolice_vida, colunas_numericas, colunas_de_data):
    for coluna in colunas_numericas:
        dados_apolice_vida[coluna] = pd.to_numeric(dados_apolice_vida[coluna].str.replace("R\$", "").str.replace(",", "."), errors='coerce')
        #error coerce transforma valores inválidos em NaN

    for coluna in colunas_de_data:
        dados_apolice_vida[coluna] = pd.to_datetime(dados_apolice_vida[coluna], format="%d/%m/%Y", errors='coerce')
        #o format especifica o formato da data presente no arquivo excel, insira o mesmo formato dos dados no arquivo excel.

#skiprows=3 para pular as 3 primeiras linhas do arquivo excel.

def padronizacao_colunas(dados_apolice_vida):
    for coluna in dados_apolice_vida.columns:
        if "_" in coluna:
            nova_coluna = coluna.replace("_", " ")
            dados_apolice_vida.rename(columns={coluna: nova_coluna}, inplace=True)
            # a tabela é tratada como dicionário para fazer a mudança de coluna como se fosse um dicionário


def exibindo_colunas(dados_apolice_sem_vazios):
    return f"\n--- COLUNAS ---\n{dados_apolice_sem_vazios.columns}"

def exibindo_tipos_dados(dados_apolice_sem_vazios):
    return f"\n--- TIPOS DE DADOS ---\n{dados_apolice_sem_vazios.dtypes}"

def exibindo_primeiras_linhas(dados_apolice_sem_vazios, numero_de_linhas_a_exibir):
    return f"\n--- PRIMEIRAS LINHAS ---\n{dados_apolice_sem_vazios.head(numero_de_linhas_a_exibir)}"

# O parâmetro sheet_name do pd.read_excel() serve para especificar qual aba (ou abas) do arquivo Excel você quer ler. Isso é útil 
# quando o Excel tem várias planilhas e você só quer trabalhar com uma delas — ou com todas.
# ele iria no mesmo local do na_values



