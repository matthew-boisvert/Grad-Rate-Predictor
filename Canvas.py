import tkinter as tk
import Window

class Canvas(object):
    current_demographic = None

    def __init__(self, master, current_dem):
        self.canvasObj = tk.Canvas(master)
        self.canvasObj.config(bg="White", bd=0, highlightthickness=1, highlightbackground="#B4B4B4")
        self.canvasObj.pack(side="top", fill="both", expand="yes")
        self.titleText = tk.StringVar()
        self.title = tk.Label(self.canvasObj, textvariable=self.titleText, font=("Helvetica", 16))
        self.title.config(bg=self.title.master['bg'])

        self.changeDemographic(current_dem)

        self.title.place(relx=.5, rely=.02, anchor="n")
        self.prediction_line = self.canvasObj.create_rectangle(0, 0, 0, 0, fill="Black")
        self.base_line = self.canvasObj.create_rectangle(0, 0, 0, 0, fill="Black")
        self.dropped_out_group = self.canvasObj.create_rectangle(0, 0, 0, 0, fill="#ffb3b3")
        self.graduated_group = self.canvasObj.create_rectangle(0, 0, 0, 0, fill="#ccffcc")

        self.button_frame = tk.Frame(self.canvasObj)
        self.button_frame.place(relx=0.90, rely=0.03, anchor="n")
        self.next_button = tk.Button(self.button_frame, text="→", command=self.next_demographic)
        self.next_button["font"] = ("Helvetica, 10")
        self.prev_button = tk.Button(self.button_frame, text="←", command=self.prev_demographic)
        self.prev_button["font"] = ("Helvetica, 10")
        self.cycleLabel = tk.Label(self.button_frame, text="Cycle Demographics", bg = "White")

        self.prev_button.pack(side="left")
        self.cycleLabel.pack(side="left")
        self.next_button.pack(side="left")

        self.grad_rate_text = self.canvasObj.create_text(0, 0, font=("Helvetica", 12, "bold"), text="Current Graduation Rate")
        self.old_rate_text = self.canvasObj.create_text(0, 0, font=("Helvetica", 12), text="Base Graduation Rate")
        self.graduated_text = self.canvasObj.create_text(0, 0, font=("Helvetica", 12, "bold"), text="Graduated", anchor="w", fill="#008000")
        self.dropped_out_text = self.canvasObj.create_text(0, 0, font=("Helvetica", 12, "bold"), text="Did Not Graduate", anchor="w", fill="#cc0000")

        self.canvasObj.bind("<Configure>", self.resize)
        self.canvasObj.bind("<<EnablePolicy>>", self.update_grad_rate)
        self.canvasObj.bind("<<UpdateGraduationRate>>", self.update_grad_rate)
        self.canvasObj.bind("<<DemographicSelected>>", self.update_to_selection)

    def update_to_selection(self, event):
        print(Canvas.current_demographic.name)
        self.set_demographic(Canvas.current_demographic)

    def set_demographic(self, demographic):
        self.changeDemographic(demographic)
        self.update_grad_rate()

    def next_demographic(self):
        current_category = Canvas.current_demographic.category
        current_index = Window.Window.demographic_list.index(Canvas.current_demographic)
        next_demographic_found = False
        while(not next_demographic_found):
            if(current_index == len(Window.Window.demographic_list)-1):
                current_index = 0
            else:
                current_index = current_index+1
            if(current_category == "all" or Window.Window.demographic_list[current_index].category == current_category):
                self.changeDemographic(Window.Window.demographic_list[current_index])
                next_demographic_found = True

        self.update_grad_rate()

    def prev_demographic(self):
        current_category = Canvas.current_demographic.category
        current_index = Window.Window.demographic_list.index(Canvas.current_demographic)
        next_demographic_found = False
        while(not next_demographic_found):
            if(current_index == 0):
                current_index = len(Window.Window.demographic_list)-1
            else:
                current_index = current_index-1
            if(current_category == "all" or Window.Window.demographic_list[current_index].category == current_category):
                self.changeDemographic(Window.Window.demographic_list[current_index])
                next_demographic_found = True
        self.update_grad_rate()


    def draw_prediction_line(self, canvas_size):
        left = 0
        bottom = canvas_size[1]*(1-Canvas.current_demographic.current_graduation_rate) - canvas_size[1]/100
        right = canvas_size[0]
        top = canvas_size[1]*(1-Canvas.current_demographic.current_graduation_rate)

        self.canvasObj.coords(self.dropped_out_group, left, top*.99, right, 0)
        self.canvasObj.coords(self.graduated_group, left, canvas_size[1], right, top)
        self.canvasObj.coords(self.prediction_line, left, bottom, right, top)

        self.canvasObj.coords(self.grad_rate_text, canvas_size[0]/2, top-canvas_size[1]/50)
        self.canvasObj.coords(self.graduated_text, canvas_size[0]/100, bottom+canvas_size[1]/30)
        self.canvasObj.coords(self.dropped_out_text, canvas_size[0]/100, canvas_size[1]/30)

        if(abs(Canvas.current_demographic.current_graduation_rate - Canvas.current_demographic.base_graduation_rate) < 0.01):
            self.canvasObj.itemconfig(self.base_line, state="hidden")
            self.canvasObj.itemconfig(self.old_rate_text, state="hidden")
            self.draw_base_line([self.canvasObj.winfo_width(), self.canvasObj.winfo_height()])
        else:
            self.canvasObj.tag_raise(self.base_line)
            self.canvasObj.itemconfig(self.base_line, state="normal")
            self.canvasObj.itemconfig(self.old_rate_text, state="normal")
            self.draw_base_line([self.canvasObj.winfo_width(), self.canvasObj.winfo_height()])

    def draw_base_line(self, canvas_size):
        left = 0
        bottom = canvas_size[1]*(1-Canvas.current_demographic.base_graduation_rate) + canvas_size[1]/200
        right = canvas_size[0]
        top = canvas_size[1]*(1-Canvas.current_demographic.base_graduation_rate)
        self.canvasObj.coords(self.base_line, left, bottom, right, top)
        self.canvasObj.coords(self.old_rate_text, canvas_size[0] / 2, top - canvas_size[1] / 50)

    def update_grad_rate(self, event=None):
        #print("Updating graduation rate")
        Canvas.current_demographic.updateGraduationRate(Window.Window.policy_list)
        graduation_rate_str = demographic_str = "Current Graduation Rate"
        self.draw_prediction_line([self.canvasObj.winfo_width(), self.canvasObj.winfo_height()])

    def resize(self, event):
        self.draw_prediction_line([event.width, event.height])

    def changeDemographic(self, demographic):
        Canvas.current_demographic = demographic
        self.titleText.set("Current Demographic: "+demographic.name)