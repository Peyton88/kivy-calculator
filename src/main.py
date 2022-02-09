#!/usr/bin/python3

'''
    main.py:
        Calculator start from
        Binding event and subscription

    Author: Peyton Fang
    Date: 2021.02.08

'''

__author__ = 'Peyton Fang'
__version__ = "1.0"
__email__ = "peyton888@gmail.com"


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from layout.layout import CalculatorLayout
from events.event import CalculatorEvent
from controller import Controller

LAYOUT_ONLY = False

class MainScreen(Screen):
    def __init__(self):
        super().__init__(name='main_screen')
        CL = CalculatorLayout()
        self.add_widget(CL)

        if LAYOUT_ONLY is True:
            return

        CC = Controller.create()
        CC.addSubscriber(CL.textpanel)

        for row in CL.btn_rows:
            for btn in row:
                btn.addSubscriber(CC)
                btn.bind(on_press=CalculatorEvent.button_click)

class RootWidget(ScreenManager):
    pass

class CalculatorApp(App):
    def build(self):
        rootWidget = RootWidget()
        rootWidget.add_widget(MainScreen())
        return rootWidget

def main():
    CalculatorApp().run()


if __name__ == "__main__":
    main()
