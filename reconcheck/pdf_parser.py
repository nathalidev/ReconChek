from PyPDF2 import PdfReader
import pandas as pd

def extrair_texto_pdf(caminho):
    textos = ""
    with open(caminho, "rb") as arquivo_pdf: #abro o pdf e jogo na varial
        leitor_pdf = PdfReader(arquivo_pdf) #crio o objeto leitor_pdf que lê o arquivo pdf
        # texto_formatado = ""

        for numero_pagina in range(len(leitor_pdf.pages)): #itero sobre cada página do pdf
            pagina = leitor_pdf.pages[numero_pagina] #pego a leitura da página atual
            texto = pagina.extract_text() #extraio o texto lido da página atual
            textos += texto + "\n"  # concateno o texto extraído de cada página em uma única string, separando por quebras de linha
    return textos

def processar_texto(textos):
    registros = []
    registro_atual = {}
    for linha in textos.splitlines(): #o splitlines quebra um texto em uma lista de linhas
        if ":" in linha:
            chave, valor = linha.split(":", 1) # se tiver : na linha separo em chave e valor a partir do 1° :
            registro_atual[chave.strip()] = valor.strip() # defino o dicionario atual com chave e valor, removendo espaços em branco
            if registro_atual:
                registros.append(registro_atual) # adiciono o dicionario atual na lista de registros
    tabela_pronta = pd.DataFrame(registros) # monto a tabela pronta a partir da lista de registros

    return tabela_pronta

def exibir_conteudo(texto):
    texto_formatado = ""
    for linha in texto.splitlines():
        if ":" not in linha:
            texto_formatado += "\n" + linha
        else:
            texto_formatado += linha
        texto_formatado += "\n"
    return texto_formatado

extrair_texto_pdf("/home/natha/Área de trabalho/ReconChek/data/apolice_vida_ficticia.pdf")
print(processar_texto(extrair_texto_pdf("/home/natha/Área de trabalho/ReconChek/data/apolice_vida_ficticia.pdf")))
# print(exibir_conteudo(extrair_texto_pdf("/home/natha/Área de trabalho/ReconChek/data/apolice_vida_ficticia.pdf")))
