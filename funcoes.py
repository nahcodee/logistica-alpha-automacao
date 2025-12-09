import pandas as pd
import os
from tkinter import messagebox

# Arquivos CSV
ARQUIVO_FRETES = 'dados_frete.csv'
ARQUIVO_CLIENTES = 'dados_clientes.csv'

# --- FRETES  ---
def salvar_frete(registro, origem, destino, cliente, produto, status):
    if not registro or not cliente:
        messagebox.showwarning("Atenção", "Preencha Registro e Cliente!")
        return

    
    if os.path.exists(ARQUIVO_FRETES):
        df = pd.read_csv(ARQUIVO_FRETES)
    else:
        df = pd.DataFrame(columns=["Registro_frete", "Origem", "Destino", "Cliente", "Produto", "Status"])

    novo_dado = {
        "Registro_frete": [registro],
        "Origem": [origem],
        "Destino": [destino],
        "Cliente": [cliente],
        "Produto": [produto],
        "Status": [status]
    }
    
    df_novo = pd.DataFrame(novo_dado)
    df_final = pd.concat([df, df_novo], ignore_index=True)
    
    try:
        df_final.to_csv(ARQUIVO_FRETES, index=False)
        messagebox.showinfo("Sucesso", "Frete salvo!")
    except PermissionError:
        messagebox.showerror("Erro", "Feche o arquivo dados_frete.csv!")

# --- CLIENTES ---
def salvar_cliente(registro_cli, nome, sobrenome, cidade, bairro):
    if not nome:
        messagebox.showwarning("Atenção", "O nome é obrigatório!")
        return

    
    if os.path.exists(ARQUIVO_CLIENTES):
        df = pd.read_csv(ARQUIVO_CLIENTES)
    else:
        df = pd.DataFrame(columns=["Registro Cliente", "Nome", "Sobrenome", "Cidade", "Bairro"])

    novo_cliente = {
        "Registro Cliente": [registro_cli],
        "Nome": [nome],
        "Sobrenome": [sobrenome],
        "Cidade": [cidade],
        "Bairro": [bairro]
    }
    
    df_novo = pd.DataFrame(novo_cliente)
    df_final = pd.concat([df, df_novo], ignore_index=True)
    
    try:
        df_final.to_csv(ARQUIVO_CLIENTES, index=False)
        messagebox.showinfo("Sucesso", "Cliente salvo!")
    except PermissionError:
        messagebox.showerror("Erro", "Feche o arquivo dados_clientes.csv!")