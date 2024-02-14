from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDIconButton
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.screen import Screen

class Mobil_App(MDApp):
    def build(self):
        #yazının rəng çları}--------------------------\
        self.theme_cls.primary_palette="Yellow"# <----|

        #yazının şrifdi}-------------------------\
        self.theme_cls.primary_hue="A700"# <-----|

        #arxa fon rəng}------------------------\
        self.theme_cls.theme_style="Dark"# <---|

        # dəyişən yaradıb həmin dəyişəni ekran funksiyasına yönəltmək}---\
        screen = Screen()#  <--------------------------------------------|
        label = MDLabel(
            text='uran',
            halign='center',
            theme_text_color='Custom',
            text_color=(
                236 / 255.0,
                98 / 255.0,
                81 / 255, 1
            ),
            font_style='Caption'
        )

        button = MDRectangleFlatButton(text='configuration', pos_hint={'center_x':0.5, 'center_y':0.4})
        button_2 = MDRectangleFlatButton(text='searcihing',  pos_hint={'center_x':0.5, 'center_y':0.3})
        icon_button = MDFloatingActionButton(icon='android', pos_hint={'center_x': 0.5, 'center_y': 0.6})
        
        
        screen.add_widget(label)
        screen.add_widget(button)
        screen.add_widget(button_2)
        screen.add_widget(icon_button)
        return screen
    
Mobil_App().run()