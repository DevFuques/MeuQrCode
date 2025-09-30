# MeuQR Code

Um aplicativo simples em **Python** para gerar QR Codes a partir de textos ou links.  
O programa utiliza **Tkinter** para a interface gráfica e salva os QR Codes em uma pasta dedicada.

---

## 🖥️ Funcionalidades

- Interface gráfica intuitiva usando Tkinter.
- Permite gerar QR Codes a partir de qualquer texto ou URL.
- Salva os QR Codes automaticamente na pasta `Meus_QR_Codes`.
- Suporte a placeholders nos campos de entrada.
- Feedback visual para sucesso ou erro na geração.

---

## 🛠 Tecnologias utilizadas
- Python 3
- Tkinter
- qrcode

---

## 📂 Estrutura do projeto
<p align= "center">
<img width="355" height="191" alt="image" src="https://github.com/user-attachments/assets/3895d31a-e831-4736-8a40-a632f9e29e9e" />
</p>

---

## ⚙️ Requisitos

- Python 3.8+
- Biblioteca qrcode:
```bash
pip install qrcode[pil]
```
- Tkinter (geralmente já incluído no Python padrão)

---

## ⚙️ Como executar

1️⃣ Clone o repositório:
```bash
git clone https://github.com/seu-usuario/meuqr-code.git
```
2️⃣ Instale a biblioteca necessária:
```bash
pip install -r requirements.txt
```
3️⃣ Execute o programa:
```bash
python main.py
```
4️⃣ Preencha os campos:
- Texto ou Link: O conteúdo que será transformado em QR Code.
- Nome do Arquivo: Nome do arquivo PNG (sem .png).

5️⃣ Clique em Gerar QR Code e o arquivo será salvo em Meus_QR_Codes.

---

## 📝 Observações

- O programa não precisa de Qt ou outras bibliotecas externas, então funciona diretamente no Linux, Windows e macOS.
- Nomes de arquivos inválidos (com caracteres especiais) serão filtrados automaticamente.

---

## 📸 Demonstração
<p  align= "center">
<img width="467" height="303" alt="Captura de tela de 2025-09-30 13-55-29" src="https://github.com/user-attachments/assets/81ad59c0-7b30-4645-a211-f3872f26c0a7" />
</p>

---

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
