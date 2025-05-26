import tkinter as tk
from tkinter import messagebox
from dados import adicionar_aluno, listar_alunos

# Nossas funções de interface  

def cadastrar_aluno():
    nome = entry_nome.get()
    
    try:
        nota1 = float(entry_nota1.get())
        nota2 = float(entry_nota2.get())  # Aqui definimos corretamente a nota2
    except ValueError:
        messagebox.showerror("Erro", "Notas devem ser números.")
        return

    if nome.strip() == "":
        messagebox.showwarning("Atenção", "Digite o nome do aluno.")
        return

    adicionar_aluno(nome, nota1, nota2)
    messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado com sucesso!")

    entry_nome.delete(0, tk.END)
    entry_nota1.delete(0, tk.END)
    entry_nota2.delete(0, tk.END)

def exibir_boletim():
    alunos = listar_alunos()
    if not alunos:
        messagebox.showinfo("Boletim", "Nenhum aluno cadastrado.")
        return

    janela_boletim = tk.Toplevel()
    janela_boletim.title("Boletim de Alunos")

    for i, aluno in enumerate(alunos):
        texto = f"{aluno['nome']} | Nota 1: {aluno['nota1']} | Nota 2: {aluno['nota2']} | Média: {aluno['media']:.2f} | Situação: {aluno['status']}"
        tk.Label(janela_boletim, text=texto).pack(anchor='w', padx=10, pady=2)

# Janela principal  
janela = tk.Tk()
janela.title("Projeto Boletim Escolar")

# Rótulos e campos de entrada
tk.Label(janela, text="Nome do aluno:").grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="Nota 1:").grid(row=1, column=0, padx=5, pady=5)
entry_nota1 = tk.Entry(janela)
entry_nota1.grid(row=1, column=1)

tk.Label(janela, text="Nota 2:").grid(row=2, column=0, padx=5, pady=5)
entry_nota2 = tk.Entry(janela)
entry_nota2.grid(row=2, column=1)

# Botões
tk.Button(janela, text="Cadastrar Aluno", command=cadastrar_aluno).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(janela, text="Visualizar Boletim", command=exibir_boletim).grid(row=4, column=0, columnspan=2)

janela.mainloop()
