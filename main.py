import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import re
import random
import mysql.connector
import pandas as pd

class text:
    class Chat(object):

        def __init__(self, pairs, reflections={}):
            self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
            self._reflections = reflections
            self._regex = self._compile_reflections()

        def _compile_reflections(self):
            sorted_refl = sorted(self._reflections, key=len, reverse=True)
            return re.compile(r"\b({0})\b".format("|".join(map(re.escape, sorted_refl))), re.IGNORECASE)

        def _substitute(self, str):
            return self._regex.sub(lambda mo: self._reflections[mo.string[mo.start() : mo.end()]], str.lower())

        def _wildcards(self, response, match):
            pos = response.find("%")
            while pos >= 0:
                num = int(response[pos + 1 : pos + 2])
                response = (response[:pos]+ self._substitute(match.group(num))+ response[pos + 2 :])
                pos = response.find("%")
            return response

        def respond(self, str):
            for (pattern, response) in self._pairs:
                match = pattern.match(str)
                if match:
                    resp = random.choice(response)  # pick a random response
                    resp = self._wildcards(resp, match)  # process wildcards
                    return resp

        def converse(self, str):
            return self.respond(str)

    li=[""]
    mydb = mysql.connector.connect(host="localhost", user="root", password="", database="test")
    df = pd.read_sql("SELECT Context, Answer FROM faq", con = mydb)
    list = df.values.tolist()
    for x in range(85):
        li[0]=list[x][1]
        list[x][1]=li
        li=[""]
    chat=Chat(list)


class ScrollableLabel(ScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = GridLayout(cols=1, size_hint_y=None)
        self.add_widget(self.layout)
        self.chat_history = Label(size_hint_y=None, markup=True)
        self.scroll_to_point = Label()
        self.layout.add_widget(self.chat_history)
        self.layout.add_widget(self.scroll_to_point)

    def update_chat_history(self, message):
        self.chat_history.text += '\n' + message
        self.layout.height = self.chat_history.texture_size[1] + 15
        self.chat_history.height = self.chat_history.texture_size[1]
        self.chat_history.text_size = (self.chat_history.width * 0.98, None)
        self.scroll_to(self.scroll_to_point)

    def update_chat_history_layout(self, _=None):
        self.layout.height = self.chat_history.texture_size[1] + 15
        self.chat_history.height = self.chat_history.texture_size[1]
        self.chat_history.text_size = (self.chat_history.width * 0.98, None)


class chatpage(GridLayout):
    def adjust_fields(self, *_):
        if Window.size[1] * 0.1 < 50:
            new_height = Window.size[1] - 50
        else:
            new_height = Window.size[1] * 0.9
        self.history.height = new_height
        if Window.size[0] * 0.2 < 160:
            new_width = Window.size[0] - 160
        else:
            new_width = Window.size[0] * 0.8
        self.new_message.width = new_width
        Clock.schedule_once(self.history.update_chat_history_layout, 0.01)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 2
        self.history = ScrollableLabel(height=Window.size[1]*0.9, size_hint_y=None)
        self.add_widget(self.history)
        self.new_message = TextInput(width=Window.size[0]*0.8, size_hint_x=None, multiline=False)
        self.send = Button(text="Send")
        self.send.bind(on_press=self.send_message)
        bottom_line = GridLayout(cols=2)
        bottom_line.add_widget(self.new_message)
        bottom_line.add_widget(self.send)
        self.add_widget(bottom_line)
        Window.bind(on_key_down=self.on_key_down)
        Clock.schedule_once(self.focus_text_input, 1)
        self.bind(size=self.adjust_fields)

    def on_key_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40:
            self.send_message(None)

    def send_message(self, _):
        message = self.new_message.text
        self.new_message.text = ''

        if message:
            self.history.update_chat_history(f'[color=dd2020]You[/color] > {message}')

        Clock.schedule_once(self.focus_text_input, 0.1)
        reply=text.chat.converse(message)
        self.history.update_chat_history(f'[color=20dd20]Bot[/color] > {reply}')

    def focus_text_input(self, _):
        self.new_message.focus = True

    def incoming_message(self):
        self.history.update_chat_history(f'[color=20dd20]Bot[/color] > reply')

class EpicApp(App):
    def build(self):

        self.screen_manager=ScreenManager()

        self.chat_page=chatpage()
        screen = Screen(name='Chat')
        screen.add_widget(self.chat_page)
        self.screen_manager.add_widget(screen)



        return self.screen_manager



if __name__=="__main__":
    chat_app=EpicApp()
    chat_app.run()
