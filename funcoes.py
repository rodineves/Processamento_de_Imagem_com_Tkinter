import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def compair(img_ori_pross, img_mine):
    if img_ori_pross.size != img_mine.size or img_ori_pross.mode != img_mine.mode:
        raise ValueError("As imagens não são do mesmo tamanho ou modo.")
    
    img_processada_do_usuario = np.array(img_ori_pross).astype(np.int16)  # Converter para int16
    img_processada_pelo_programa = np.array(img_mine).astype(np.int16)  # Converter para int16
    
    height, width = img_processada_do_usuario.shape[:2]
    
    m = img_processada_pelo_programa - img_processada_do_usuario
    for x in range(height):
        for y in range(width):
            m[x][y] = int(img_processada_pelo_programa[x][y]) - int(img_processada_do_usuario[x][y])
            #print(f"{img_processada_pelo_programa[x][y]} - {img_processada_do_usuario[x][y]} = {m[x][y]}")

    return m