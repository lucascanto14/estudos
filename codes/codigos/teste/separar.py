import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

# CONFIGURAÇÃO GEOGRÁFICA FIXA DA SUA ESTAÇÃO
DADOS_GEOGRAFICOS = {
    "lng": "-45.189701",
    "lat": "-22.811001",
    "alt": "549.000000",
    "observer": "D._MOURAO",
    "lens": "Fujinon_F1.3",
    "cap": "Easycap",
    "u2": "224",
    "ua": "244",
    "memo": ""
}

def salvar_arquivo_individual(xml_raiz, pasta_destino, nome_clip):
    """Função auxiliar para formatar e gravar um XML individual no disco"""
    # Adicione o argumento short_empty_elements=False
    xml_string = ET.tostring(xml_raiz, encoding='utf-8', short_empty_elements=False)
    pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
    
    # Define o nome do arquivo usando o nome do clip da trajetória
    caminho_saida = os.path.join(pasta_destino, f"{nome_clip}.xml")
    with open(caminho_saida, "w", encoding='utf-8') as f:
        f.write(pretty_xml)

def selecionar_e_converter():
    root = tk.Tk()
    root.withdraw()

    caminho_do_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo TXT do RMS",
        filetypes=(("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*"))
    )

    if caminho_do_arquivo:
        try:
            total_gerado = processar_conversao_por_trajetoria(caminho_do_arquivo)
            messagebox.showinfo("Sucesso", f"Conversão concluída!\nForam gerados {total_gerado} arquivos XML individuais nesta pasta.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na conversão: {e}")

def processar_conversao_por_trajetoria(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Define a pasta onde os novos arquivos XML serão salvos (a mesma do TXT)
    pasta_destino = os.path.dirname(txt_path)

    id_camera_detetado = "UNKNOWN"
    # Passo 1: Descobrir o ID da câmara
    for line in lines:
        if "FF  folder" in line or "FF_" in line:
            match = re.search(re.compile(r'(BR\d+|[A-Za-z]+\d+)'), line)
            if match:
                id_camera_detetado = match.group(1)
                break

    # Variáveis de controle para separação dos arquivos
    root_xml = None
    current_event = None
    clip_name_atual = None
    proxima_linha_e_calibracao = False
    contador_trajetorias = 0

    # Passo 2: Processamento e estruturação por blocos
    for line in lines:
        line = line.strip()
        
        # Identifica o início de uma nova trajetória
        if line.startswith("FF_") and line.endswith(".fits"):
            
            # --- MUDANÇA LÓGICA AQUI ---
            # Se já existia um XML sendo populado, significa que terminamos uma 
            # trajetória anterior. Vamos salvá-la antes de resetar a estrutura.
            if root_xml is not None and clip_name_atual is not None:
                salvar_arquivo_individual(root_xml, pasta_destino, clip_name_atual)
                contador_trajetorias += 1
            
            # Agora recriamos uma nova raiz XML totalmente limpa para o novo meteoro
            root_xml = ET.Element("ufoanalyzer_record", version="200")
            clip_name_atual = line.replace(".fits", "")
            
            parts_name = line.split('_')
            date_str = parts_name[2]
            time_str = parts_name[3]
            
            current_attribs = {
                "clip_name": clip_name_atual,
                "y": date_str[:4], "mo": date_str[4:6], "d": date_str[6:8],
                "h": time_str[:2], "m": time_str[2:4], "s": time_str[4:6],
                "lid": id_camera_detetado,
                "cam": id_camera_detetado
            }
            current_attribs.update(DADOS_GEOGRAFICOS)
            
            current_event = ET.SubElement(root_xml, "event", **current_attribs)
            proxima_linha_e_calibracao = False
            continue

        # Identifica que a próxima linha contém os dados de calibração da câmara
        if "Cam# Meteor#" in line:
            proxima_linha_e_calibracao = True
            continue

        # Processa a linha de calibração geométrica
        if proxima_linha_e_calibracao and current_event is not None:
            cal_data = line.split()
            if len(cal_data) >= 10:
                current_event.attrib.update({
                    "sid": cal_data[1],
                    "fps": str(float(cal_data[3])),
                    "az": str(float(cal_data[8])),   
                    "ev": str(float(cal_data[9]))    
                })
            proxima_linha_e_calibracao = False
            continue

        # Ignora linhas decorativas e de cabeçalho secundárias
        if not line or line.startswith("-") or "Recalibrated" in line or "Per segment" in line:
            continue
        if any(line.startswith(cam_id) for cam_id in [id_camera_detetado, "BR"]) and not line.endswith(".fits") and not proxima_linha_e_calibracao:
            continue

        # Processa as coordenadas dos segmentos (Frames de dados) da trajetória ATUAL
        data = line.split()
        if len(data) >= 12 and current_event is not None and not proxima_linha_e_calibracao:
            try:
                ET.SubElement(current_event, "ua2_fdata2",
                              fno=data[0].split('.')[0], 
                              ra=data[3], 
                              dec=data[4],
                              az=data[5], 
                              ev=data[6], 
                              mag=data[9])
            except: 
                continue

    # --- MUDANÇA LÓGICA AQUI ---
    # Ao sair do loop, a última trajetória do arquivo não terá um próximo "FF_" para disparar
    # o salvamento dela. Por isso, precisamos salvá-la manualmente aqui no final.
    if root_xml is not None and clip_name_atual is not None:
        salvar_arquivo_individual(root_xml, pasta_destino, clip_name_atual)
        contador_trajetorias += 1

    return contador_trajetorias

if __name__ == "__main__":
    selecionar_e_converter()