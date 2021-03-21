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
__copyright__ = "Copyright (C) 2021 Peyton Fang"
__email__ = "peyton888@gmail.com"


from kivy.app import App
from layout.layout import CalculatorLayout
from events.event import CalculatorEvent
from controller import Controller

LAYOUT_ONLY = False


class CalculatorApp(App):
    def build(self):
        CL = CalculatorLayout()
        if LAYOUT_ONLY is True:
            return CL

        CC = Controller.create()
        CC.addSubscriber(CL.textpanel)

        for row in CL.btn_rows:
            for btn in row:
                btn.addSubscriber(CC)
                btn.bind(on_press=CalculatorEvent.button_click)

        return CL


def main():
    CalculatorApp().run()


if __name__ == "__main__":
    main()
