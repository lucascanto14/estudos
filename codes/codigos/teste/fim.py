import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def salvar_arquivo_individual(xml_raiz, pasta_destino, nome_clip):
    """Função auxiliar para formatar e gravar um XML individual no disco"""
    # Transforma a estrutura XML em string usando o padrão puro do Python
    xml_string = ET.tostring(xml_raiz, encoding='utf-8')
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
            messagebox.showinfo("Sucesso", f"Conversão concluída!\nForam gerados {total_gerado} arquivos XML.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na conversão: {e}")

def processar_conversao_por_trajetoria(txt_path):
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    pasta_destino = os.path.dirname(txt_path)

    id_camera_detetado = "UNKNOWN"
    for line in lines:
        if "FF  folder" in line or "FF_" in line:
            match = re.search(re.compile(r'(BR\d+|[A-Za-z]+\d+)'), line)
            if match:
                id_camera_detetado = match.group(1)
                break

    root_xml = None
    container_objetos = None
    clip_name_atual = None
    proxima_linha_e_calibracao = False
    contador_trajetorias = 0

    for line in lines:
        line = line.strip()
        
        if line.startswith("FF_") and line.endswith(".fits"):
            if root_xml is not None and clip_name_atual is not None:
                salvar_arquivo_individual(root_xml, pasta_destino, clip_name_atual)
                contador_trajetorias += 1
            
            clip_name_atual = line.replace(".fits", "")
            parts_name = line.split('_')
            date_str = parts_name[2]
            time_str = parts_name[3]
            
            current_attribs = {
                "version": "200",
                "clip_name": clip_name_atual,
                "y": date_str[:4], "mo": str(int(date_str[4:6])), "d": str(int(date_str[6:8])),
                "h": time_str[:2], "m": time_str[2:4], "s": time_str[4:6],
                "lid": id_camera_detetado,
                "cam": id_camera_detetado
            }
            
            root_xml = ET.Element("ufoanalyzer_record", **current_attribs)
            container_objetos = ET.SubElement(root_xml, "ua2_objects")
            
            proxima_linha_e_calibracao = False
            continue

        if "Cam# Meteor#" in line:
            proxima_linha_e_calibracao = True
            continue

        if proxima_linha_e_calibracao and root_xml is not None:
            cal_data = line.split()
            if len(cal_data) >= 10:
                root_xml.attrib.update({
                    "sid": cal_data[1],
                    "fps": str(float(cal_data[3])),
                    "az": str(float(cal_data[8])),   
                    "ev": str(float(cal_data[9]))    
                })
            proxima_linha_e_calibracao = False
            continue

        if not line or line.startswith("-") or "Recalibrated" in line or "Per segment" in line:
            continue
        if any(line.startswith(cam_id) for cam_id in [id_camera_detetado, "BR"]) and not line.endswith(".fits") and not proxima_linha_e_calibracao:
            continue

        data = line.split()
        if len(data) >= 12 and container_objetos is not None and not proxima_linha_e_calibracao:
            try:
                # Cria a tag de forma simples e direta, sem inserção de texto fantasma
                ET.SubElement(container_objetos, "ua2_fdata2",
                              fno=data[0].zfill(4), 
                              ra=data[3], 
                              dec=data[4],
                              az=data[5], 
                              ev=data[6], 
                              mag=data[9])
            except: 
                continue

    if root_xml is not None and clip_name_atual is not None:
        salvar_arquivo_individual(root_xml, pasta_destino, clip_name_atual)
        contador_trajetorias += 1

    return contador_trajetorias

if __name__ == "__main__":
    selecionar_e_converter()