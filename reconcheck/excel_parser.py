import pandas as pd

dados_apolice_vida = pd.read_excel("/home/natha/Área de trabalho/ReconChek/data/apolice_vida_reestruturada.xlsx", na_values=['N/A', 'sem dados', '-'])

colunas_numericas = ["Prêmio Anual", "Garantia_Valor"]
colunas_de_data = ["Início da Vigência", "Fim da Vigência", "Próximo Vencimento"]
for coluna in colunas_numericas:
    dados_apolice_vida[coluna] = pd.to_numeric(dados_apolice_vida[coluna].str.replace("R\$", "").str.replace(",", "."), errors='coerce')
    #error coerce transforma valores inválidos em NaN

for coluna in colunas_de_data:
    dados_apolice_vida[coluna] = pd.to_datetime(dados_apolice_vida[coluna], format="%d/%m/%Y", errors='coerce')
    #o format especifica o formato da data presente no arquivo excel, insira o mesmo formato dos dados no arquivo excel.

#skiprows=3 para pular as 3 primeiras linhas do arquivo excel.

def padronizacao_colunas(colunas):
    if isinstance(colunas, list):
        for coluna in colunas:
            if "_" in coluna:
                nova_coluna = coluna.replace("_", " ")
                dados_apolice_vida.rename(columns={coluna: nova_coluna}, inplace=True)
                # a tabela é tratada como dicionário para fazer a mudança de coluna como se fosse um dicionário
    else:
        if "_" in colunas:
            nova_coluna = colunas.replace("_", " ")
            dados_apolice_vida.rename(columns={colunas: nova_coluna}, inplace=True)


dados_apolice_sem_vazios = dados_apolice_vida.dropna() # Remover linhas com valores ausentes
print("\n--- COLUNAS ---")
print(dados_apolice_sem_vazios.columns)

print("\n--- TIPOS DE DADOS ---")
print(dados_apolice_sem_vazios.dtypes)

print("\n--- PRIMEIRAS LINHAS ---")
print(dados_apolice_sem_vazios.head(5)) #serve para visualizar rapidamente as primeiras linhas de um DataFrame — como uma amostra inicial dos dados.

# O parâmetro sheet_name do pd.read_excel() serve para especificar qual aba (ou abas) do arquivo Excel você quer ler. Isso é útil 
# quando o Excel tem várias planilhas e você só quer trabalhar com uma delas — ou com todas.
# ele iria no mesmo local do na_values



