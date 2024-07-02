from Processamento import Processamento
from funcoes import *

import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk

def open_image():
    # Abre o diálogo para selecionar o arquivo de imagem
    filepath = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if not filepath:
        return
    
    # Abre a imagem usando Pillow
    img = Image.open(filepath)
    img.thumbnail((400, 400))  # Redimensiona a imagem se necessário
    
    # Converte a imagem para um formato compatível com Tkinter
    img_tk = ImageTk.PhotoImage(img)
    
    # Atualiza o widget Label para mostrar a nova imagem
    image_label.config(image=img_tk)
    image_label.image = img_tk  # Necessário para evitar que a imagem seja coletada pelo garbage collector
    

#op = menu()

# Cria a janela principal
root = tk.Tk()
root.title("Visualizador de Imagens")

# Criando a lista de processamento
processamentos = ["negative", "binarizetion", "monochrome"]



# Define o tamanho inicial da janela
root.geometry("600x400")

# Cria um botão para abrir o diálogo de seleção de imagem 
open_button = tk.Button(root, text="Abrir Imagem", command=open_image)
open_button.pack(pady=10)

# Cria um Label para exibir a imagem
image_label = tk.Label(root)
image_label.pack()

# Inicia o loop principal da interface
root.mainloop()



# img_processor = Processamento("imgs/gatenho.jpg")
# #inverted_img = img_processor.negative()
# if op == 1:
#     inverted_img = img_processor.negative()
# elif op == 2:
#     monochrome_img = img_processor.monochrome()
# elif op == 3:
#     bi_img = img_processor.binarization()
# elif op == 4:
#     monochrome_img = img_processor.monochrome()
#     thresholds = [85, 170]
#     th_img = img_processor.thresholding(monochrome_img, thresholds)




