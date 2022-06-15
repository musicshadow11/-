#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import numpy as np
from goldSearch import *

def F(upper_cross_width):
    motor_mass = text_motor_mass.get('1.0', 'end')
    upper_cross_length = text_upper_cross_length.get('1.0', 'end')
    motor_mass = float(motor_mass.replace(" ", "").replace("\n", ""))
    upper_cross_length = float(upper_cross_length.replace(" ", "").replace("\n", ""))
    #print(motor_mass)
    #print(upper_cross_length)
    
    lam = 100.0 # multiplier
    p = (min(0.0, upper_cross_width))**2 # penalty function
    g = 9.8
    f1 = (upper_cross_width-5)**5 + (upper_cross_width-15)**3 + motor_mass*g*(upper_cross_width-25) + 750 # example functions
    f2 = (upper_cross_width-10)**4 - 0.05*upper_cross_length*(upper_cross_width-20)**2 + 250
    f_all = f1 + f2
    return f_all + lam * p

def calculate():
    motor_mass = text_motor_mass.get('1.0', 'end')
    upper_cross_length = text_upper_cross_length.get('1.0', 'end')
    motor_mass = float(motor_mass.replace(" ", "").replace("\n", ""))
    upper_cross_length = float(upper_cross_length.replace(" ", "").replace("\n", ""))
    #print(motor_mass)
    #print(upper_cross_length)
    
    x1, x2 = bracket(F, 1.0, 0.01)
    upper_cross_width, FMin = search(F, x1, x2)
    upper_cross_volume = (2*upper_cross_length-upper_cross_width)*upper_cross_width**2
    
    output_upper_cross_width = "The minimum width of the upper cross is " + str(upper_cross_width) + " (cm)"
    label_output_upper_cross_width.config(text = output_upper_cross_width)
    
    output_upper_cross_volume = "The minimum volume of the upper cross is " + str(upper_cross_volume) + " (cm^2)"
    label_output_upper_cross_volume.config(text = output_upper_cross_volume)
    
win = tk.Tk()
win.title('發酵桶配件尺寸搭配系統')
win.geometry('600x330')

label_motor_mass = tk.Label(win, text = 'The mass of motor is :                       (kg)', font = ('Arial', 12))
label_motor_mass.place(x = 12, y = 10)

var_motor_mass = tk.StringVar()
text_motor_mass = tk.Text(win, width = 11, height = 1)
text_motor_mass.place(x = 176, y = 14)

label_upper_cross_length = tk.Label(win, text = 'The length of the upper-cross is :                       (cm)', font = ('Arial', 12))
label_upper_cross_length.place(x = 12, y = 36)

text_upper_cross_length = tk.Text(win, width = 11, height = 1)
text_upper_cross_length.place(x = 248, y = 40)

button = tk.Button(win, text = "Calculate", font = ('Arial', 12), height = 2, width = 63, command = calculate)
button.place(x = 12, y = 72)

label_output_upper_cross_width = tk.Label(win, text = '', font = ('Arial', 12))
label_output_upper_cross_width.place(x = 12, y = 132)

label_output_upper_cross_volume = tk.Label(win, text = '', font = ('Arial', 12))
label_output_upper_cross_volume.place(x = 12, y = 158)

win.mainloop()

