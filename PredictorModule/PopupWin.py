import tkinter as tk
import tkinter.ttk
from . import Canvas

class PopupWin(object):
    def __init__(self, demographic_dict):
        self.demographic_dict = demographic_dict
        self.popup_win = tk.Toplevel()
        self.popup_win.config(bg="#C2F7FB")
        self.popup_win.title("Change Demographic")
        self.popup_win.geometry('350x100')
        self.popup_win.resizable(False, False)
        self.current_demographic = None
        popup_label = tk.Label(self.popup_win, text="Change Demographic", bg=self.popup_win['bg'])
        popup_label.grid(row=0, columnspan=2, padx=100)
        category_label = tk.Label(self.popup_win, text="Category:", bg=self.popup_win['bg'])
        category_label.grid(row=1, column=0)
        category_label = tk.Label(self.popup_win, text="Demographic:", bg=self.popup_win['bg'])
        category_label.grid(row=2, column=0)

        category_list = self.create_category_list()

        self.category_combo = tk.ttk.Combobox(self.popup_win, values=category_list, width=40)
        self.category_combo.current(0)
        self.category_combo.grid(row=1, column=1)
        self.category_combo.bind("<<ComboboxSelected>>", self.changeDemographicOptions)

        self.demographic_combo = tk.ttk.Combobox(self.popup_win, values=[], width=40)
        self.changeDemographicOptions()
        self.demographic_combo.current(0)
        self.demographic_combo.grid(row=2, column=1)
        self.demographic_combo.bind("<<ComboboxSelected>>", self.set_current_demographic)
        self.set_current_demographic()

        self.exit_button = tk.Button(self.popup_win, text="Done", command=self.exit)
        self.exit_button.grid(row=3, columnspan=2, pady=10)

    def set_current_demographic(self, event=None):
        demographicsInGroup = self.demographic_dict[list(self.demographic_dict.keys())[self.category_combo.current()]]
        self.current_demographic = demographicsInGroup[self.demographic_combo.current()]

    def exit(self, event=None):
        canvasObj = self.popup_win.master.winfo_children()[0].winfo_children()[0]
        Canvas.Canvas.current_demographic = self.current_demographic
        canvasObj.event_generate("<<DemographicSelected>>", when="now")
        self.popup_win.destroy()


    def create_category_list(self):
        categories = []
        for key in self.demographic_dict:
            categories.append(key)
        return categories

    def changeDemographicOptions(self, event=None):
        demographic_list = []
        for demographic in self.demographic_dict[list(self.demographic_dict.keys())[self.category_combo.current()]]:
            demographic_list.append(demographic.name)
        self.demographic_combo["values"] = demographic_list

        self.demographic_combo.current(0)