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
janela._set_appearance_mode("dark") #modo escuro definido
#system pega o tema do sistema

#criando novva janela ===aula4===
def nova_tela():
    nova_janela = ctk.CTkToplevel(janela)
    nova_janela.geometry("200x200")
    nova_janela.mainloop()

btn_novtela = ctk.CTkButton(master=janela,text="abrir nova janela", command=nova_tela).place(x=300,y=100)
janela.mainloop()