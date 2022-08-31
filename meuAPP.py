from kivymd.app import MDApp
from kivy.lang import Builder

class MeuApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.title = "conversor de velocidade"
        return Builder.load_file('menu.kv')
    def fechar(self):
        self.stop()
app = MeuApp()
app.run()