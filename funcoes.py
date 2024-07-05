import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def compair(img_ori_pross, img_mine):
    if img_ori_pross.size != img_mine.size or img_ori_pross.mode != img_mine.mode:
        raise ValueError("As imagens não são do mesmo tamanho ou modo.")
    
    img_processada_do_usuario = np.array(img_ori_pross)
    img_processada_pelo_programa = np.array(img_mine)
    
    m = img_processada_pelo_programa - img_processada_do_usuario
    #print(m)

    return m
    
    



