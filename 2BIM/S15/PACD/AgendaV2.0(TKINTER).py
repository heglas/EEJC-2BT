import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AgendaContatos:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Contatos v2.0")
        self.contatos = []
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=25)
        
        # Criar widgets
        self.criar_widgets()
        self.carregar_contatos_iniciais()

    def criar_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame de entrada de dados
        input_frame = ttk.LabelFrame(main_frame, text="Dados do Contato", padding=10)
        input_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NSEW)

        # Campos de entrada
        campos = [
            ("Nome", "nome"),
            ("Idade", "idade"),
            ("Telefone", "telefone"),
            ("E-mail", "email"),
            ("Renda", "renda"),
            ("Estado (UF)", "estado")
        ]

        self.entries = {}
        for i, (label, field) in enumerate(campos):
            ttk.Label(input_frame, text=label+":").grid(row=i, column=0, sticky=tk.W)
            entry = ttk.Entry(input_frame, width=25)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entries[field] = entry

        # Frame de botões
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=1, column=0, pady=10, sticky=tk.EW)

        botoes = [
            ("Adicionar", self.adicionar_contato),
            ("Editar", self.editar_contato),
            ("Remover", self.remover_contato),
            ("Limpar", self.limpar_campos)
        ]

        for i, (texto, comando) in enumerate(botoes):
            ttk.Button(btn_frame, text=texto, command=comando)\
                .grid(row=0, column=i, padx=5, pady=5)

        # Treeview para exibição
        cols = ("Nome", "Telefone", "E-mail", "Idade", "Renda", "Estado")
        self.tree = ttk.Treeview(
            main_frame, 
            columns=cols, 
            show="headings",
            selectmode="browse",
            height=10
        )

        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120, anchor=tk.CENTER)

        self.tree.grid(row=2, column=0, pady=10, sticky=tk.NSEW)
        self.tree.bind("<<TreeviewSelect>>", self.preencher_campos_auto)

        # Frame de estatísticas
        stats_frame = ttk.LabelFrame(main_frame, text="Estatísticas", padding=10)
        stats_frame.grid(row=3, column=0, sticky=tk.EW)

        self.lbl_total = ttk.Label(stats_frame, text="Total: 0 contatos")
        self.lbl_total.pack(side=tk.LEFT, padx=20)

        self.lbl_media = ttk.Label(stats_frame, text="Média Idade: 0 anos")
        self.lbl_media.pack(side=tk.LEFT, padx=20)

        self.lbl_estados = ttk.Label(stats_frame, text="Estados: 0")
        self.lbl_estados.pack(side=tk.LEFT, padx=20)

    def validar_campos(self):
        campos_obrigatorios = ["nome", "telefone", "email"]
        for campo in campos_obrigatorios:
            if not self.entries[campo].get().strip():
                messagebox.showwarning("Campo obrigatório", 
                    f"O campo {campo.capitalize()} é obrigatório!")
                return False
        
        try:
            int(self.entries["idade"].get())
            float(self.entries["renda"].get())
        except ValueError:
            messagebox.showerror("Erro de formato", 
                "Idade deve ser número inteiro e Renda deve ser numérico!")
            return False
            
        return True

    def adicionar_contato(self):
        if not self.validar_campos():
            return

        novo_contato = {
            "nome": self.entries["nome"].get().title(),
            "idade": int(self.entries["idade"].get()),
            "telefone": self.entries["telefone"].get(),
            "email": self.entries["email"].get().lower(),
            "renda": float(self.entries["renda"].get()),
            "estado": self.entries["estado"].get().upper()
        }

        self.contatos.append(novo_contato)
        self.atualizar_lista()
        self.limpar_campos()
        messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")

    def editar_contato(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Seleção necessária", 
                "Selecione um contato na lista para editar!")
            return
            
        if not self.validar_campos():
            return

        index = self.tree.index(selecionado)
        self.contatos[index] = {
            "nome": self.entries["nome"].get().title(),
            "idade": int(self.entries["idade"].get()),
            "telefone": self.entries["telefone"].get(),
            "email": self.entries["email"].get().lower(),
            "renda": float(self.entries["renda"].get()),
            "estado": self.entries["estado"].get().upper()
        }

        self.atualizar_lista()
        messagebox.showinfo("Sucesso", "Contato atualizado com sucesso!")

    def remover_contato(self):
        selecionado = self.tree.selection()
        if not selecionado:
            messagebox.showwarning("Seleção necessária", 
                "Selecione um contato na lista para remover!")
            return
            
        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            "Tem certeza que deseja remover este contato?"
        )
        
        if confirmar:
            index = self.tree.index(selecionado)
            del self.contatos[index]
            self.atualizar_lista()
            self.limpar_campos()

    def limpar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

    def preencher_campos_auto(self, event):
        selecionado = self.tree.selection()
        if selecionado:
            item = self.tree.item(selecionado)
            valores = item["values"]
            campos = ["nome", "telefone", "email", "idade", "renda", "estado"]
            
            for campo, valor in zip(campos, valores):
                self.entries[campo].delete(0, tk.END)
                self.entries[campo].insert(0, valor)

    def atualizar_lista(self):
        self.tree.delete(*self.tree.get_children())
        for contato in self.contatos:
            self.tree.insert("", tk.END, values=(
                contato["nome"],
                contato["telefone"],
                contato["email"],
                contato["idade"],
                f"R$ {contato['renda']:.2f}",
                contato["estado"]
            ))
        
        self.atualizar_stats()

    def atualizar_stats(self):
        total = len(self.contatos)
        self.lbl_total.config(text=f"Total: {total} contatos")
        
        if total > 0:
            media_idade = sum(c["idade"] for c in self.contatos) / total
            self.lbl_media.config(text=f"Média Idade: {media_idade:.1f} anos")
            
            estados = len({c["estado"] for c in self.contatos})
            self.lbl_estados.config(text=f"Estados: {estados} diferentes")
        else:
            self.lbl_media.config(text="Média Idade: 0 anos")
            self.lbl_estados.config(text="Estados: 0")

    def carregar_contatos_iniciais(self):
        # Exemplos para demonstração
        exemplos = [
            {
                "nome": "Ana Silva",
                "idade": 28,
                "telefone": "(11) 9999-8888",
                "email": "ana@email.com",
                "renda": 4500.00,
                "estado": "SP"
            },
            {
                "nome": "Carlos Oliveira",
                "idade": 35,
                "telefone": "(21) 7777-5555",
                "email": "carlos@email.com",
                "renda": 6800.50,
                "estado": "RJ"
            }
        ]
        self.contatos.extend(exemplos)
        self.atualizar_lista()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaContatos(root)
    root.mainloop()
