from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.screen import Screen
from kivy.uix.video import Video
from kivy.clock import Clock 

class Mobil_App(MDApp): 
    def build(self):   
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

        
        screen = Screen()
        label = MDLabel(
            text = 'MOBIL_APLICATION',
            halign = 'center',
            theme_text_color = 'Custom',
            text_color = (
                236 / 255.0,
                98 / 255.0,
                81 / 255, 1),
                font_style = 'Caption')


        button_1 = MDRectangleFlatButton(
            text = 'configuration',
            pos_hint = {'center_x': 0.5, 'center_y': 0.4})
        
        button_2 = MDRectangleFlatButton(
            text = 'searcihing', 
            pos_hint = {'center_x': 0.5, 'center_y': 0.3})
        
        icon_button = MDFloatingActionButton(
            icon = 'android',
            pos_hint = {'center_x': 0.5, 'center_y': 0.6})
        
  
        screen.add_widget(label)
        screen.add_widget(button_1)
        screen.add_widget(button_2)
        screen.add_widget(icon_button)
        return screen
    
    # dt means delta-time
    def my_callback(dt):
        pass

# call my_callback every 0.5 seconds
    Clock.schedule_interval(my_callback, 0.5)

# call my_callback in 5 seconds
    Clock.schedule_once(my_callback, 5)

# call my_callback as soon as possible (usually next frame.)
    Clock.schedule_once(my_callback)
    
if __name__ == "__main__":
    Mobil_App().run()
#-------------------------------------------------------------------------------#

message = "hello world!"
hello = "hello"
print(hello not in message)  # False
 
gold = "gold"
print(gold not in message)  # True