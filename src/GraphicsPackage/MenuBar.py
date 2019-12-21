import tkinter as tk

class MenuBar(object):
    def __init__(self, master):
        self.menuObj = tk.Menu(master)
        self.menuObj.config(bg=self.menuObj.master['bg'])
        self.fileMenuItem = tk.Menu(self.menuObj, tearoff=0)
        self.fileMenuItem.add_command(label='Exit', command=master.quit)

        self.demographicMenuItem = tk.Menu(master, tearoff=0)

        self.menuObj.add_cascade(label='File', menu=self.fileMenuItem)
        self.menuObj.add_command(label="Change Demographic", command=self.updateDemographic)
        self.menuObj.add_command(label="Verbose Mode", command=self.changeMode)

    def updateDemographic(self):
        self.menuObj.master.event_generate("<<UpdateDemographic>>", when="now")

    def changeMode(self):
        canvasObj = self.menuObj.master.winfo_children()[0]
        canvasObj.event_generate("<<SwitchMode>>", when="now")
