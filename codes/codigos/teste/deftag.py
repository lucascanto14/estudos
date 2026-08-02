def salvar_arquivo_individual(xml_raiz, pasta_destino, nome_clip):
    """Função auxiliar para formatar e gravar um XML individual no disco"""
    xml_string = ET.tostring(xml_raiz, encoding='utf-8', short_empty_elements=False)
    pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")
    
    # --- A SOLUÇÃO DEFINITIVA AQUI ---
    # Se o minidom insistir em colocar a barra (ex: '/>'), nós quebramos ela 
    # transformando textualmente em '></ua2_fdata2>' linha por linha.
    linhas_corrigidas = []
    for linha in pretty_xml.splitlines():
        if "<ua2_fdata2" in linha and "/>" in linha:
            # Substitui a barra de fechamento curto pelo fechamento longo explícito
            linha = linha.replace("/>", "></ua2_fdata2>")
        linhas_corrigidas.append(linha)
    
    # Junta as linhas de volta em um único texto
    xml_final_perfeito = "\n".join(linhas_corrigidas)
    
    # Define o nome do arquivo usando o nome do clip da trajetória
    caminho_saida = os.path.join(pasta_destino, f"{nome_clip}.xml")
    with open(caminho_saida, "w", encoding='utf-8') as f:
        f.write(xml_final_perfeito)