import qrcode
import datetime
import os

print("QR Code Generator")

# Input de dados 
data = input("Enter text or URL for QR code: ")

# Caminho para salvar o QR Code
repo_path = "./QR_Gerados" 

# Criar diretório caso não exista
if not os.path.exists(repo_path):
    os.makedirs(repo_path)

# Nome do arquivo com data e hora
filename = f"qrcode-{datetime.datetime.now().strftime('_%d_%m_%Y_')}.png" 
file_path = os.path.join(repo_path, filename)

# Gerar QR code
img = qrcode.make(data)  

# Salvar imagem no caminho 
img.save(file_path)  

print(f"QR code salvo em: {file_path}")