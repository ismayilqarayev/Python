def get(number_1, number_2, number_3, number_4, number_5):
    print(f"{number_1}")
    print(f"{number_2}")
    print(f"{number_3}")
    print(f"{number_4}")
    print(f"{number_5}")

get(number_1 = 3, 
    number_2 = 2, 
    number_3 = 3,               # funksiyanin parametrine 
    number_4 = 4,               # melumat gondermek
    number_5 = 5)               #
                                # 
#-------------------------------------------------------
import os
import sys

class Prog:
    def __init__(self) -> None:
        self.age = 22
        self.ismaried = 3
        self.result = self.age + self.ismaried
        print(self.result)
        print("############################")

    def mainloop(self):
        pass 


if __name__ == "__main__":
    prog = Prog()
    prog.mainloop()

# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
class App:
    def __init__(self):
        numbers = int(input())
        if numbers < -5:
            print('low')
        elif -5 <= numbers <= 4:
            print('low')
        else:
            print('hif')

    def mainloop(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
#-------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
#  -----------------------------------------------------
language = str(input())
if language == "english":
    print("hi")
elif language == "german":
    print("hallo")
else:
    print("privet")
#-------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
#  -----------------------------------------------------
age = 22
isMarried = False
result = age > 21 or isMarried
print(result)

message = "ismayil net"
person2 = "ismayil"
print(person2 in message)

#######################################333
from ast import Num
import os
import sys

number = 1

while number < 5:
    print(f"number = {number}")
    number += 1

print("................")

message = "hello"

for c in message:
    print(c)

number = 1
number_2 = 2

while number < 10:
    print(number * number_2, end="\t")
    number_2 += 1
  
#-------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
#  -----------------------------------------------------

'''
knopkalarda animasiya yaratmaq
'''
'''
Widget animation
================

This example demonstrates creating and applying a multi-part animation to
a button widget. You should see a button labelled 'plop' that will move with
an animation when clicked.
'''

import kivy
kivy.require('1.0.7')

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):

    def animate(self, instance):
        # create an animation object. This object could be stored
        # and reused each call or reused across different widgets.
        # += is a sequential step, while &= is in parallel
        animation = Animation(pos=(100, 100), t='out_bounce')
        animation += Animation(pos=(200, 100), t='out_bounce')
        animation &= Animation(size=(500, 500))
        animation += Animation(size=(100, 50))

        # apply the animation on the button, passed in the "instance" argument
        # Notice that default 'click' animation (changing the button
        # color while the mouse is down) is unchanged.
        animation.start(instance)

    def build(self):
        # create a button, and  attach animate() method as a on_press handler
        button = Button(size_hint=(None, None), text='plop',
                        on_press=self.animate)
        return button


if __name__ == '__main__':
    TestApp().run()

