import customtkinter as ctk # importando customtkinter como ctk
janela = ctk.CTk()

janela._set_appearance_mode("dark")

btn = ctk.CTkButton(janela, text = 'ola')
btn.pack()

janela.mainloop()