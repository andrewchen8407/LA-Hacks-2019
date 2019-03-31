from tkinter import *
from tkinter.ttk import *
import data
# import process
# import human
import tkinter as tk
from tkinter import font as tkfont
# from tkinter import ttk
# import threading
import webbrowser
from pydub import AudioSegment

class LAHacks2019(tk.Tk):
    nameDict = None
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        global nameDict
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Got Finance?", font=('Times', 60, 'bold italic'), fg = 'gold')

        label.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="This app is a simultation of a real-life situation in which one must economize properly.")
        label2.pack(side="top", fill="x")
        label3 = tk.Label(self,
                          text="Choose a character and buy goods to keep their attributes at healthy limits.")
        label3.pack(side="top", fill="x", pady=10)
        label4 = tk.Label(self,
                          text="Being in debt (having a negative account balance) or exhausting all account balance money")
        label4.pack(side="top", fill="x")
        label5 = tk.Label(self,
                          text="while having attributes at unhealthy levels causes one to \'die\'.")
        label5.pack(side="top", fill="x", pady=10)

        data.get_json()
        nameDict = {v[0]:v[2] for k,v in data.account_dict.items()}
        names = Combobox(self, values = [v[0] for v in data.account_dict.values()])
        names.pack()
        def show_page_one():
            name = names.get()
            controller.frames["PageOne"].set_vals(name)
            if name!= "":
                controller.show_frame("PageOne")
        button1 = tk.Button(self, text="Check Health",
                            command=lambda: show_page_one())
        button1.pack()
        button2 = tk.Button(self, text = "Check Financial News", command = lambda: controller.show_frame("PageThree"))
        button2.pack()

        comic_photo = PhotoImage(file="comic.png")
        self.comic_lab = Label(self, image=comic_photo)
        self.comic_lab.image = comic_photo
        self.comic_lab.pack(pady=5)

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Play Now", font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=100)

        # frames = [PhotoImage(file='kickassfinance.gif', format='gif -index %i' % (i)) for i in range(28)]
        #
        # def update(ind):
        #     frame = frames[ind]
        #     ind += 1
        #     label.configure(image=frame)
        #     self.after(28, update, ind)
        #
        # label = Label(self)
        # label.pack()
        # self.after(0, update, 0)
        # self.mainloop()

        # kickass_gif = PhotoImage(file="kickassfinance.gif", format="gif -index 2")
        # kickass_lab = Label(image=kickass_gif)
        # kickass_lab.image = kickass_gif  # keep a reference!

        #health labels
        tk.Label(self, text='Health', anchor='w', fg = "blue", font = ("Times", "20", 'bold')).pack(fill='both')
        self.health_lab = tk.Label(self, text='0', anchor='w', fg = "red")
        self.health_lab.pack(fill="both")
        # self.health_prog = ttk.Progressbar(self, orient="horizontal",
        #                            length=200, mode="determinate", maximum = 200,  variable=self.val)
        # self.health_prog.pack()
        tk.Label(self, text='Entertainment', anchor='w', fg="pink", font = ("Times", "20", 'bold')).pack(fill='both')
        self.entertainment_lab = tk.Label(self, text='0', anchor='w', fg="red")
        self.entertainment_lab.pack(fill="both")
        # self.entertain_prog = ttk.Progressbar(self.root, orient="horizontal",
        #                            length=200, mode="determinate", maximum = 200)
        # self.entertain_prog.pack()
        tk.Label(self, text='Food', anchor='w', fg="orange", font = ("Times", "20", 'bold')).pack(fill='both')
        self.food_lab = tk.Label(self, text='0', anchor='w', fg="red")
        self.food_lab.pack(fill="both")
        # self.food_prog = ttk.Progressbar(self.root2, orient="horizontal",
        #                            length=200, mode="determinate", maximum = 200,  variable=self.val)
        # self.food_prog.pack()
        tk.Label(self, text='Luxury', anchor='w', fg="purple", font = ("Times", "20", 'bold')).pack(fill='both')
        self.luxury_lab = tk.Label(self, text='0', anchor='w', fg="red")
        self.luxury_lab.pack(fill="both")
        # self.luxury_prog = ttk.Progressbar(self.root, orient="horizontal",
        #                            length=200, mode="determinate", maximum = 200,  variable=self.val)
        # self.luxury_prog.pack()
        tk.Label(self, text='Balance', anchor='w', fg="gold", font = ("Times", "20", 'bold')).pack(fill='both')
        self.balance_lab = tk.Label(self, text='0', anchor='w', fg="black")
        self.balance_lab.pack(fill="both")
        tk.Label(self, text='Status', anchor='w', fg="silver", font = ("Times", "20", 'bold')).pack(fill='both')
        self.status_lab = tk.Label(self, text='N/A', anchor='w', fg="black")
        self.status_lab.pack(fill="both")
        self.button = tk.Button(self, text="Go to the start page",
                           command=lambda: self.controller.show_frame("StartPage"))
        self.button2 = tk.Button(self, text="Goods and Services",
                            command=lambda: controller.show_frame("PageTwo"))
        self.button.pack()
        self.button2.pack()
        self.my_name = None

    def set_vals(self,name):
        n = ["red", "yellow", "green"]
        self.my_name = name
        if name in nameDict:
            self.label.config(text = "Welcome back, " + name +"!", font = ('Arial', 50))
            self.health_lab.config(text=str(nameDict[name].get_health()))
            self.entertainment_lab.config(text=str(nameDict[name].get_entertainment()))
            self.food_lab.config(text=str(nameDict[name].get_food()))
            self.luxury_lab.config(text=str(nameDict[name].get_luxury()))
            self.balance_lab.config(text="$"+str(nameDict[name].get_balance()), font = ('Times', '20', 'bold'))
            if nameDict[name].alive:
                self.status_lab.config(text = "Wow, you're doing great!", font = ('Arial', 30, "bold italic"))
                self.button2.config(state="normal", text="Goods and Services")
            else:
                self.status_lab.config(text = "Oh no! You are dead!", font = ("Times", "40", "bold italic") , fg='red')
                self.button2.config(state = "disabled", text = "No more shopping for you!")
            if nameDict[name].get_health()<50:
                self.health_lab.config(font = ("Times", "35"), fg = "red")
            elif 50<=nameDict[name].get_health()<75:
                self.health_lab.config(font = ("Times", "35"), fg= "brown")
            else:
                self.health_lab.config(font = ("Times", "35"), fg="green")
            if nameDict[name].get_entertainment()<30:
                self.entertainment_lab.config(font = ("Times", "35"), fg = "red")
            elif 30<=nameDict[name].get_entertainment()<65:
                self.entertainment_lab.config(font = ("Times", "35"), fg= "brown")
            else:
                self.entertainment_lab.config(font = ("Times", "35"), fg="green")
            if nameDict[name].get_food()<40:
                self.food_lab.config(font = ("Times", "35"), fg = "red")
            elif 40<=nameDict[name].get_food()<70:
                self.food_lab.config(font = ("Times", "35"), fg= "brown")
            else:
                self.food_lab.config(font = ("Times", "35"), fg="green")
            if nameDict[name].get_luxury()<5:
                self.luxury_lab.config(font = ("Times", "35"), fg = "red")
            elif 5<=nameDict[name].get_luxury()<20:
                self.luxury_lab.config(font = ("Times", "35"), fg= "brown")
            else:
                self.luxury_lab.config(font = ("Times", "35"), fg="green")

    # def advance(self):
    #     self.val.set(8)
    # def changeProgress(self, name):
    #     if name in nameDict:
    #         k = 0
    #         print("hit")
    #         while k <= nameDict[name].get_health():
    #             self.update_idletasks()
    #         self.after(100)
            # self.health_prog = ttk.Progressbar(self, orient="horizontal",
            #                                    length=nameDict[name].get_health(), mode="determinate", maximum=200)
            # self.health_prog.pack()
            #
            # self.entertain_prog = ttk.Progressbar(self, orient="horizontal",
            #                                       length = nameDict[name].get_entertainment(), mode="determinate", maximum=200)
            # self.entertain_prog.pack()
            # self.food_prog = ttk.Progressbar(self, orient="horizontal",
            #                                  length=nameDict[name].get_food(), mode="determinate", maximum=200)
            # self.food_prog.pack()
            # self.luxury_prog = ttk.Progressbar(self, orient="horizontal",
            #                                    length=nameDict[name].get_luxury(), mode="determinate", maximum=200)
            # self.luxury_prog.pack()



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Goods and Services", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        #getting images
        apple_photo = PhotoImage(file ="apple.png")
        car_photo = PhotoImage(file = "car.png")
        doctor_photo = PhotoImage(file = "doctor.png")
        exercise_photo = PhotoImage(file="exercise.png")
        phone_photo = PhotoImage(file = "phone.png")
        fast_food_photo = PhotoImage(file="fastfood.png")
        theme_park_photo = PhotoImage(file="themepark.png")
        yoga_photo = PhotoImage(file = "yoga.png")

        #labels to stop garbage collection
        apple_lab = Label(image=apple_photo)
        apple_lab.image = apple_photo  # keep a reference!
        car_lab = Label(image=car_photo)
        car_lab.image = car_photo  # keep a reference!
        doctor_lab = Label(image=doctor_photo)
        doctor_lab.image = doctor_photo  # keep a reference!
        exercise_lab = Label(image=exercise_photo)
        exercise_lab.image = exercise_photo  # keep a reference!
        phone_lab = Label(image=phone_photo)
        phone_lab.image = phone_photo  # keep a reference!
        fast_food_lab = Label(image=fast_food_photo)
        fast_food_lab.image = fast_food_photo  # keep a reference!
        theme_park_lab = Label(image=theme_park_photo)
        theme_park_lab.image = theme_park_photo  # keep a reference!
        yoga_lab = Label(image=yoga_photo)
        yoga_lab.image = yoga_photo

        #adding picture buttons
        # scroll = Scrollbar(self)
        # scroll.pack(side=RIGHT, fill=Y)
        def show_page_one(h, e, f, l, b):
            name = controller.frames["PageOne"].my_name
            nameDict[name].set_health(nameDict[name].get_health()*h)
            nameDict[name].set_entertainment(nameDict[name].get_entertainment() * e)
            nameDict[name].set_food(nameDict[name].get_food() * f)
            nameDict[name].set_luxury(nameDict[name].get_luxury() * l)
            nameDict[name].set_balance(nameDict[name].get_balance() + b)
            nameDict[name].update_status()
            controller.frames["PageOne"].set_vals(name)
            controller.show_frame("PageOne")
        self.pic_1 = tk.Button(self, image=apple_photo, text="OK",command = lambda: show_page_one(1.1, 1, 1.05, 1, -50))
        self.pic_2 = tk.Button(self, image=car_photo, text="OK", command=lambda: show_page_one(.9, 1.10, 1, 1.3, -700))
        self.pic_3 = tk.Button(self, image=doctor_photo, text="OK",command=lambda: show_page_one(1.2, 1, 1, 1, -100))
        self.pic_4 = tk.Button(self, image=exercise_photo, text="OK",command=lambda: show_page_one(1.15, .95, .85, 1, -75))
        self.pic_5 = tk.Button(self, image=phone_photo, text="OK", command=lambda: show_page_one(1, 1.15, 1, 1.07, -300))
        self.pic_6 = tk.Button(self, image=fast_food_photo, text="OK", command=lambda: show_page_one(.8, 1.05, 1.1, 1, -100))
        self.pic_7 = tk.Button(self, image=theme_park_photo, text="OK", command=lambda: show_page_one(.9, 1.12, 1.05, 1, -100))
        self.pic_8 = tk.Button(self, image=yoga_photo, text="OK", command=lambda: show_page_one(1.15, 1.05, 0.95, 1, -100))
        tk.Label(self,
                 text='Apple: $50, Car: $700, Doctor: $100, Treadmill: $75, Cellphone: $300, Fast Food: $100, Theme Park: $100, Yoga: $100',
                 anchor='w', fg="black").pack(fill='both')
        self.pic_1.pack(pady = 5)
        self.pic_2.pack(pady = 5)
        self.pic_3.pack(pady = 5)
        self.pic_4.pack(pady = 5)
        self.pic_5.pack(pady = 5)
        self.pic_6.pack(pady = 5)
        self.pic_7.pack(pady = 5)
        self.pic_8.pack(pady = 5)
class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Read the Latest Financial Stories", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        subhead = tk.Label(self, text="Articles")
        subhead.pack(side="top", fill="x", pady=10)
        def callback1(event):
            webbrowser.open_new(r"https://www.google.com/url?q=https://www.tc.columbia.edu/articles/2010/february/teaching-kids-about-the-national-debt/&sa=D&source=hangouts&ust=1554091157827000&usg=AFQjCNEU6sqJdA_IXwDNmRHXFbGps-qWGA")
        def callback2(event):
            webbrowser.open_new(r"https://www.usa.gov/before-you-shop")
        def callback3(event):
            webbrowser.open_new(r"https://www.usa.gov/currency")
        link1 = tk.Label(self, text="Teaching Kids about National Debt",fg = "blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", callback1)
        link2 = tk.Label(self, text="Before You Shop...", fg="blue", cursor="hand2")
        link2.pack()
        link2.bind("<Button-1>", callback2)
        link3 = tk.Label(self, text="United States Currency", fg="blue", cursor="hand2")
        link3.pack()
        link3.bind("<Button-1>", callback3)
        self.button = tk.Button(self, text="Go to the start page",
                                command=lambda: self.controller.show_frame("StartPage"))
        self.button.pack()
        # subhead2 = tk.Label(self, text="Audio Learning")
        # subhead2.pack(side="top", fill="x", pady=10)
        # song = AudioSegment.from_mp3("output1.mp3")
        #
        # play = lambda: song.play()
        # button = Button(self, text='Play', command=play)


if __name__ == "__main__":
    app = LAHacks2019()
    app.mainloop()
