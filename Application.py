from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from Processamento import Processamento

root = Tk()

class Application:
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_1()
        self.create_widgets_frame_2()
        self.image = None
        root.mainloop()
    
    def tela(self):
        self.root.title("Verificação de Processamento de Imagem")
        self.root.configure(background="#1e3743")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
    def frames_da_tela(self):
        self.frame1 = Frame(self.root)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.5)
        
        self.frame2 = Frame(self.root)
        self.frame2.place(relx=0.02, rely=0.55, relwidth=0.96, relheight=0.5)
        
    def widgets_frame_1(self):
        # Dropdown Menu para seleção de tipo de processamento
        self.TipVar = StringVar(self.frame1)
        self.TipV = ("Negative", "Binarization", "Monochrome")
        self.TipVar.set("Negative")
        self.popup_menu = OptionMenu(self.frame1, self.TipVar, *self.TipV)
        self.popup_menu.place(relx=0.4, rely=0.75, relwidth=0.2, relheight=0.075)
        
        # Botão para selecionar imagem original
        self.select_image_button = Button(
            self.frame1, text="Selecionar Imagem", command=self.select_image
        )
        self.select_image_button.place(relx=0.1, rely=0.09, relwidth=0.2, relheight=0.075)

        # Label da Imagem Origininal
        self.image_label = Label(self.frame1, image=None)
        self.image_label.place(relx=0.0, rely=0.19, relwidth=0.45, relheight=0.45)
        
        # Botão para selecionar imagem Processada Originial
        self.select_image_button2 = Button(
            self.frame1, text="Selecionar Imagem", command=self.select_image2
        )
        self.select_image_button2.place(relx=0.7, rely=0.09, relwidth=0.2, relheight=0.075)

        # Label da Imagem Processada Original
        self.image_label2 = Label(self.frame1, image=None)
        self.image_label2.place(relx=0.55, rely=0.19, relwidth=0.45, relheight=0.45)
        
        # Botão OK
        self.ok_button = Button(
            self.frame1, text="OK", command=self.process_image
        )
        self.ok_button.place(relx=0.5, rely=0.9, relwidth=0.1, relheight=0.075, anchor=CENTER)
    
    def create_widgets_frame_2(self):
        
        # Label para exibir a imagem processada
        self.processed_image_label = Label(self.frame2, image=None)
        self.processed_image_label.place(relx=0.0, rely=0.19, relwidth=0.45, relheight=0.45)
    
    def select_image(self):
        # Abre para selecionar arquivo
        file_path = filedialog.askopenfilename(
            title="Selecionar Imagem", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )

        if file_path:
            self.image = Image.open(file_path)  # Lê a imagem selecionada
            resized_image = self.resize_image(self.image, self.image_label.winfo_width(), self.image_label.winfo_height())  # Redimensiona imagem para caber no Label
            image_tk = ImageTk.PhotoImage(resized_image)  # Converte para ser no formato Tkinter

            # Atualiza o label da imagem 2 inseirindo a imagem processada pelo programa
            self.image_label.config(image=image_tk)
            self.image_label.image = image_tk 
            
    def select_image2(self):
        # Abre para selecionar arquivo
        file_path = filedialog.askopenfilename(
            title="Sua IMG Processada", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )

        if file_path:
            self.image2 = Image.open(file_path)  # Lê a imagem selecionada
            resized_image2 = self.resize_image(self.image2, self.image_label.winfo_width(), self.image_label.winfo_height())  # Redimensiona imagem para caber no Label
            image_tk2 = ImageTk.PhotoImage(resized_image2)  # Converte para ser no formato Tkinter

            # Atualiza label 2 para a imagem processada
            self.image_label2.config(image=image_tk2)
            self.image_label2.image = image_tk2  # Padrão

    def resize_image(self, image, max_width, max_height):
        
        # Redimencionar imagem
        image_width, image_height = image.size
        ratio = min(max_width / image_width, max_height / image_height)
        new_width = int(image_width * ratio)
        new_height = int(image_height * ratio)
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        return resized_image

    def process_image(self):
        if self.image:
            selected_type = self.TipVar.get()
            processamento = Processamento(self.image)

            if selected_type == "Negative":
                processed_image = processamento.negative()
            elif selected_type == "Binarization":
                processed_image = processamento.binarization()
            elif selected_type == "Monochrome":
                processed_image = processamento.monochrome()

            resized_processed_image = self.resize_image(processed_image, self.image_label.winfo_width(), self.image_label.winfo_height())
            processed_image_tk = ImageTk.PhotoImage(resized_processed_image)
            self.processed_image_label.config(image=processed_image_tk)
            self.processed_image_label.image = processed_image_tk
            self.root.update_idletasks()  # Atualiza a interface na hora
            
            # diff_image = processamento.calculate_difference(self.image, processed_image)
            # resized_diff_image = self.resize_image(diff_image, self.processed_image_label.winfo_width(), self.processed_image_label.winfo_height())
            # diff_image_tk = ImageTk.PhotoImage(resized_diff_image)
            # self.processed_image_label.config(image=diff_image_tk)
            # self.processed_image_label.image = diff_image_tk

            # self.root.update_idletasks()

Application()
