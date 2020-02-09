# Simple Fortune Cookie
## hopefully will get more complex as revisions are made

from tkinter import *
import random

class Application(Frame):
  """ GUI for our fortune-cookie picker. """
  def __init__(self, master):
    """ Initialize frame. """
    super(Application, self).__init__(master)
    self.grid()
    self.create_widgets()
    
  def create_widgets(self):
    pass

# main
root = Tk()
root.title("Fortune Cookie")
root.geometry("300x300") # temporary, changeable
app = Application(root)
root.mainloop()
