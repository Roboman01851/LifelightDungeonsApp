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
        self.label = Label(text="Hello from Android!", font_size='24sp')
        layout.add_widget(self.label)

        # Add a butto
        button = Button(text="Press Me", size_hint=(0.6, 0.2), pos_hint={'center_x': 0.5})
        button.bind(on_press=self.on_button_press)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        self.label.text = "Button Pressed on Android!"

# Run the app
if __name__ == "__main__":
    AndroidKivyApp().run()
