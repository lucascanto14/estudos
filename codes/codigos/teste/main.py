import xml.etree.ElementTree as ET
from xml.dom import minidom
import os

def parse_rms_txt_to_ufo_xml(txt_path):
    if not os.path.exists(txt_path):
        print(f"Arquivo {txt_path} não encontrado.")
        return

    with open(txt_path, 'r') as f:
        lines = f.readlines()

    # Criar o elemento raiz do XML
    root = ET.Element("ufoanalyzer_record", version="200")
    
    current_event = None

    for line in lines:
        line = line.strip()

        # 1. Detecta o início de um novo meteoro pelo nome do arquivo .fits
        if line.startswith("FF_BR0017"):
            # Extrair metadados básicos do nome do arquivo (ex: Data e Hora)
            # FF_BR0017_20260418_023723...
            parts_name = line.split('_')
            date_str = parts_name[2] # 20260418
            time_str = parts_name[3] # 023723
            
            current_event = ET.SubElement(root, "event", 
                                         clip_name=line.replace(".fits", ""),
                                         y=date_str[:4], mo=date_str[4:6], d=date_str[6:8],
                                         h=time_str[:2], m=time_str[2:4], s=time_str[4:6])
            continue

        # 2. Ignora cabeçalhos e linhas vazias
        if not line or line.startswith("-") or "Recalibrated" in line or "Cam#" in line or "Per segment" in line:
            continue

        # 3. Processa as linhas de dados (segmentos do meteoro)
        # Exemplo de linha: 0043.1396 0238.22 0100.52 231.223726 -28.541710 ...
        data = line.split()
        
        # Uma linha de dados válida do RMS costuma ter 12 ou 13 colunas
        if len(data) >= 12 and current_event is not None:
            try:
                # Mapeamento baseado na estrutura do seu arquivo TXT:
                # index 0: Frame#, 3: RA, 4: Dec, 5: Azim, 6: Elev, 9: Mag
                ET.SubElement(current_event, "ua2_fdata2",
                              fno=data[0].split('.')[0], # Apenas a parte inteira do frame
                              ra=data[3],
                              dec=data[4],
                              az=data[5],
                              ev=data[6],
                              mag=data[9])
            except ValueError:
                continue

    # 4. Salvar e formatar o XML
    xml_string = ET.tostring(root, encoding='utf-8')
    pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
    
    output_name = txt_path.replace(".txt", ".xml")
    with open(output_name, "w", encoding='utf-8') as f:
        f.write(pretty_xml)
    
    print(f"Sucesso! Arquivo gerado: {output_name}")

# Executar
parse_rms_txt_to_ufo_xml("FTPdetectinfo_BR0017_20260417_222110_654516.txt")