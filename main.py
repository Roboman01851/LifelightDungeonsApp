# from json import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class AndroidKivyApp(App):
    def build(self):
        # Simple vertical layout
        mainmenu = BoxLayout(orientation='vertical', padding=20, spacing=10)


        # Party Button
        button_party = Button(text="Party", size_hint=(0.6, 0.2), pos_hint={'center_x': 0.5})
        button_party.bind(on_press=self.on_button_press_test)
        mainmenu.add_widget(button_party)

        # Character Button
        button_chara = Button(text="Characters", size_hint=(0.6, 0.2), pos_hint={'center_x': 0.5})
        button_chara.bind(on_press=self.on_button_press_test)
        mainmenu.add_widget(button_chara)

        # Archive Button
        button_archive = Button(text="Archives", size_hint=(0.6, 0.2), pos_hint={'center_x': 0.5})
        button_archive.bind(on_press=self.on_button_press_test)
        mainmenu.add_widget(button_archive)

        # Academic Button
        button_academ = Button(text="Academics", size_hint=(0.6, 0.2), pos_hint={'center_x': 0.5})
        button_academ.bind(on_press=self.on_button_press_test)
        mainmenu.add_widget(button_academ)

        # Gacha Button
        button_gacha = Button(text="Gacha", size_hint=(0.6, 0.2), pos_hint={'center_x': 0.5})
        button_gacha.bind(on_press=self.on_button_press_test)
        mainmenu.add_widget(button_gacha)

        # Fusion Button
        button_fusion = Button(text="Fusion", size_hint=(0.6, 0.2), pos_hint={'center_x': 0.5})
        button_fusion.bind(on_press=self.on_button_press_test)
        mainmenu.add_widget(button_fusion)

        # Calculator Button
        button_calculator = Button(text="Calculator", size_hint=(0.6, 0.2), pos_hint={'center_x': 0.5})
        button_calculator.bind(on_press=self.on_button_press_test)
        mainmenu.add_widget(button_calculator)

        return mainmenu

    def on_button_press_test(self, instance):
        self.label.text = "FUCK YOU LOL"

    ## MAIN MENU BUTTONS ##

    def on_button_press_party(self, instance):
        return 0

    def on_button_press_chara(self, instance):
        return 0

    def on_button_press_archive(self, instance):
        return 0

    def on_button_press_academ(self, instance):
        return 0

    def on_button_press_gacha(self, instance):
        return 0

    def on_button_press_fuse(self, instance):
        return 0

    def on_button_press_calc(self, instance):
        return 0

    ###########################################

    ## EXTRA ##

    def on_button_press_spirit(self, instance):
        return 0

    def on_button_press_lore(self, instance):
        return 0

    def on_button_press_skll(self, instance):
        return 0

    def on_button_press_beast(self, instance):
        return 0

    def on_button_press_chara(self, instance):
        return 0

    #############################################


# Run the app
if __name__ == "__main__":
    AndroidKivyApp().run()
