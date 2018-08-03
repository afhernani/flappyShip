import kivy
from kivy.uix.button import Button
from kivy.core.window import Window

class MyButton(Button):
    '''
    The next class will be used to streamline buttons. 
    For now we will have just one button. 
    More are planned for future versions.
    '''
    #class used to get uniform button styles
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
 #all we're doing is setting the font size. more can be done later
        self.font_size = Window.width*0.018