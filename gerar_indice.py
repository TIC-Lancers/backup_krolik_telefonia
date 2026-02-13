import os
import re
import json
from datetime import datetime

def obter_caminhos():
    # O script está em .../app/
    pasta_app = os.path.dirname(os.path.abspath(__file__))
    # A raiz dos dados está em .../TI - Gravações Telefonia Krolik/
    raiz_dados = os.path.dirname(pasta_app)
    return raiz_dados, pasta_app

def analisar_arquivo(nome_arquivo):
    # Padrões de Regex (mantidos os mesmos)
    padrao_saida = re.match(r"(\d{8})_(\d{6})_(\d+)_(\d+)_(\d+)_(\d+)\.mp3", nome_arquivo)
    padrao_entrada = re.match(r"(\d{8})_(\d{6})_(\d+)_(\d+)_(\d+)\.mp3", nome_arquivo)

    dados = {}
    if padrao_saida:
        g = padrao_saida.groups()
        dados = {'data_raw': g[0], 'hora_raw': g[1], 'origem': g[2], 'destino': g[4], 'tipo': 'Saída', 'id': g[5]}
    elif padrao_entrada:
        g = padrao_entrada.groups()
        dados = {'data_raw': g[0], 'hora_raw': g[1], 'origem': g[2], 'destino': g[3], 'tipo': 'Entrada', 'id': g[4]}
    else:
        return None

    # Formatação Visual
    try:
        dados['data'] = datetime.strptime(dados['data_raw'], "%Y%m%d").strftime("%d/%m/%Y")
        dados['hora'] = datetime.strptime(dados['hora_raw'], "%H%M%S").strftime("%H:%M:%S")
    except:
        dados['data'] = dados['data_raw']
        dados['hora'] = dados['hora_raw']
        
    return dados

def gerar_base_dados():
    raiz_dados, pasta_app = obter_caminhos()
    print(f"--- GERANDO BASE PARA WEB ---")
    
    lista_final = []
    
    for pasta_ano in os.listdir(raiz_dados):
        caminho_ano = os.path.join(raiz_dados, pasta_ano)
        if os.path.isdir(caminho_ano) and pasta_ano.lower().startswith('gravacoes_'):
            print(f"Processando: {pasta_ano}...")
            
            for raiz, subs, arquivos in os.walk(caminho_ano):
                for arq in arquivos:
                    if arq.lower().endswith('.mp3'):
                        meta = analisar_arquivo(arq)
                        if meta:
                            caminho_completo = os.path.join(raiz, arq)
                            # GERA O CAMINHO RELATIVO (Fundamental para o HTML funcionar)
                            # Ex: ../gravacoes_2024/01_Janeiro/arquivo.mp3
                            caminho_relativo = os.path.relpath(caminho_completo, pasta_app)
                            # Corrige barras invertidas do Windows para barras normais de web
                            meta['caminho'] = caminho_relativo.replace("\\", "/")
                            meta['nome_arquivo'] = arq
                            lista_final.append(meta)

    # Salva como um arquivo Javascript (Variável Global)
    # Isso evita erro de CORS (Cross-Origin) ao abrir localmente
    caminho_js = os.path.join(pasta_app, "banco_dados.js")
    
    conteudo_js = f"window.DADOS_GRAVACOES = {json.dumps(lista_final, ensure_ascii=False)};"
    
    with open(caminho_js, "w", encoding="utf-8") as f:
        f.write(conteudo_js)
        
    print(f"\nSUCESSO! Base de dados gerada com {len(lista_final)} registros.")
    print(f"Arquivo salvo: {caminho_js}")
    input("Pressione Enter para sair...")

if __name__ == "__main__":
    gerar_base_dados()
    