# Simple Fortune Cookie
# last edit 2/17/23
## hopefully will get more complex as revisions are made

moodPath = "resources/moods.txt" # read moods from moods.txt in resources
fortunesPath = "resources/fortunes/" # append + input mood + ".txt" later in code
cookiePicPath = "resources/images/fortuneCookie.png" # image location

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
    """ The fortune cookie will pick a fortune based on your mood. """

    # Drop down menu for moods
    self.mood_choice = StringVar(self)
    
    # read moods from file and store into mood list
    with open(moodPath) as file:
      moods = [line.rstrip() for line in file]
    
    # configure the grid for allowing mood choice
    self.mood_choice.set(moods[0])
    self.mood_menu = OptionMenu(self, self.mood_choice, *moods)
    Label(self, text="Your current mood:").grid(row = 0, column = 0, sticky = W)
    self.mood_menu.grid(row = 0, column = 1, sticky = W)

    # display fortune cookie image button to acquire fortunes
    self.cookiePicture = PhotoImage(file = cookiePicPath)
    self.cookieImage = self.cookiePicture.subsample(2, 2)
    self.cookiePanel = Button(self, text = "Click Me!",
                       command = self.acquire_fortune, image = self.cookieImage, compound = TOP).grid(row = 1, column = 2, sticky = W)

    # Text box for fortune
    self.text_box = Text(self, width = 50, height = 10, wrap = WORD)
    self.text_box.configure(state='disabled') # makes text box read-only
    self.text_box.grid(row = 1, column = 0, columnspan = 2)
    
  def acquire_fortune(self):
    """ Gets the user's mood; Produces a fortune. """
    # Deletes old entry
    self.text_box.configure(state='normal')
    self.text_box.delete(0.0, END)
                       
    mood = self.mood_choice.get()

    # read fortunes from correct file
    # file name of fortunes is the same as variable mood
    path = fortunesPath + mood.lower() + ".txt"
    myFortunes = [] # store all read fortunes
    with open(path) as file:
      for line in file:
        myFortunes.append(line)
    
    # grab random fortune
    num = random.randint(0,len(myFortunes)-1)
    fortune_text = myFortunes[num]
    
    # insert fortune
    self.text_box.insert(0.0, fortune_text)
    self.text_box.configure(state='disabled')
    


# main
root = Tk()
root.title("Fortune Cookie")
app = Application(root)
root.mainloop()


