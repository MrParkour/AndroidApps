import kivy
kivy.require('1.7.2')
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu, RightContent

Window.clearcolor = (1, 1, 1, 1)
# KV = '''
# <RightContentCls>
#     disabled: True

#     MDIconButton:
#         icon: root.icon
#         user_font_size: "16sp"
#         pos_hint: {"center_y": .5}

#     MDLabel:
#         text: root.text
#         font_style: "Caption"
#         size_hint_x: None
#         width: self.texture_size[0]
#         text_size: None, None


# Screen:
#     MDRaisedButton:
#         id: button
#         text: "open menu"
#         size: 75, 50
#         size_hint: None, None
#         pos_hint: {"center_x": .5, "center_y": .5}
#         on_release: app.menu.open()
# '''
Builder.load_string("""
<Test>:
    GridLayout:
        cols: 1
        Button:
            id: clear_button
            text: "Clear"
            font_size: 12
            pos: (10, 100000000)
            on_press: root.clear()
            size: 75, 50
            size_hint: None, None
        Button:
            id: button_one
            text: "Red color"
            font_size: 12
            pos: (10, 80)
            on_press: root.clear()
            size: 750, 50
            size_hint: None, None
        Button:
            id: menu_opener
            text: "Open Menu"
            font_size: 12
            pos: (10, 80)
            on_press: open_menu()
            size: 750, 50
            size_hint: None, None
""")
class Highest(Screen):
    # def __init__(self):
    #     self.ids['button_one'].pos = 10, 10000
    def open_menu(self):
        self.ids['button_one'].pos = 10, 500
    def new(self):
        self.ids['clear_button'].background_color = 1, 0, 0, 1
    def clear(self):
        self.ids['clear_button'].background_color = 0, 0, 0, 1


# Create the screen manager
sm = ScreenManager()
sm.add_widget(Highest(name='Highest'))

# class TestApp(MDApp, Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.screen = Builder.load_string(KV)

#         def new(self):
#             self.ids['clear_button'].background_color = 1, 0, 0, 1

#         def clear(self):
#             self.ids['clear_button'].background_color = 0, 0, 0, 1

#         menu_items = []

#         def go_color(self, r, g, b, a):
#             Window.clearcolor = (r, g, b, a)
#             print(r)

        # menu_items.append(
        #     {
        #         "text": "Red",
        #         "font_style": "Caption",
        #         "height": "36dp",
        #         "top_pad": "10dp",
        #         "bot_pad": "10dp",
        #         "selected_color": [1, 0, 0, 1],
        #         "divider": None,
        #         "on_release": go_color(self, 1, 0, 0, 1),
        #     }
        # )
        # menu_items.append(
        #     {
        #         "text": "Green",
        #         "font_style": "Caption",
        #         "height": "36dp",
        #         "top_pad": "10dp",
        #         "bot_pad": "10dp",
        #         "divider": None,
        #         "selected_color": [0, 1, 0, 1],
        #         "on_release": go_color(self, 0, 1, 0, 1),
        #     }
        # )
        # menu_items.append(
        #     {
        #         "text": "Blue",
        #         "font_style": "Caption",
        #         "height": "36dp",
        #         "top_pad": "10dp",
        #         "bot_pad": "10dp",
        #         "divider": None,
        #         "selected_color": [0, 0, 1, 1],
        #         "on_release": go_color(self, 0, 0, 1, 1),
        #     }
        # )
    #     self.menu = MDDropdownMenu(
    #         caller=self.screen.ids.button,
    #         items=menu_items,
    #         width_mult=4,
    #     )
    #     self.menu.bind(on_release=self.menu_callback)
    
    # def menu_callback(self, instance_menu, instance_menu_item):
    #     print(instance_menu, instance_menu_item)
    # def build(self):
    #     return self.screen


# Test().run()

if __name__ == '__main__':
    TestApp().run()