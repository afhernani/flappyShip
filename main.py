# Load the essential modules you’ll use
import kivy
kivy.require('1.9.1')
 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.graphics import Rectangle
import random
# Set desired graphic settings
from kivy.config import Config
Config.set('graphics','resizable',0) #don't make the app re-sizeable
#Graphics fix
#this fixes drawing issues on some phones
Window.clearcolor = (0,0,0,1.) 

# Create the classes
# import classes
# import asteroid
# import ship
# import mybutton
# import gui
from clientapp import ClientApp


if __name__ == '__main__' :
    ClientApp().run()