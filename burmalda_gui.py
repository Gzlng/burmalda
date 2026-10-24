import tkinter as tk
from tkinter import *
import random
from playsound3 import playsound

root = tk.Tk()



files = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png']
'''Вот тут надо решетку ставить, если не хочется бурмалдить до посинения'''
#files = ['1.png']



images = [tk.PhotoImage(file=f) for f in files]

random_image1 = random.choice(images)
random_image2 = random.choice(images)
random_image3 = random.choice(images)

if random_image1 == random_image2 and random_image2 == random_image3:
    playsound('pesenka.mp3', block=False)


label1 = tk.Label(root, image=random_image1)
label1.grid(row=0, column= 0)

label2 = tk.Label(root, image=random_image2)
label2.grid(row=0, column=1)

label3 = tk.Label(root, image=random_image3)
label3.grid(row=0, column=2)


root.mainloop()