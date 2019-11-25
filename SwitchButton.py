import tkinter as tk
from venv import *

class SwitchButton(object):
    def __init__(self, master, policy, canvas):
        self.policy = policy
        self.canvas = canvas
        self.button = tk.Button(master, text=policy.name, command=self.switch)
        self.button.pack(side="left", fill="both", expand="yes")
        self.state = 0

    def disable(self):
        self.state = False
        self.policy.disable()
        self.button.master.event_generate("<<EnablePolicy>>", when="now")
        self.redraw()

    def switch(self):
        #print("Generating <<EnablePolicy>> event")
        self.state = not self.state
        self.policy.changeState()
        self.button.master.event_generate("<<EnablePolicy>>", when="now")

        self.redraw()

    def redraw(self):
        if(self.state == 0):
            self.button.config(bg="#e6e6e6")
        else:
            self.button.config(bg="#b3b3b3")