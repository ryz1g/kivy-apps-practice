import kivy
from datetime import datetime
from kivy.app import App
import threading
import time
import random

from kivy.core.window import Window
Window.size=(600,700)
Window.clearcolor = (0/255,0/255,0/255,1)

from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen

text_count=0
text_dict={}
dply=0

class MoleApp(App):
    def exit(self):
        Window.close()

    def game(self,t,score,*args):
        score.text="0"
        while int(t.text)>0:
            r=random.randint(0,8)
            args[r].text="X"
            time.sleep(0.4)
            args[r].text=""
        t.text="60"

    def timer(self,t,st):
        tim=59
        st.disabled=True
        while tim>=0:
            time.sleep(1)
            t.text=str(tim)
            tim=tim-1
        st.disabled=False

    def check(self,b,score):
        if b.text=='X':
            score.text=str(int(score.text)+1)

    def build(self):
        return Builder.load_file("design.kv")

MoleApp().run()
