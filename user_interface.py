from tkinter import Tk, Label, Button, Frame


class DTGUI:
    def __init__(self, master):
        self.master = master
        master.title("Dream Team GUI")

        self.label = Label(master, text="Dream Team Baby!")
        self.label.pack()

        self.greet_button = Button(master, text="Try Me", command=self.greet)
        self.greet_button.pack()

        self.frame = Frame(master, height=100, width = 100, bg="blue")
        self.frame.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Fuck you!")

root = Tk()
my_gui = DTGUI(root)
root.mainloop()