# from json import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.image import Image
from kivy.utils import platform
from kivy.resources import resource_find
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.audio import SoundLoader
from kivy.logger import Logger
from kivy.graphics import Rectangle

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create Main Menu Layout
        mainmenu = BoxLayout(orientation='vertical', padding=20, spacing=10)

        scrolling_buttons_menu = ScrollView(size_hint=(0.5, 1), pos_hint={'center_x': 0.5})
        button_grid_menu = GridLayout(cols=1, spacing=20, size_hint_y=None)
        button_grid_menu.bind(minimum_height=button_grid_menu.setter('height'))
        scrolling_buttons_menu.add_widget(button_grid_menu)
        mainmenu.add_widget(scrolling_buttons_menu)

        self.add_widget(mainmenu)

        self.noise = SoundLoader.load('appassets/pissingallbye.wav')
        if not self.noise:
            Logger.error("Audio file failed to load")

        # Party Button
        button_party = Button(background_normal='appassets/button_imgs/button_party.png', size_hint=(0.5, None),
                              height=Window.width * 0.5 * (328 / 1017), pos_hint={'center_x': 0.5})  # Full Scale
        button_party.bind(on_press=self.on_button_press_test)
        button_grid_menu.add_widget(button_party)

        # Character Button
        button_chara = Button(background_normal='appassets/button_imgs/button_characters.png', size_hint=(0.5, None),
                              height=Window.width * 0.5 * (328 / 1017),
                              pos_hint={'center_x': 0.5})  # 50% height and 50% width with respect to image resolution
        button_chara.bind(on_press=self.on_button_press_test)
        button_grid_menu.add_widget(button_chara)

        # Archive Button
        button_archive = Button(background_normal='appassets/button_imgs/button_archives.png', size_hint=(0.5, None),
                                height=Window.width * 0.5 * (328 / 1017),
                                pos_hint={'center_x': 0.5})  # No Set with or height
        button_archive.bind(on_press=self.on_button_press_test)
        button_grid_menu.add_widget(button_archive)

        # Academic Button
        button_academ = Button(background_normal='appassets/button_imgs/button_academics.png', size_hint=(0.5, None),
                               height=Window.width * 0.5 * (328 / 1017), width=Window.height * 0.5 * (328 / 1017),
                               pos_hint={'center_x': 0.5})  # 50% hieght and with respect to image resolution
        button_academ.bind(on_press=self.on_button_press_test)
        button_grid_menu.add_widget(button_academ)

        # Gacha Button
        button_gacha = Button(background_normal='appassets/button_imgs/button_gacha.png', size_hint=(0.5, None),
                              height=Window.width * 0.5 * (328 / 1017), pos_hint={'center_x': 0.5})
        button_gacha.bind(on_press=self.on_button_press_test)
        button_grid_menu.add_widget(button_gacha)

        # Fusion Button
        button_fusion = Button(background_normal='appassets/button_imgs/button_fusion.png', size_hint=(0.5, None),
                               height=Window.width * 0.5 * (328 / 1017), pos_hint={'center_x': 0.5})
        button_fusion.bind(on_press=self.on_button_press_test)
        button_grid_menu.add_widget(button_fusion)

        # Calculator Button
        button_calculator = Button(background_normal='appassets/button_imgs/button_calc.png', size_hint=(0.5, None),
                                   height=Window.width * 0.5 * (328 / 1017), pos_hint={'center_x': 0.5})
        button_calculator.bind(on_press=self.on_button_press_test)
        button_grid_menu.add_widget(button_calculator)

        def on_button_press_test(self, instance):

            print("pees")

        ## MAIN MENU BUTTONS ##

    def on_button_press_party(self, instance):
        print("peepee")

    def on_button_press_chara(self, instance):
        print("peepee")

    def on_button_press_archive(self, instance):
        print("peepee")

    def on_button_press_academ(self, instance):
        print("peepee")

    def on_button_press_gacha(self, instance):
        print("peepee")

    def on_button_press_fuse(self, instance):
        print("peepee")

    def on_button_press_calc(self, instance):
        print("peepee")

class AndroidKivyApp(App):
    def build(self):

        screenmen = ScreenManager()
        screenmen.add_widget(MainMenu(name = "main_menu"))

        return screenmen

# Run the app
if __name__ == "__main__":
    AndroidKivyApp().run()
