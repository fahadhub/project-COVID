from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
import helpers
from cbot import text
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        check=Builder.load_string(helpers.kv)
        screen.add_widget(check)
        return screen

    def doThis(self,val):
        try:
            flag=text.chat.converse(val)
            reply="Bot>"+str(flag)
            return reply
        except:
            print("error while fetching answer")

MyApp().run()
