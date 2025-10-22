import pandas as pd

dados_apolice_vida = pd.read_excel("/home/nath/ReconChek/data/apolice_vida_corrigida.xlsx", na_values=['N/A', 'sem dados', '-'])

#skiprows=3 para pular as 3 primeiras linhas do arquivo excel.

dados_apolice_sem_vazios = dados_apolice_vida.dropna() # Remover linhas com valores ausentes

# O parâmetro sheet_name do pd.read_excel() serve para especificar qual aba (ou abas) do arquivo Excel você quer ler. Isso é útil 
# quando o Excel tem várias planilhas e você só quer trabalhar com uma delas — ou com todas.
# ele iria no mesmo local do na_values



