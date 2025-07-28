import tkinter as tk
from tkinter import simpledialog, messagebox

# Cifra de César
def cifra_cesar(texto, deslocamento):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            resultado += chr((ord(letra) - base + deslocamento) % 26 + base)
        else:
            resultado += letra
    return resultado

# Decifra César
def decifra_cesar(texto, deslocamento):
    return cifra_cesar(texto, -deslocamento)

# Brute force para decifra César
def brute_force_cesar(texto):
    resultados = []
    for deslocamento in range(1, 26):
        decifrado = decifra_cesar(texto, deslocamento)
        resultados.append(f"Deslocamento {deslocamento}: {decifrado}")
    return "\n".join(resultados)

# Cifra hexadecimal
def cifra_hexadecimal(texto):
    return ' '.join(f"{ord(c):02x}" for c in texto)

# Decifra hexadecimal
def decifra_hexadecimal(hex_texto):
    try:
        return ''.join(chr(int(c, 16)) for c in hex_texto.split())
    except ValueError:
        return "Erro: entrada inválida."

# Cifra personalizada e secreta do Cipher Master
def cipher_master_custom(texto):
    resultado = ""
    for i, letra in enumerate(texto):
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            code = ((ord(letra) - base + i * 3) % 26)
            code = 25 - code  # inverte o alfabeto
            resultado += chr(code + base)
        else:
            resultado += chr(ord(letra) ^ (13 + i))
    resultado += chr(0x1F)
    return resultado

# Decifra personalizada do Cipher Master
def decipher_master_custom(texto):
    if not texto or ord(texto[-1]) != 0x1F:
        return "Erro: texto inválido ou não criptografado com Cipher Master Secret."

    texto = texto[:-1]  # remove o caractere final especial
    resultado = ""
    for i, letra in enumerate(texto):
        if letra.isalpha():
            base = ord('A') if letra.isupper() else ord('a')
            code = ord(letra) - base
            code = 25 - code
            resultado += chr((code - i * 3) % 26 + base)
        else:
            resultado += chr(ord(letra) ^ (13 + i))
    return resultado

# GUI principal
class CipherMasterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cipher Master")
        self.root.geometry("400x550")
        self.root.configure(bg="black")

        self.title = tk.Label(root, text="CIPHER MASTER", font=("Consolas", 20), fg="lime", bg="black")
        self.title.pack(pady=10)

        # Abas
        self.tab_frame = tk.Frame(root, bg="black")
        self.tab_frame.pack(pady=10)

        self.cipher_tab_btn = tk.Button(self.tab_frame, text="Cipher", command=self.show_cipher_menu,
                                        font=("Consolas", 10), fg="black", bg="lime", activebackground="green")
        self.cipher_tab_btn.grid(row=0, column=0, padx=5)

        self.decipher_tab_btn = tk.Button(self.tab_frame, text="Decipher", command=self.show_decipher_menu,
                                          font=("Consolas", 10), fg="black", bg="white", activebackground="green")
        self.decipher_tab_btn.grid(row=0, column=1, padx=5)

        self.menu_frame = tk.Frame(root, bg="black")
        self.menu_frame.pack(pady=10)

        self.quit_button = tk.Button(root, text="Exit", command=root.quit, font=("Consolas", 12),
                                     fg="lime", bg="black", activebackground="red", activeforeground="black")
        self.quit_button.pack(pady=20)

        self.show_cipher_menu()

    def clear_menu(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()

    def show_cipher_menu(self):
        self.clear_menu()

        self.mode1 = tk.Button(self.menu_frame, text="Caesar Cipher", command=self.encrypt_cesar,
                               font=("Consolas", 12), fg="lime", bg="black", activebackground="lime",
                               activeforeground="black")
        self.mode1.pack(pady=5)

        self.mode2 = tk.Button(self.menu_frame, text="Hexadecimal Cipher", command=self.encrypt_hex,
                               font=("Consolas", 12), fg="lime", bg="black", activebackground="lime",
                               activeforeground="black")
        self.mode2.pack(pady=5)

        self.mode3 = tk.Button(self.menu_frame, text="Cipher Master Secret", command=self.encrypt_custom,
                               font=("Consolas", 12), fg="lime", bg="black", activebackground="lime",
                               activeforeground="black")
        self.mode3.pack(pady=5)

    def show_decipher_menu(self):
        self.clear_menu()

        self.dec1 = tk.Button(self.menu_frame, text="Decipher Caesar", command=self.decrypt_cesar,
                              font=("Consolas", 12), fg="lime", bg="black", activebackground="lime",
                              activeforeground="black")
        self.dec1.pack(pady=5)

        self.dec2 = tk.Button(self.menu_frame, text="Decipher Hexadecimal", command=self.decrypt_hex,
                              font=("Consolas", 12), fg="lime", bg="black", activebackground="lime",
                              activeforeground="black")
        self.dec2.pack(pady=5)

        self.dec3 = tk.Button(self.menu_frame, text="Decipher Cipher Master Secret", command=self.decrypt_custom,
                              font=("Consolas", 12), fg="lime", bg="black", activebackground="lime",
                              activeforeground="black")
        self.dec3.pack(pady=5)

        self.dec4 = tk.Button(self.menu_frame, text="Brute Force Caesar", command=self.brute_force_cesar_gui,
                              font=("Consolas", 12), fg="lime", bg="black", activebackground="lime",
                              activeforeground="black")
        self.dec4.pack(pady=5)

    def encrypt_cesar(self):
        texto = simpledialog.askstring("Caesar Cipher", "Enter text to encrypt:", parent=self.root)
        deslocamento = simpledialog.askinteger("Caesar Cipher", "Enter displacement (0-25):", parent=self.root, minvalue=0, maxvalue=25)
        if texto is not None and deslocamento is not None:
            resultado = cifra_cesar(texto, deslocamento)
            messagebox.showinfo("Encrypted", f"Encrypted text:\n{resultado}")

    def encrypt_hex(self):
        texto = simpledialog.askstring("Hexadecimal Cipher", "Enter text to encrypt:", parent=self.root)
        if texto is not None:
            resultado = cifra_hexadecimal(texto)
            messagebox.showinfo("Encrypted", f"Encrypted text:\n{resultado}")

    def encrypt_custom(self):
        texto = simpledialog.askstring("Cipher Master Secret", "Enter secret text:", parent=self.root)
        if texto is not None:
            resultado = cipher_master_custom(texto)
            messagebox.showinfo("Encrypted", f"Encrypted text:\n{resultado}")

    def decrypt_cesar(self):
        texto = simpledialog.askstring("Decipher Caesar", "Enter text to decrypt:", parent=self.root)
        deslocamento = simpledialog.askinteger("Decipher Caesar", "Enter displacement (0-25):", parent=self.root, minvalue=0, maxvalue=25)
        if texto is not None and deslocamento is not None:
            resultado = decifra_cesar(texto, deslocamento)
            messagebox.showinfo("Decrypted", f"Decrypted text:\n{resultado}")

    def decrypt_hex(self):
        texto = simpledialog.askstring("Decipher Hexadecimal", "Enter hex text (e.g., 68 65 6c 6c 6f):", parent=self.root)
        if texto is not None:
            resultado = decifra_hexadecimal(texto)
            messagebox.showinfo("Decrypted", f"Decrypted text:\n{resultado}")

    def decrypt_custom(self):
        texto = simpledialog.askstring("Decipher Cipher Master Secret", "Enter encrypted text:", parent=self.root)
        if texto is not None:
            resultado = decipher_master_custom(texto)
            messagebox.showinfo("Decrypted", f"Decrypted text:\n{resultado}")

    def brute_force_cesar_gui(self):
        texto = simpledialog.askstring("Brute Force Caesar", "Enter text to brute force decrypt:", parent=self.root)
        if texto is not None:
            resultados = brute_force_cesar(texto)
            # Mostrar em uma janela de texto para facilitar a leitura
            top = tk.Toplevel(self.root)
            top.title("Brute Force Caesar Results")
            top.geometry("400x400")
            top.configure(bg="black")
            text_widget = tk.Text(top, wrap="word", bg="black", fg="lime", font=("Consolas", 12))
            text_widget.insert("1.0", resultados)
            text_widget.config(state="disabled")
            text_widget.pack(expand=True, fill="both")

# Inicialização do app
if __name__ == '__main__':
    root = tk.Tk()
    app = CipherMasterApp(root)
    root.mainloop()
