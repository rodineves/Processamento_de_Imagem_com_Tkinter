import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def compair(img_ori_pross, img_mine):
    if img_ori_pross.size != img_mine.size or img_ori_pross.mode != img_mine.mode:
        raise ValueError("As imagens não são do mesmo tamanho ou modo.")
    
    l, c = img_ori_pross.size
    print(f"{l} e {c}")
    matrix = [[0 for _ in range(l)] for _ in range(c)]
    
    img_ori_pross = np.array(img_ori_pross)
    img_mine = np.array(img_mine)
    
    for x in range(l):
        for y in range(c):
            matrix[x][y] = img_ori_pross[x][y] - img_mine[x][y]
    #matrix =  img_ori_pross.astype(int) - img_mine.astype(int)
    return matrix
    
    



