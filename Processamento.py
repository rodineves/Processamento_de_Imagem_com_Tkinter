from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

class Processamento:
    
    def __init__(self, img_ori):
        self.img = img_ori.convert("RGB")
    
    # Método de imprimir imagem
    def display_img(self, img): 
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5)) 
        ax1.imshow(np.array(self.img))
        ax1.axis('off')
        ax2.imshow(np.array(img))
        ax2.axis('off')
        plt.show()
    
    # Método de negativar imagem
    def negative(self):
        l, c = self.img.size
        inverted_img = Image.new("RGB", (l, c))

        for x in range(l):
            for y in range(c):
                pxl = self.img.getpixel((x, y))

                if isinstance(pxl, tuple):
                    inverted_pixel = tuple([255 - i for i in pxl])
                else:
                    inverted_pixel = 255 - pxl
                inverted_img.putpixel((x, y), inverted_pixel)
        inverted_img.save("imgs/gatenho_negativo.jpg")
        #self.display_img(inverted_img)
        return inverted_img
    
    # Método de tranforma imagem em monocromática
    def monochrome(self):
        l, c = self.img.size
        img_mono = Image.new("RGB", (l, c))

        for x in range(l):
            for y in range(c):
                pxl = self.img.getpixel((x, y))

                if isinstance(pxl, tuple):
                    media = (pxl[1] + pxl[2] + pxl[0]) // 3

                    img_mono.putpixel((x, y), (media, media, media))
                else:
                    img_mono.putpixel((x, y), (pxl, pxl, pxl))
        img_mono.save("imgs/gatenho_monocroma.jpg")
        #self.display_img(img_mono)
        return img_mono
    
    def binarization(self):
        l,c = self.img.size
        img_bi = Image.new("RGB", (l, c))
        
        for x in range(l):
            for y in range(c):
                pxl = self.img.getpixel((x, y))

                media = (pxl[1] + pxl[2] + pxl[0]) // 3

                if media < 128:
                    img_bi.putpixel((x, y), (0, 0, 0))
                else:
                    img_bi.putpixel((x, y), (255, 255, 255))
        img_bi.save("imgs/gatenho_binarizado.jpg")
        #self.display_img(img_bi)
        return img_bi
    
    def thresholding(self, pb, thresholds):
        l, c = pb.size
        img = Image.new("RGB", (l, c))
        qtd = len(thresholds)
        
        if qtd == 1:
            for x in range(l):
                for y in range(c):
                    pxl = pb.getpixel((x, y))

                    media = (pxl[1] + pxl[2] + pxl[0]) // 3

                    if media < thresholds[0]:
                        img.putpixel((x, y), (0, 0, 0))
                    else:
                        img.putpixel((x, y), (255, 255, 255))
        else:
            for x in range(l):
                for y in range(c):
                    pxl = pb.getpixel((x, y))

                    media = (pxl[0] + pxl[1] + pxl[2]) // 3

                    for i in range(qtd-1):
                        if media <= thresholds[0]:
                            img.putpixel((x, y), (0, 0, 0))

                        if media >= thresholds[qtd-1]:
                            img.putpixel((x, y), (255, 255, 255))
                        if thresholds[i] <= media < thresholds[i+1]:
                            img.putpixel((x, y), (thresholds[i], thresholds[i], thresholds[i]))
        img.save("imgs/gatenho_threshhold.jpg")
        #self.display_img(img)
        return img
    
    def calculate_difference(self, image1, image2):
        image1_np = np.array(image1)
        image2_np = np.array(image2)

        if image1_np.shape != image2_np.shape:
            raise ValueError("As imagens devem ter o mesmo tamanho e número de canais")

        diff_np = np.abs(image1_np - image2_np)
        diff_image = Image.fromarray(diff_np.astype('uint8'))
        return diff_image