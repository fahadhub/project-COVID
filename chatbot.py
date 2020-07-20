from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
import helpers
from cbot import text
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
global oldreply

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Controller(FloatLayout):
    Builder.load_string(helpers.kv1)
    label_wid = ObjectProperty()
    textf = ObjectProperty()

    def doThis(self,val):
        global old
        try:
            try:
                flag=text.chat.converse(val)
                if str(flag)=="None":
                    flag="Ask another question"
                reply="\nYou: "+val+" \n\nBot: "+str(flag)+"\n"
                self.label_wid.text =reply
                old=old+reply
                self.label_wid.text =old
            except:
                flag=text.chat.converse(val)
                if str(flag)=="None":
                    flag="Ask another question"
                reply="\nYou: "+val+" \n\nBot: "+str(flag)+"\n"
                self.label_wid.text =reply
                old=reply
                self.label_wid.text =old
        except:
            self.label_wid.text = "There seems to be an error"

    def clearField(self):
        self.textf.text=""

class ControllerApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark"
        return Controller()




ControllerApp().run()
