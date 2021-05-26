import kivy
from math import sqrt
from math import pow
from kivy.app import App

from kivy.core.window import Window
Window.size=(500*0.6,0.45*700)
Window.clearcolor = (104/255,235/255,211/255,1)

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

import time

Builder.load_file("design.kv")

first_num=0.0
op=''

class MyLayout(Widget):

    field=ObjectProperty(None)
    dell=ObjectProperty(None)
    cl=ObjectProperty(None)
    add=ObjectProperty(None)
    sub=ObjectProperty(None)
    mul=ObjectProperty(None)
    div=ObjectProperty(None)
    equals=ObjectProperty(None)
    sqrt=ObjectProperty(None)
    decimal=ObjectProperty(None)
    exponent=ObjectProperty(None)

    def addition(self):
        global first_num
        global op
        first_num=float(self.field.text)
        op='+'
        self.field.text="0"
    def subtraction(self):
        global first_num
        global op
        first_num=float(self.field.text)
        op='-'
        self.field.text="0"
    def multiplication(self):
        global first_num
        global op
        first_num=float(self.field.text)
        op='*'
        self.field.text="0"
    def division(self):
        global first_num
        global op
        first_num=float(self.field.text)
        op='/'
        self.field.text="0"
    def clear(self):
        global op
        self.field.text="0.0"
        op=''
    def delete(self):
        if len(self.field.text)==1:
            self.field.text="0"
        else:
            self.field.text=self.field.text[:-1]
    def sq(self):
        if float(self.field.text)>=0.0 :
            self.field.text=str(sqrt(float(self.field.text)))
        else :
            orig=self.field.text
            self.field.text="Invalid Input!Press Clr to resume!"
            #time.sleep(2)
            #self.field.text=orig
    def exp(self):
        global op
        global first_num
        first_num=float(self.field.text)
        self.field.text="0"
        op='^'
    def chg_sng(self):
        num=float(self.field.text)
        if num>0:
            self.field.text="-"+self.field.text
        elif num<0:
            self.field.text=self.field.text[1:]
    def equality(self):
        global first_num
        global op
        if op=='':
            pass
        elif op=='+':
            if self.field.text=='0' and first_num==1.0:
                self.field.text="Never Settle!"
            else :
                self.field.text=str(float(self.field.text)+first_num)
        elif op=='-':
            self.field.text=str(first_num-float(self.field.text))
        elif op=='*':
            self.field.text=str(float(self.field.text)*first_num)
        elif op=='/':
            try:
                self.field.text=str(first_num/float(self.field.text))
            except:
                self.field.text="Error!Press Clr to resume!"
        elif op=='^':
            self.field.text=str(pow(first_num, float(self.field.text)))
        op=''
        first_num=0

    def n1(self):
        self.field.text=str(float(self.field.text)*10+1)
    def n2(self):
        self.field.text=str(float(self.field.text)*10+2)
    def n3(self):
        self.field.text=str(float(self.field.text)*10+3)
    def n4(self):
        self.field.text=str(float(self.field.text)*10+4)
    def n5(self):
        self.field.text=str(float(self.field.text)*10+5)
    def n6(self):
        self.field.text=str(float(self.field.text)*10+6)
    def n7(self):
        self.field.text=str(float(self.field.text)*10+7)
    def n8(self):
        self.field.text=str(float(self.field.text)*10+8)
    def n9(self):
        self.field.text=str(float(self.field.text)*10+9)
    def n0(self):
        self.field.text=str(float(self.field.text)*10)


class TestApp(App):
    def build(self):
        return MyLayout()

TestApp().run()
