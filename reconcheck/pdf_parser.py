from PyPDF2 import PdfReader

def extrair_texto_pdf(caminho):
    with open(caminho, "rb") as arquivo_pdf:
        leitor_pdf = PdfReader(arquivo_pdf)
        texto_formatado = ""

        for numero_pagina in range(len(leitor_pdf.pages)):
            pagina = leitor_pdf.pages[numero_pagina]
            texto = pagina.extract_text()

            for linha in texto.splitlines():
                if ":" not in linha:
                    texto_formatado += "\n" + linha
                else:
                    texto_formatado += linha
                texto_formatado += "\n"

        return texto_formatado

print(extrair_texto_pdf("/home/natha/Área de trabalho/ReconChek/data/apolice_vida_ficticia.pdf"))
