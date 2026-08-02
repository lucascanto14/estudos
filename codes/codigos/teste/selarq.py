import xml.etree.ElementTree as ET
from xml.dom import minidom
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def selecionar_e_converter():
    # 1. Cria uma janela oculta apenas para usar o seletor de arquivos
    root = tk.Tk()
    root.withdraw()

    # 2. Abre a janela de busca do Windows/Linux/Mac
    caminho_do_arquivo = filedialog.askopenfilename(
        title="Selecione o arquivo TXT do RMS",
        filetypes=(("Arquivos de Texto", "*.txt"), ("Todos os arquivos", "*.*"))
    )

    # 3. Se o usuário escolheu um arquivo, chama a função de conversão
    if caminho_do_arquivo:
        try:
            processar_conversao(caminho_do_arquivo)
            messagebox.showinfo("Sucesso", f"Arquivo convertido com sucesso!\nSalvo em: {caminho_do_arquivo.replace('.txt', '.xml')}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro na conversão: {e}")
    else:
        print("Nenhum arquivo foi selecionado.")

def processar_conversao(txt_path):
    # --- Aqui entra a lógica que você já tem ---
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    root_xml = ET.Element("ufoanalyzer_record", version="200")
    current_event = None

    for line in lines:
        line = line.strip()
        if line.startswith("FF_BR0017"):
            parts_name = line.split('_')
            date_str, time_str = parts_name[2], parts_name[3]
            current_event = ET.SubElement(root_xml, "event", 
                                         clip_name=line.replace(".fits", ""),
                                         y=date_str[:4], mo=date_str[4:6], d=date_str[6:8],
                                         h=time_str[:2], m=time_str[2:4], s=time_str[4:6])
            continue

        if not line or line.startswith("-") or "Recalibrated" in line:
            continue

        data = line.split()
        if len(data) >= 12 and current_event is not None:
            try:
                ET.SubElement(current_event, "ua2_fdata2",
                              fno=data[0].split('.')[0], ra=data[3], dec=data[4],
                              az=data[5], ev=data[6], mag=data[9])
            except: continue

    # Salva o arquivo XML com o mesmo nome do TXT
    xml_string = ET.tostring(root_xml, encoding='utf-8')
    pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
    output_name = txt_path.replace(".txt", ".xml")
    
    with open(output_name, "w", encoding='utf-8') as f:
        f.write(pretty_xml)

# Inicia o programa chamando o seletor
if __name__ == "__main__":
    selecionar_e_converter()