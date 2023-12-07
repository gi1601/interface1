import customtkinter as Tk
Tk .set_appearance_mode ("System")

janela = Tk .CTk()
janela.title("Janela 1")
janela.geometry("400x350")
janela.resizable(width=False, height=False)

colunas = list (range(13))
linhas = list (range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)


def verificar():
    n1 = int(caixa1.get())
    n2 = int(caixa2.get())

    media = (n1 + n2) / 2
    if media >= 6:
        texto1.configure(text="Aprovado")
    else:
        texto1.configure(text="Reprovado")


texto1= Tk.CTkLabel(janela, text="Digite...")
texto1.grid(row=6, column=6)


caixa1=Tk.CTkEntry(janela, placeholder_text="Digite a primeira nota", width=200, height=30)
caixa1.grid(row=7, column=6)


caixa2=Tk.CTkEntry(janela, placeholder_text="Digite a segunda nota", width=200, height=30)
caixa2.grid(row=8, column=6)


btn1= Tk.CTkButton(janela, text="Clique Aqui", command= verificar, width=100, height=30, fg_color='DarkTurquoise')
btn1.grid (row=9, column=6)


janela.mainloop()
