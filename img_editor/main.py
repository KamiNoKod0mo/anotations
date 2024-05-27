import customtkinter as ctk
from image_widget import *
from PIL import Image, ImageTk, ImageOps,ImageEnhance, ImageFilter
from menu import Menu

FLIP_OPTIONS = ['None','X','Y','Both']
EFFECT_OPTIONS = ['None','Emboss','Find edges', 'Contour', 'Edge enhance']
class App(ctk.CTk):
    def __init__(self):

        #setup
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('1000x600')
        self.title('Photo Editor')
        self.minsize(800,500)

        #layout
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=2,uniform='a')
        self.columnconfigure(1,weight=6,uniform='a')

        #canvas
        self.image_width=0
        self.image_height=0
        self.canvas_width = 0
        self.canvas_height =0

        #widgets
        self.image_import = ImageImport(self,self.import_image)
        
        self.init_parameters()
        #run
        self.mainloop()

    def init_parameters(self):
        self.pos_vars = {
            'rotate': ctk.DoubleVar(value= 0),
            'zoom':  ctk.DoubleVar(value= 0),
            'flip': ctk.StringVar(value=FLIP_OPTIONS[0])
        }
        self.color_vars = {
            'brightness':ctk.DoubleVar(value=1),
            'grayscale':ctk.BooleanVar(value=False),
            'invert': ctk.BooleanVar(value=False),
            'vibrance':ctk.DoubleVar(value=1)
        }

        self.effect_vars = {
            'blur':ctk.DoubleVar(value=0),
            'contrast':ctk.IntVar(value=0),
            'effect': ctk.StringVar(value=EFFECT_OPTIONS[0]),
        }



        #self.rotatefloat = ctk.DoubleVar(value= 0)
        #self.zoom_float = ctk.DoubleVar(value= 0)
        # trcing
        combined_vars = list(self.pos_vars.values()) + list(self.color_vars.values()) + list(self.effect_vars.values())
        for var in combined_vars:
            var.trace('w',self.manipulate_image)
        
        #self.rotatefloat.trace('w',self.manipulate_image)
        #self.zoom_float.trace('w',self.manipulate_image)

    def manipulate_image(self,*args):
        self.image = self.original
        #rotate
        if self.pos_vars['rotate'].get() != 0:
            self.image = self.image.rotate(self.pos_vars['rotate'].get())
        #zoom
        if self.pos_vars['zoom'].get():
            self.image = ImageOps.crop(image= self.image, border=self.pos_vars['zoom'].get())


        #flip 
        if self.pos_vars['flip'].get() != FLIP_OPTIONS[0]:
            if self.pos_vars['flip'].get() == 'X':
                self.image = ImageOps.mirror(self.image)
            if self.pos_vars['flip'].get() == 'Y':
                self.image = ImageOps.flip(self.image)
            if self.pos_vars['flip'].get() == 'Both':
                self.image = ImageOps.mirror(self.image)
                self.image = ImageOps.flip(self.image)

        # brightness e vibrance
        if self.color_vars['brightness'].get() != 1:
            brightness_enchancer = ImageEnhance.Brightness(self.image)
            self.image = brightness_enchancer.enhance(self.color_vars['brightness'].get())
        if self.color_vars['brightness'].get() != 1:
            vibrance_enhancer = ImageEnhance.Color(self.image)
            self.image = vibrance_enhancer.enhance(self.color_vars['vibrance'].get())

        #grayscale and invert of the colors
    
        if self.color_vars['grayscale'].get():
            self.image = ImageOps.grayscale(self.image)

        if self.color_vars['invert'].get():
            self.image = ImageOps.invert(self.image)

        #blur and contrast
        if self.effect_vars['blur'].get() != 0:
            self.image = self.image.filter(ImageFilter.GaussianBlur(self.effect_vars['blur'].get()))
        if self.effect_vars['contrast'].get() != 0:
            self.image = self.image.filter(ImageFilter.UnsharpMask(self.effect_vars['contrast'].get()))

        match self.effect_vars['effect'].get():
            case 'Emboss': self.image = self.image.filter(ImageFilter.EMBOSS)
            case 'Find Edges': self.image = self.image.filter(ImageFilter.FIND_EDGES)
            case 'Contour': self.image = self.image.filter(ImageFilter.CONTOUR)
            case 'Edge enhance': self.image = self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)
            

        self.place_image()


    def import_image(self,path):
        self.original = Image.open(path)
        self.image = self.original
        self.image_ratio = self.image.size[0] / self.image.size[1]
        self.image_tk = ImageTk.PhotoImage(self.image)
        self.image_import.grid_forget()
        
        self.image_output = ImageOutput(self,self.resize_image)
        self.close_button = CloseOutput(self,self.close_edit)

        self.menu = Menu(self,self.pos_vars,self.color_vars,self.effect_vars,self.export_image)

    
    def close_edit(self):
        self.image_output.grid_forget()
        self.close_button.place_forget()
        self.menu.grid_forget()
        self.image_import = ImageImport(self,self.import_image)


    def resize_image(self,event):
        #resize
        canvas_ratio = event.width / event.height
        self.canvas_width = event.width 
        self.canvas_height = event.height 
        
        if canvas_ratio > self.image_ratio:
            self.image_height = int(event.height())
            self.image_width = int(self.image_height * self.image_ratio)
        else:
            self.image_width = int(event.width)
            self.image_height = int(self.image_width/ self.image_ratio)

        self.place_image()

    def place_image(self):
        #place image
        self.image_output.delete('all')
        resized_image = self.image.resize((self.image_width,self.image_height))
        self.image_tk = ImageTk.PhotoImage(resized_image)
        self.image_output.create_image(self.canvas_width / 2,self.canvas_height / 2,image = self.image_tk)

    def export_image(self,name,file,path):
        export_string = f'{path}/{name}.{file}'
        self.image.save(export_string)


App()