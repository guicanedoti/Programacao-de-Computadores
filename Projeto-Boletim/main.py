import tkinter as tk
from tkinter import ttk
import csv
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def salvar_boletim():
    nome = entry_nome.get()
    notas = [float(entry.get()) for entry in entries_notas]
    media = sum(notas) / len(notas)

    with open('Projeto-Boletim/boletim.csv', mode='a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome] + notas + [media])

    limpar_campos()

def limpar_campos():
    entry_nome.delete(0, tk.END)
    for entry in entries_notas:
        entry.delete(0, tk.END)

def abrir_no_excel():
    caminho = os.path.abspath("Projeto-Boletim/boletim.csv")
    os.startfile(caminho)  # Funciona apenas no Windows

# Interface gráfica
janela = tk.Tk()
janela.title("Boletim Escolar")

tk.Label(janela, text="Nome do Aluno:").grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

entries_notas = []
for i in range(4):
    tk.Label(janela, text=f"Nota {i+1}:").grid(row=i+1, column=0, padx=5, pady=5)
    entry = tk.Entry(janela)
    entry.grid(row=i+1, column=1, padx=5, pady=5)
    entries_notas.append(entry)

# Botões
ttk.Button(janela, text="Salvar", command=salvar_boletim).grid(row=5, column=0, padx=5, pady=10)
ttk.Button(janela, text="Abrir no Excel", command=abrir_no_excel).grid(row=5, column=1, padx=5, pady=10)

janela.mainloop()
