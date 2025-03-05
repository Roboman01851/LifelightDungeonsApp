# from json import *
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class AndroidKivyApp(App):
    def build(self):
        # Simple vertical layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Add a label
        self.label = Label(text="Press button for message.", font_size='24sp')
        layout.add_widget(self.label)

        # Add a button
        button = Button(text="This is a test button", size_hint=(0.6, 0.2), pos_hint={'center_x': 0.5})
        button.bind(on_press=self.on_button_press_test)
        layout.add_widget(button)

        return layout

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
