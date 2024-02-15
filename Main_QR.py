import qrcode
import datetime
import os

print("QR Code Generator")

# Input de dados 
data = input("Enter text or URL for QR code: ")

# Caminho para salvar o QR Code
repo_path = "/users/Ygor-Silva/Documents/GitHub/Gerador_QRCode" 

# Criar diretório caso não exista
if not os.path.exists(repo_path):
    os.makedirs(repo_path)

# Nome do arquivo com data e hora
filename = f"qrcode-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.png" 
file_path = os.path.join(repo_path, filename)

# Gerar QR code
img = qrcode.make(data)  

# Salvar imagem no caminho 
img.save(file_path)  

print(f"QR code salvo em: {file_path}")