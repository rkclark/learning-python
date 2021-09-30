from tkinter import Frame, Tk, Button, Menu


class Window(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)

    self.master = master

    self.init_window()

  def init_window(self):
    self.master.title("My GUI")

    self.pack(fill="both", expand=1)

    # Quit button
    quitButton = Button(self, text="Quit", command=self.client_exit)
    quitButton.place(x=0, y=0)

    menu = Menu(self.master)
    self.master.config(menu=menu)

    # Quit from menu item
    fileMenu = Menu(menu)
    fileMenu.add_command(label="Exit", command=self.client_exit)

    menu.add_cascade(label="File", menu=fileMenu)

  def client_exit(self):
    exit()


root = Tk()
root.geometry("400x300")

app = Window(root)

root.mainloop()
