import tkinter as tk
from tkinter import messagebox
from datetime import datetime

tarefas = []

def adicionar_tarefa():
    tarefa = entry_tarefa.get()
    if tarefa:
        tarefas.append({"tarefa": tarefa, "data": datetime.now()})
        listbox_tarefas.insert(tk.END, f"{tarefa} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        entry_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa.")

def concluir_tarefa():
    indice_selecionado = listbox_tarefas.curselection()
    if indice_selecionado:
        tarefa_concluida = tarefas.pop(indice_selecionado[0])
        listbox_tarefas.delete(indice_selecionado)
        messagebox.showinfo("Concluído", f"Tarefa '{tarefa_concluida['tarefa']}' concluída!")

# Interface gráfica
root = tk.Tk()
root.title("Gerenciador de Tarefas")
label = tk.Label(root, text="Tarefa:")
label.pack(pady=5)
entry_tarefa = tk.Entry(root, width=30)
entry_tarefa.pack(pady=5)
botao_adicionar = tk.Button(root, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(pady=10)
listbox_tarefas = tk.Listbox(root, width=40, height=10)
listbox_tarefas.pack()
botao_concluir = tk.Button(root, text="Concluir Tarefa", command=concluir_tarefa)
botao_concluir.pack(pady=5)
root.mainloop()