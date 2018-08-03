import kivy
from classes import WidgetDrawer
from kivy.properties import NumericProperty

class Asteroid(WidgetDrawer):
    #Asteroid class. The flappy ship will dodge these
    velocity_x = NumericProperty(0) #initialize velocity_x and velocity_y
    velocity_y = NumericProperty(0) #declaring variables is not necessary in python
 #update the position using the velocity defined here. every time move is called we change the position by velocity_x  
    def move(self):                    
        self.x = self.x + self.velocity_x 
        self.y = self.y + self.velocity_y 
    def update(self): 
#the update function moves the astreoid. Other things could happen here as well (speed changes for example)       
        self.move() 