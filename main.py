from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
    pass
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return MyBoxLayout()
MainApp().run()