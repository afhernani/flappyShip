import kivy
from kivy.properties import NumericProperty
from kivy.core.window import Window

from classes import WidgetDrawer

class Ship(WidgetDrawer):
    #Ship class. This is for the main ship object. 
    #velocity of ship on x/y axis
 
    impulse = 3 #this variable will be used to move the ship up
    grav = -0.1 #this variable will be used to pull the ship down
 
    velocity_x = NumericProperty(0) #we wont actually use x movement
    velocity_y = NumericProperty(0) 
 
    def move(self):                    
        self.x = self.x + self.velocity_x 
        self.y = self.y + self.velocity_y 
 
        #don't let the ship go too far
        if self.y >= Window.height*0.95: #don't let the ship go up too high
            self.impulse = -3
 
    def determineVelocity(self):
        #move the ship up and down
        #we need to take into account our acceleration
        #also want to look at gravity
        self.grav = self.grav*1.05  #the gravitational velocity should increase
        #set a grav limit
        if self.grav < -4: #set a maximum falling down speed (terminal velocity)
            self.grav = -4
        #the ship has a propety called self.impulse which is updated
        #whenever the player touches, pushing the ship up
        #use this impulse to determine the ship velocity
        #also decrease the magnitude of the impulse each time its used
 
        self.velocity_y = self.impulse + self.grav
        self.impulse = 0.95*self.impulse #make the upward velocity decay
 
    def update(self):
        self.determineVelocity() #first figure out the new velocity
        self.move()              #now move the ship