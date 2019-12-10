import tkinter as tk
import PopupWin


class Window(object):
    policy_list = None
    demographic_list = None

    def __init__(self, demographic_list, policyList=None):
        Window.policy_list = policyList
        Window.demographic_list = demographic_list

        self.windowObj = tk.Tk()
        self.windowObj.title("First-Gen Graduation Rate Simulator")
        self.windowObj.iconbitmap("../project_logo.ico")
        self.frameObj = tk.Frame(self.windowObj)
        self.frameObj.configure(background="White", bd=0)
        self.frameObj.pack(fill="both", expand="yes")


        self.windowObj.state("zoomed")
        self.windowObj.geometry("800x500")
        self.fullScreenState = False
        self.windowObj.bind("<F11>", self.toggle_fullscreen)
        self.windowObj.bind("<Escape>", self.end_fullscreen)

        self.windowObj.bind("<<UpdateDemographic>>", self.create_popup)
        self.windowObj.bind("<<UpdateDemographic>>", self.create_popup)

    def create_popup(self, event=None):
        popup = PopupWin.PopupWin(self.generate_demographic_dict())


    def generate_demographic_dict(self):
        demographic_dict = dict()
        demographic_dict["all"] = []
        for demographic in self.demographic_list:
            if(demographic.category is not None):
                if(demographic.category not in demographic_dict.keys()):
                    demographic_dict[demographic.category] = []
                demographic_dict[demographic.category].append(demographic)
            if(demographic.category is not "all"):
                demographic_dict["all"].append(demographic)
        return demographic_dict


    def update(self, event=None):
        self.windowObj.update_idletasks()

    def toggle_fullscreen(self, event=None):
        self.fullScreenState = not self.fullScreenState
        self.windowObj.attributes("-fullscreen", self.fullScreenState)
        return "break"

    def end_fullscreen(self, event=None):
        self.fullScreenState = False
        self.windowObj.attributes("-fullscreen", False)
        return "break"

    def getSize(self):
        self.update()
        return [self.windowObj.winfo_width(), self.windowObj.winfo_height()]