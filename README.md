# 🛡️ Cipher Master

**Cipher Master** é uma poderosa ferramenta de criptografia e descriptografia com interface gráfica moderna. Feito em Python com Tkinter, ele suporta múltiplos tipos de cifras — incluindo uma cifra secreta que **só o app pode decifrar**.

<p align="center">
  <img src="https://user-images.githubusercontent.com/0000000/banner.png" alt="Cipher Master Banner" width="600"/>
</p>

## 🔐 Funcionalidades

- ✅ **Cifra de César**
- ✅ **Hexadecimal**
- ✅ **Cipher Master Secret** (exclusiva e indecifrável sem o app!)
- ✅ **Modo Decifra** com brute force incluso
- ✅ Interface GUI com **tema hacker verde neon**
- ✅ Compatível com **Windows e Linux**
- ✅ **Compilado em `.exe`** via `pyinstaller` e `.py` para Linux e Mac

---

## 🖥️ Baixe Agora

| Sistema | Download |
|--------|----------|
| 🪟 Windows | [Clique aqui para baixar](https://github.com/K-K-Coder-debug/cipher-master/releases/tag/cipher-master/cypher-master-x64.exe) |
| 🐧 Linux | [Clique aqui para baixar](https://github.com/K-K-Coder-debug/cipher-master/releases/tag/cipher-master/cypher-master.py) |



---

## 🧠 Como Usar

1. Execute o app
2. Escolha entre `Cipher` ou `Decipher`
3. Selecione o método desejado
4. Insira o texto e veja a mágica acontecer!

---

## 🚀 Como Rodar o Cipher Master
### 🪟 Windows (.exe)
Baixe o executável da aba Releases.

Dê dois cliques em cipher_master.exe.

Pronto! A interface gráfica vai abrir.

#### ⚠️ O executável pode ser detectado como falso positivo por antivírus. Adicione uma exceção se necessário.

### 🐧 Linux e 🍎 macOS (via Python)
Pré-requisitos:
Python 3.7 ou superior instalado.

Tkinter (normalmente já vem com Python).

Passos:
```bash
git clone https://github.com/SEU_USUARIO/cipher-master.git
cd cipher-master
python3 cipher_master_gui.py
```
#### 💡 No macOS, se houver erro sobre display, use python3 -m tkinter para checar se o Tkinter está funcionando.

### ✅ Requisitos Python:
Se preferir instalar as dependências com pip, rode:
```bash
pip install -r requirements.txt
```
Obs: No momento, o Cipher Master só usa bibliotecas nativas do Python (sem dependências externas).
## 🧪 Build Manual

Para compilar:
Windows
```bash
# Instale dependências
pip install pyinstaller
# E ADICIONE O PATH NAS VARIAVEIS DE AMBIENTE

# Compile no Windows
pyinstaller --onefile cypher-master.py --noconsole --windowed
```
## Feito com 💚 por [K_KCoder](https://github.com/K-K-Coder-debug).
Você pode usar, modificar e distribuir livremente.
Se gostou, deixe uma ⭐ no projeto!
