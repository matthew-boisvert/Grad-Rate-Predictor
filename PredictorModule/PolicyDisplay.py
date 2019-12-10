import tkinter as tk
import SwitchButton

class PolicyDisplay(object):

    def __init__(self, master, policy_list, canvas):
        self.canvas = canvas
        self.policyFrame = tk.Frame(master)
        self.policyFrame.config(bg = "#ccf2ff", highlightthickness=1, highlightbackground="#B4B4B4")
        self.policyFrame.pack(side="bottom", fill="both")
        self.title = tk.Label(self.policyFrame, text="Policies", font=("Helvetica", 12))
        self.title.config(bg=self.title.master["bg"])
        self.title.pack(side="top")

        self.resetButton = tk.Button(self.policyFrame, text="Reset", command=self.resetSwitches)
        self.resetButton.pack(side="bottom", fill="both")

        self.policyFrame.bind("<<EnablePolicy>>", self.generate_event)
        self.policyButtons = []
        self.canvas.policies = policy_list
        for policy in policy_list:
            self.policyButtons.append(SwitchButton.SwitchButton(self.policyFrame, policy, self.canvas))

    def generate_event(self, event):
        self.canvas.event_generate("<<UpdateGraduationRate>>", when="now")

    def resetSwitches(self):
        for button in self.policyButtons:
            button.disable()