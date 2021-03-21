'''
    event.py:
        Button event and text event

    Author: Peyton Fang
    Date: 2021.02.08

'''

__author__ = 'Peyton Fang'
__version__ = "1.0"
__copyright__ = "Copyright (C) 2021 Peyton Fang"
__email__ = "peyton888@gmail.com"


class CalculatorEvent:

    @staticmethod
    def button_click(btn) -> None:
        btn.notifySubscriber(btn.text)


class CalculatorPanelEvent:

    @staticmethod
    def on_text(instance, text: str) -> None:
        instance.text_changed(text)
