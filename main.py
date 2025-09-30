import os
import qrcode
import tkinter as tk
from tkinter import PhotoImage, messagebox

caminho_base = os.path.dirname(__file__)

def add_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry.config(fg="grey")

    def comFoco(event):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def semFoco(event):
        if not entry.get():
            entry.insert(0, placeholder_text)
            entry.config(fg="grey")

    entry.bind("<FocusIn>", comFoco)
    entry.bind("<FocusOut>", semFoco)

class GeradorQRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MeuQR Code")
        self.root.geometry("450x250")
        self.root.resizable(False, False)
        self.pasta_destino = "Meus_QR_Codes"
        os.makedirs(self.pasta_destino, exist_ok=True)
        caminho_icone = os.path.join(caminho_base, "assets", "qrCode.png")
        imagem_icone = PhotoImage(file=caminho_icone)
        self.root.iconphoto(True, imagem_icone)

        # Estilo simples
        self.root.configure(bg="#f0f0f0")

        # Widgets
        # Texto ou Link
        tk.Label(root, text="Texto ou Link:", bg="#f0f0f0", fg="#333", font=("Arial", 12)).pack(pady=(10, 0))
        self.input_dados = tk.Entry(root, width=40)
        self.input_dados.pack(pady=5)
        add_placeholder(self.input_dados, "Ex: https://www.google.com ou Olá Mundo")

        # Nome do arquivo
        tk.Label(root, text="Nome do Arquivo (sem .png):", bg="#f0f0f0", fg="#333", font=("Arial", 12)).pack(pady=(10, 0))
        self.input_nome = tk.Entry(root, width=40)
        self.input_nome.pack(pady=5)
        add_placeholder(self.input_nome, "Ex: meuQRCode")

        # Botão Gerar QR Code
        self.botao = tk.Button(root, text="Gerar QR Code", command=self.gerar_qr_code,
                               bg="#333", fg="white", font=("Arial", 12, "bold"), padx=40, pady=2)
        self.botao.pack(pady=20)

        self.label_feedback = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 10))
        self.label_feedback.pack()

    def gerar_qr_code(self):
        dados = self.input_dados.get().strip()
        nome_arquivo = self.input_nome.get().strip()

        if not dados or not nome_arquivo:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
            return

        nome_arquivo_limpo = "".join(c for c in nome_arquivo if c.isalnum() or c in ('-', '_')).rstrip()
        if not nome_arquivo_limpo:
            messagebox.showwarning("Erro", "Nome de arquivo inválido.")
            return

        try:
            caminho_completo = os.path.join(self.pasta_destino, f"{nome_arquivo_limpo}.png")
            img = qrcode.make(dados)
            img.save(caminho_completo)

            self.label_feedback.config(text=f"Salvo em: {caminho_completo}", fg="green")
            messagebox.showinfo("Sucesso!", f"QR Code '{nome_arquivo_limpo}.png' gerado com sucesso!")

        except Exception as e:
            self.label_feedback.config(text="Ocorreu um erro.", fg="red")
            messagebox.showerror("Erro!", f"Não foi possível gerar o QR Code:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GeradorQRCodeApp(root)
    root.mainloop()
