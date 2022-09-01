from cgitb import text
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

def on_press(btn):
    btn.text = "apertado"
def on_release(btn):
    btn.text = "solto"
class MyApp(MDApp):
    def build(self):
        box = BoxLayout()
        box.orientation = "vertical"
        #label
        label = MDLabel()
        label.text = "ola mundo"
        label.font_size = 50
        #input
        text_input = TextInput(

        )
        #buttao
        btn = Button(
            text="botao",
            font_size=50,
            on_press=on_press,
            on_release=on_release
        )
        box.add_widget(label)
        box.add_widget(text_input)
        box.add_widget(btn)
        return box
MyApp().run()