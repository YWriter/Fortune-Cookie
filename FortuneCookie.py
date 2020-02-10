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
    """ The fortune cookie will pick a fortune based on your mood. """

    # Drop down menu for moods
    self.mood_choice = StringVar(self)
    moods = ["Happy", "Sad", "Neutral", "Annoyed", "Stressed"]
    self.mood_choice.set("Happy")
    self.mood_menu = OptionMenu(self, self.mood_choice, *moods)
    Label(self, text="Your current mood:").grid(row = 0, column = 0, sticky = W)
    self.mood_menu.grid(row = 0, column = 1, sticky = W)

    # Button for getting fortune
    submitBtn = Button(self,
                       text = "Get My Fortune",
                       command = self.acquire_fortune
                       ).grid(row = 2, column = 1, sticky = W)

    # Text box for fortune
    self.text_box = Text(self, width = 50, height = 10, wrap = WORD)
    self.text_box.grid(row = 1, column = 0, columnspan = 2)
    
  def acquire_fortune(self):
    """ Gets a random number; Gets the user's mood; Produces a fortune. """
    # Deletes old entry
    self.text_box.delete(0.0, END)
    
    # Dictionaries for fortunes
    happyFortunes = {1 : "You will have a grand time today!",
                     2 : "You are a rockstar! Keep rocking!",
                     3 : "Cultivate a new habit today, reap the benefits forever.",
                     4 : "A new beginning is on its way.",
                     5 : "The happiest people are the ones who learn to appreciate everything."}

    sadFortunes = {1 : "Treat yourself today; Feel better tomorrow.",
                   2 : "Time heals most wounds.",
                   3 : "If something is troubling you, talk to a friend or a loved one.",
                   4 : "Today is a new day.",
                   5 : "What doesn't kill you makes you stronger."}

    neutralFortunes = {1 : "Bored? Do something crazy different!",
                       2 : "Happiness comes from within.",
                       3 : "Take some time off to enjoy the little things.",
                       4 : "Failure is part of life.",
                       5 : "Effort is caring. Determination is passion."}
    
    annoyedFortunes = {1 : "The more you let it get to you, the weaker you become.",
                       2 : "Never let pressure guide your decisions. Your decisions are your own.",
                       3 : "To live is to feel.",
                       4 : "Take a break. You deserve it.",
                       5 : "Move on. Emotions are temporary. Life is fleeting."}

    stressedFortunes = {1 : "You're doing great. Keep up the good work.",
                        2 : "Whether you succeed or fail, it will pay off in the end.",
                        3 : "Take a nap. Recharge.",
                        4 : "If it is truly worth it, you will make time for it.",
                        5 : "Value yourself. You are as rich as you make yourself out to be."}
                       

    num = random.randint(1,5)
    mood = self.mood_choice.get()
    fortune_text = ""
    if mood == "Happy":
      fortune_text = happyFortunes.get(num)
    elif mood == "Sad":
      fortune_text = sadFortunes.get(num)
    elif mood == "Neutral":
      fortune_text = neutralFortunes.get(num)
    elif mood == "Annoyed":
      fortune_text = annoyedFortunes.get(num)
    elif mood == "Stressed":
      fortune_text = stressedFortunes.get(num)
      
    self.text_box.insert(0.0, fortune_text)
    
# main
root = Tk()
root.title("Fortune Cookie")
app = Application(root)
root.mainloop()
