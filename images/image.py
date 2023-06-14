from PIL import ImageDraw, Image, ImageFilter, ImageColor, ImageFont
import random

total = int(input('total quantity of pages '))
position = int(input('were are you now ? '))
bg_image_index = random.randint(0, 9)
colors = ['#1B9C85', '#1D267D', '#FFD95A', '#394867', '#F45050', '#B2A4FF', '#7149C6', '#AEC2B6', '#97DEFF', '#655DBB']
color = random.choice(colors)
min = 100
full_size = 450


class ProgressBar():

    #calculates percentage and progressbar currect position
    def calculation(self):
        index_raw = total / position
        index = round(index_raw, 2)
        final = full_size / index
        return 105 + float(round(final, 1))

    #changing resolution of the book_icon image
    def book_icon(self):
        image = Image.open('book_icon.png')
        resized = image.resize((100, 100))
        return resized

    def image_draw(self, len: int, icon):
        #loading and changing resolution and filters
        image = Image.open(f"{str(bg_image_index)}.png")
        resized_image = image.resize((640, 360))
        filtered_image = resized_image.filter(ImageFilter.MinFilter(size=3))

        #drawing new objects 
        draw = ImageDraw.Draw(filtered_image)

        draw.rounded_rectangle((70, 120, 550, 180), radius=20,
                               outline=ImageColor.getcolor(color, 'RGB'), 
                               width=2, fill=ImageColor.getcolor('#CDFCF6', 'RGB'))
        draw.rounded_rectangle((69, 120, len, 180),
                               fill=ImageColor.getcolor(color, 'RGB'), radius=25)
        
        #adding icon on the main image
        filtered_image.paste(icon, (0, 0), mask=icon)
    
        #font / percentage
        font1 = ImageFont.truetype("Invisible-ExtraBold.otf", 30)
        font2 = ImageFont.truetype('BOOKMARK-Bold-Italic.otf', 40)
        percentage = position / total * 100

        draw.text((250, 135), f'{position} / {total}', font=font1, fill='black')
        draw.text((555, 125), f'{round(percentage, 1)}%',font=font2, fill=ImageColor.getcolor(color, 'RGB'))

        filtered_image.save(r'path' + '.png')


progress = ProgressBar()

value = progress.calculation()
icon = progress.book_icon()
progress.image_draw(value, icon)