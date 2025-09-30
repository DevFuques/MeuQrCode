import sys
import os
import qrcode
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox
)
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt


class GeradorQRCodeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.pasta_destino = "Meus_QR_Codes"
        self.initUI()

    def initUI(self):
        caminho_base = os.path.dirname(__file__)

        self.setWindowTitle("Gerador de QR Code")
        icone_path = os.path.join(caminho_base, "assets", "qrCode.png")
        if os.path.exists(icone_path):
            self.setWindowIcon(QIcon(icone_path))
        self.setFixedSize(450, 300)

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                color: #333;
                font-family: Arial, sans-serif;
            }
            QLabel {
                font-size: 14px;
            }
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #ccc;
                padding: 8px;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #333;
                color: #ffffff;
                border: none;
                padding: 10px 15px;
                font-size: 15px;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #555;
            }
            QPushButton:pressed {
                background-color: #222;
            }
        """)

        layout_principal = QVBoxLayout()
        layout_principal.setSpacing(15)
        layout_principal.setContentsMargins(20, 20, 20, 20)

        label_dados = QLabel("Texto ou Link para o QR Code:")
        self.input_dados = QLineEdit()
        self.input_dados.setPlaceholderText("Ex: https://www.google.com")

        label_nome_arquivo = QLabel("Nome do Arquivo (sem .png):")
        self.input_nome_arquivo = QLineEdit()
        self.input_nome_arquivo.setPlaceholderText("Ex: meu-site")

        self.botao_gerar = QPushButton("Gerar QR Code")
        self.botao_gerar.clicked.connect(self.gerar_qr_code)

        self.label_feedback = QLabel("")
        self.label_feedback.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_principal.addWidget(label_dados)
        layout_principal.addWidget(self.input_dados)
        layout_principal.addSpacing(10)
        layout_principal.addWidget(label_nome_arquivo)
        layout_principal.addWidget(self.input_nome_arquivo)
        layout_principal.addStretch()
        layout_principal.addWidget(self.botao_gerar)
        layout_principal.addWidget(self.label_feedback)

        self.setLayout(layout_principal)

    def gerar_qr_code(self):
        dados = self.input_dados.text()
        nome_arquivo = self.input_nome_arquivo.text()

        if not dados or not nome_arquivo:
            self.mostrar_mensagem("Erro", "Por favor, preencha todos os campos.", QMessageBox.Warning)
            return

        nome_arquivo_limpo = "".join(c for c in nome_arquivo if c.isalnum() or c in ('-', '_')).rstrip()
        if not nome_arquivo_limpo:
            self.mostrar_mensagem("Erro", "O nome do arquivo é inválido.", QMessageBox.Warning)
            return

        try:
            if not os.path.exists(self.pasta_destino):
                os.makedirs(self.pasta_destino)

            caminho_completo = os.path.join(self.pasta_destino, f"{nome_arquivo_limpo}.png")
            imagem_qr = qrcode.make(dados)
            imagem_qr.save(caminho_completo)

            self.label_feedback.setText(f"Salvo em: {caminho_completo}")
            self.label_feedback.setStyleSheet("color: green; font-weight: bold;")
            self.mostrar_mensagem("Sucesso", f"QR Code '{nome_arquivo_limpo}.png' gerado com sucesso!", QMessageBox.Information)

        except Exception as e:
            self.label_feedback.setText("Ocorreu um erro.")
            self.label_feedback.setStyleSheet("color: red; font-weight: bold;")
            self.mostrar_mensagem("Erro na Geração", f"Não foi possível gerar o QR Code: {e}", QMessageBox.Critical)

    def mostrar_mensagem(self, titulo, texto, icone):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(titulo)
        msg_box.setText(texto)
        msg_box.setIcon(icone)
        msg_box.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = GeradorQRCodeApp()
    janela.show()
    sys.exit(app.exec())
