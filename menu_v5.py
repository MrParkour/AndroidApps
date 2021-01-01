from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import random
dropdown = DropDown()
Window.clearcolor = (1, 1, 1, 1)

def color(index):
    if index == 1:
        Window.clearcolor = (1, 0, 0, 1)
    if index == 2:
        Window.clearcolor = (0, 1, 0, 1)
    if index == 3:
        Window.clearcolor = (0, 0, 1, 1)
    if index == 4:
        Window.clearcolor = (1, 1, 1, 1)
    if index == 5:
        Window.clearcolor = random.random(), random.random(), random.random(), 1


# class app(App):
#     def build(self):

#         btn1 = Button(text='Red', size_hint_y=None, height=100, width=300)
#         btn1.bind(on_release=lambda btn: color(1))
#         dropdown.add_widget(btn1)

#         btn2 = Button(text='Green', size_hint_y=None, height=100, width=300)
#         btn2.bind(on_release=lambda btn: color(2))
#         dropdown.add_widget(btn2)

#         btn3 = Button(text='Blue', size_hint_y=None, height=100, width=300)
#         btn3.bind(on_release=lambda btn: color(3))
#         dropdown.add_widget(btn3)

#         btn4 = Button(text='Clear', size_hint_y=None, height=100, width=300)
#         btn4.bind(on_release=lambda btn: color(4))
#         dropdown.add_widget(btn4)

#         mainbutton = Button(text='Hello', size_hint=(None, None))
#         mainbutton.bind(on_release=dropdown.open)
#         dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
#         mainbutton.pos = (100, 200)

#         def build(self):
#             parent = Widget()
#             self.painter = MyPaintWidget()
#             clearbtn = Button(text='Clear')
#             clearbtn.bind(on_release=self.clear_canvas)
#             parent.add_widget(self.painter)
#             parent.add_widget(clearbtn)
#             return parent

#         return mainbutton

# if __name__ == '__main__':
#     app().run()

lbl = Button(text = 'Random', size_hint_y=None, height=100, width=300)
lbl.bind(on_release=lambda btn: color(5))

btn1 = Button(text='Red', size_hint_y=None, height=100, width=300)
btn1.bind(on_release=lambda btn: color(1))
dropdown.add_widget(btn1)

btn2 = Button(text='Green', size_hint_y=None, height=100, width=300)
btn2.bind(on_release=lambda btn: color(2))
dropdown.add_widget(btn2)

btn3 = Button(text='Blue', size_hint_y=None, height=100, width=300)
btn3.bind(on_release=lambda btn: color(3))
dropdown.add_widget(btn3)

btn4 = Button(text='Clear', size_hint_y=None, height=100, width=300)
btn4.bind(on_release=lambda btn: color(4))
dropdown.add_widget(btn4)

mainbutton = Button(text='Hello', size_hint=(None, None))
mainbutton.bind(on_release=dropdown.open)
dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
mainbutton.pos = (100, 200)

box = BoxLayout()
box.add_widget(lbl)
box.add_widget(btn)
runTouchApp(box)
# runTouchApp(mainbutton, secondbutton)
# runTouchApp(secondbutton)