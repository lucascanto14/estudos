import customtkinter as ctk
janela = ctk.CTk()
janela.geometry("700x400") #tamanho da janela em pixels 
janela.title("teste baja")
janela.maxsize(width=900, height=550) #tamanho maximo tela cheia
janela.minsize(width=500, height=300) #tamanho minimo da tela
janela.resizable(width=False, height=False )
#janela.iconify() #minimiza a janela
#janela.deiconify() #maximiza a janela

#custumizar tema aplicacao  ===aula3===
janela._set_appearance_mode("system") #modo escuro definido
#system pega o tema do sistema

#aula5 = frame
frame1 = ctk.CTkFrame(master = janela, width=200, height=330, fg_color="teal", bg_color="transparent", border_width=10, corner_radius=30).place(x=10,y=60)
frame2 = ctk.CTkFrame(janela, width=200,height=330, fg_color="teal", bg_color="transparent", border_width=10, corner_radius=30).place(x=220,y=60)
frame3 = ctk.CTkFrame(janela, width=200,height=330, fg_color="teal", bg_color="transparent", border_width=10, corner_radius=30).place(x=430,y=60)
janela.mainloop()