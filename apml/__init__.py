
import tkinter as tk
import os
import sys
import random

win = tk.Tk()

class example:
    class click:
        def btnCallback():
            global btnclicks,btn
            btnclicks+=1   
            btn.config(text=btnclicks)
        btnclicks = 0
        text = tk.Label(win,text="click the button")
        btn = tk.Button(win,text="click me!",command=btnCallback)
            
