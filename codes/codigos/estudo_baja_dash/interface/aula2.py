import customtkinter as ctk
janela = ctk.CTk()
janela.geometry("700x400") #tamanho da janela em pixels 
janela.title("teste baja")
janela.maxsize(width=900, height=550) #tamanho maximo tela cheia
janela.minsize(width=500, height=300) #tamanho minimo da tela
janela.resizable(width=False, height=False )
#janela.iconify() #minimiza a janela
#janela.deiconify() #maximiza a janela

#custumizar tema aplicacao
janela._set_appearance_mode("dark") #modo escuro definido
#system pega o tema do sistema
janela.mainloop()