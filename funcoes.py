import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def menu():
    print('Put a image in your past, and then choose a preprocesing selecting the number:')
    print('1 - Negative                | 12 - Low-pass (Median)')
    print('2 - Monochrome              | 13 - High-pass')
    print('3 - Binarization            | ')
    print('4 - Thresholding            | ')
    print('5 - Slicing                 | ')
    print('6 - Contrast Flare          | ')
    print('7 - Histogram               | ')
    print('8 - Histogram Equalization  | ')
    print('9 - Low-pass (Mean)        | ')
    op = int(input("Type a number: "))
    return op

def compair(img_ori_pross, img_mine):
    if img_ori_pross.size != img_mine.size or img_ori_pross.mode != img_mine.mode:
        raise ValueError("As imagens não são do mesmo tamanho ou modo.")
    
    l, c = img_ori_pross
    
    qtd_pxl = l*c
    
    img_ori_pross_array = np.array(img_ori_pross)
    img_mine_array = np.array(img_mine)
    
    num_equal_pixels = np.sum( img_ori_pross_array == img_mine_array)
    percentage_equal = (num_equal_pixels / qtd_pxl) * 100
    
    return percentage_equal



