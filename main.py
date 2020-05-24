import random
import os
from PIL import Image, ImageDraw, ImageFont


class Capthcha:
    interval_height_width = [10,70]
    save_name = 'i.png'
    aligin = 'center'
    green_min_max = [0,200]
    red_min_max = [0,200]
    blue_min_max = [0,200]
    alpha_min_max = [150,255]
    min_max_font_size = [70,75]
    width_height_img = [1125,125]
    background_color = 'white'
    mode = 'RGBA'
    text_length = 15
    fonts = []
    text = ''
    factor = 40
    fonts_folder = "fonts/"
    files = [
            'ARIAL.TTF',
            'CALIBRI.TTF',
            'CAMBRIA.TTC',
            'COMIC.TTF',
            'CONSOLA.TTF',
            'CONSTAN.TTF',
            'CORBEL.TTF',
            'GABRIOLA.TTF',
            'GARA.TTF',
            'LUCON.TTF',
            'MICROSS.TTF',
            'PALA.TTF',
            'TAHOMA.TTF',
            'TIMES.TTF',
            'TREBUC.TTF',
            'VERDANA.TTF',
    ]
    symvols = '1234567890abcdefhijklmnopqrstuywxyzABCDEFGHIJKLMNOPQRSTUYWXYZ!@#$%^&*()-=+[]~'
    def __init__(self):
        self.img = Image.new(self.mode, (self.width_height_img[0],self.width_height_img[1]), self.background_color)
        self.draw = ImageDraw.Draw(self.img)
        self.width = self.img.size[0]
        self.height = self.img.size[1]  #Определяем высоту.
        self.pix = self.img.load()  #Выгружаем значения пикселей.
        self.Generate_Random_Text()
        self.InitFonts()
        self.CreateCaptchaImangie()
    def Generate_Random_Text(self):
        i = 0
        result = ''
        while i < self.text_length:
            result = result + self.symvols[random.randint(0,len(self.symvols)) - 1]
            i = i + 1
        self.text = result

    def InitFonts(self):
        r = []
        i = 0
        for item in self.files:
            r.append(
                ImageFont.truetype(
                    font=os.path.abspath("".join([self.fonts_folder,item])), size=random.randint(self.min_max_font_size[0],self.min_max_font_size[1])))
            i = i + 1
        self.fonts = r

    def CreateCaptchaImangie(self):
        i = 0
        while i < len(self.text):
            self.draw.text((self.interval_height_width[1] * (i + 1), self.interval_height_width[0]),
                       self.text[i],
                       font=self.fonts[random.randint(0,len(self.fonts) - 1)],
                       fill=(random.randint(self.red_min_max[0],self.red_min_max[1]), random.randint(self.green_min_max[0],self.green_min_max[1]),
                             random.randint(self.blue_min_max[0],self.blue_min_max[1]), random.randint(self.alpha_min_max[0],self.alpha_min_max[1])),
                       align=self.aligin)
            i = i + 1
        self.Generate_Salt()
        self.img.save(self.save_name)

    def Generate_Salt(self):
        for i in range(self.width):
            for j in range(self.height):
                rand = random.randint(self.factor - self.factor * 2, self.factor)
                a = self.pix[i, j][0] + rand
                b = self.pix[i, j][1] + rand
                c = self.pix[i, j][2] + rand
                if (a < 0):
                    a = 0
                if (b < 0):
                    b = 0
                if (c < 0):
                    c = 0
                if (a > 255):
                    a = 255
                if (b > 255):
                    b = 255
                if (c > 255):
                    c = 255
                self.draw.point((i, j), (a, b, c))
        self.Add_Lines()

    def Add_Lines(self):
        print('')
c = Capthcha()
