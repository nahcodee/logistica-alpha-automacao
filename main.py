from tkinter import *
from tkinter import messagebox
import funcoes

janela = Tk()
janela.title("Projeto Scrum - Logística")
janela.geometry("400x450")
janela.configure(bg="#f0f0f0")

# --- JANELA DE FRETES ---
def abrir_janela_fretes():
    top = Toplevel(janela)
    top.title("Adicionar Fretes")
    top.geometry("300x500")
    
    Label(top, text="Registro:").pack(pady=5)
    e_reg = Entry(top)
    e_reg.pack()
    
    Label(top, text="Origem:").pack(pady=5)
    e_orig = Entry(top)
    e_orig.pack()
    
    Label(top, text="Destino:").pack(pady=5)
    e_dest = Entry(top)
    e_dest.pack()
    
    Label(top, text="Cliente:").pack(pady=5)
    e_cli = Entry(top)
    e_cli.pack()
    
    Label(top, text="Produto:").pack(pady=5)
    e_prod = Entry(top)
    e_prod.pack()
    
    Label(top, text="Status:").pack(pady=5)
    e_stat = Entry(top)
    e_stat.pack()

    def salvar():
        funcoes.salvar_frete(e_reg.get(), e_orig.get(), e_dest.get(), e_cli.get(), e_prod.get(), e_stat.get())
        e_reg.delete(0, END) 

    Button(top, text="SALVAR", bg="#4CAF50", fg="white", command=salvar).pack(pady=20)

# --- JANELA DE CLIENTES ---
def abrir_janela_clientes():
    top = Toplevel(janela)
    top.title("Gerenciar Clientes")
    top.geometry("300x450")
    
    Label(top, text="Registro Cliente:").pack(pady=5)
    e_reg = Entry(top)
    e_reg.pack()

    Label(top, text="Nome:").pack(pady=5)
    e_nome = Entry(top)
    e_nome.pack()

    Label(top, text="Sobrenome:").pack(pady=5)
    e_sobre = Entry(top)
    e_sobre.pack()

    Label(top, text="Cidade:").pack(pady=5)
    e_cid = Entry(top)
    e_cid.pack()
    
    Label(top, text="Bairro:").pack(pady=5)
    e_bairro = Entry(top)
    e_bairro.pack()

    def salvar():
        funcoes.salvar_cliente(e_reg.get(), e_nome.get(), e_sobre.get(), e_cid.get(), e_bairro.get())
        e_reg.delete(0, END)
        e_nome.delete(0, END)
        e_sobre.delete(0, END)

    Button(top, text="SALVAR CLIENTE", bg="#2196F3", fg="white", command=salvar).pack(pady=20)

# --- TELA PRINCIPAL ---
Label(janela, text="Logística Alpha", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)

Button(janela, text="Adicionar Fretes", command=abrir_janela_fretes, width=25, height=2).pack(pady=10)
Button(janela, text="Cadastrar Clientes", command=abrir_janela_clientes, width=25, height=2).pack(pady=10)
Button(janela, text="Sair", command=janela.quit, width=25, height=2, bg="#ffcccc").pack(pady=10)

janela.mainloop()