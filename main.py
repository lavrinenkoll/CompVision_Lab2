import math
import numpy as np
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt


#read image from path
def read_image(path):
    image = Image.open(path)
    pixels = image.load()
    width, height = image.size
    draw = ImageDraw.Draw(image)
    return image, pixels, width, height, draw


#draw image from pixels
def draw_image(image, pixels, width, height, draw, title):
    for i in range(width):
        for j in range(height):
            draw.point((i, j), (pixels[i, j][0], pixels[i, j][1], pixels[i, j][2]))
    plt.title(title)
    plt.imshow(image)
    plt.show()


#change brightness
def change_brightness(path):
    # read image
    image, pixels, width, height, draw = read_image(path)
    # get brightness
    brightness = int(input("Введіть бажану яскравість: "))

    for i in range(width):
        for j in range(height):
            #add brightness
            r = pixels[i, j][0] + brightness
            g = pixels[i, j][1] + brightness
            b = pixels[i, j][2] + brightness
            #check for overflow
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            #set new pixel
            draw.point((i, j), (r, g, b))

    #draw image
    draw_image(image, pixels, width, height, draw, "Зміна яскравості на " + str(brightness))
    return image, pixels, width, height, draw


#shades of gray
def shades_of_gray(path):
    # read image
    image, pixels, width, height, draw = read_image(path)

    for i in range(width):
        for j in range(height):
            r = pixels[i, j][0]
            g = pixels[i, j][1]
            b = pixels[i, j][2]
            #get average
            sr = (r + g + b) // 3
            #set new pixel
            draw.point((i, j), (sr, sr, sr))

    #draw image
    draw_image(image, pixels, width, height, draw, "Відтінки сірого")
    return image, pixels, width, height, draw


#negative
def negative(path):
    # read image
    image, pixels, width, height, draw = read_image(path)

    for i in range(width):
        for j in range(height):
            #get negative color
            r = 255 - pixels[i, j][0]
            g = 255 - pixels[i, j][1]
            b = 255 - pixels[i, j][2]
            #set new pixel
            draw.point((i, j), (r, g, b))

    #draw image
    draw_image(image, pixels, width, height, draw, "Негатив")
    return image, pixels, width, height, draw


#serpia diagonal
def serpia_diagonal(path):
    # read image
    image, pixels, width, height, draw = read_image(path)
    #get depth
    depth = int(input("Введіть коефіцієнт серпії (по діагоналі): "))

    #create gradient diagonal
    gradient = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            #get koeff of pozition
            x = (i+1)/width
            y = (j+1)/height
            #calculate gradient
            gradient[i, j] = math.fabs(0.5 - x + 0.5 - y)

    for i in range(width):
        for j in range(height):
            r = pixels[i, j][0]
            g = pixels[i, j][1]
            b = pixels[i, j][2]
            #get average
            S = (r + g + b) // 3
            #calculate new color
            sr1 = round(S + depth*(1-gradient[i,j]) * 2)
            sr2 = round(S + depth*(1-gradient[i,j]))
            sr3 = S
            #check for overflow
            if sr1 > 255:
                sr1 = 255
            if sr2 > 255:
                sr2 = 255
            if sr3 > 255:
                sr3 = 255
            #set new pixel
            draw.point((i, j), (sr1, sr2, sr3))

    #draw image
    draw_image(image, pixels, width, height, draw, "Серпія по діагоналі, коефіцієнт "+str(depth))
    return image, pixels, width, height, draw


#serpia to center
def serpia_to_center(path):
    # read image
    image, pixels, width, height, draw = read_image(path)
    #get depth
    depth = int(input("Введіть коефіцієнт серпії (до центра): "))

    # create gradient to center
    gradient = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            #get koeff of pozition
            x = (i + 1) / width
            y = (j + 1) / height
            #calculate gradient
            gradient[i, j] = math.sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2)

    for i in range(width):
        for j in range(height):
            r = pixels[i, j][0]
            g = pixels[i, j][1]
            b = pixels[i, j][2]
            #get average
            S = (r + g + b) // 3
            #calculate new color
            sr1 = round(S + depth * (1 - gradient[i, j]) * 2)
            sr2 = round(S + depth * (1 - gradient[i, j]))
            sr3 = S
            #check for overflow
            if sr1 > 255:
                sr1 = 255
            if sr2 > 255:
                sr2 = 255
            if sr3 > 255:
                sr3 = 255
            #set new pixel
            draw.point((i, j), (sr1, sr2, sr3))

    #draw image
    draw_image(image, pixels, width, height, draw, "Серпія до центру, коефіцієнт "+str(depth))
    return image, pixels, width, height, draw


#serpia from center
def serpia_from_center(path):
    # read image
    image, pixels, width, height, draw = read_image(path)
    #get depth
    depth = int(input("Введіть коефіцієнт серпії (від центру): "))

    # create gradient from center
    gradient = np.zeros((width, height))
    for i in range(width):
        for j in range(height):
            #get koeff of pozition
            x = (i + 1) / width
            y = (j + 1) / height
            #calculate gradient
            gradient[i, j] = math.sqrt((x - 0.5) ** 2 + (y - 0.5) ** 2)

    for i in range(width):
        for j in range(height):
            r = pixels[i, j][0]
            g = pixels[i, j][1]
            b = pixels[i, j][2]
            #get average
            S = (r + g + b) // 3
            #calculate new color
            sr1 = round(S + depth * (gradient[i, j]) * 2)
            sr2 = round(S + depth * (gradient[i, j]))
            sr3 = S
            #check for overflow
            if sr1 > 255:
                sr1 = 255
            if sr2 > 255:
                sr2 = 255
            if sr3 > 255:
                sr3 = 255
            #set new pixel
            draw.point((i, j), (sr1, sr2, sr3))

    #draw image
    draw_image(image, pixels, width, height, draw, "Серпія від центру, коефіцієнт "+str(depth))
    return image, pixels, width, height, draw


#main
img_path = "img.png"
image, pixels, width, height, draw = read_image(img_path)
draw_image(image, pixels, width, height, draw, "Оригінал")

change_brightness(img_path)
shades_of_gray(img_path)
negative(img_path)
serpia_diagonal(img_path)
serpia_from_center(img_path)
serpia_to_center(img_path)
