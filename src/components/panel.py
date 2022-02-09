'''
    panel.py:
        Display input number and calculation result

    Author: Peyton Fang
    Date: 2021.02.08

'''

__author__ = 'Peyton Fang'
__version__ = "1.0"
__email__ = "peyton888@gmail.com"


from kivy.uix.label import Label
from kivy.metrics import sp
from components.display import CDisplay
from common.defines import BtnText as bt
from common.defines import NO_VALUE
from events.event import CalculatorPanelEvent


class CPanel(CDisplay):
    MaxTextSize = 70
    MinTextSize = 10

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs,
            text="0",
            font_size="{}sp".format(CPanel.MaxTextSize),
            halign="right",
            valign="center",
            size_hint=(1.0, 1.2)
        )
        self.sign = ""
        self.number = "0"
        self.label = Label(text="0", font_size="{}sp".format(CPanel.MaxTextSize))

    @staticmethod
    def create():
        panel = CPanel()
        panel.bind(size=panel.setter('text_size'))
        panel.bind(text=CalculatorPanelEvent.on_text)
        return panel

    def update(self, data: str) -> None:
        """
        Override update in subscriber
        """

        if data == "Error":
            self.text = data
        else:
            self.get_sign_and_number(data)
            self.text = self.sign + self.to_thousand_sep(self.number)

    def text_changed(self, text: str) -> None:
        self.check_if_text_exceed_panel(text)

    def check_if_text_exceed_panel(self, text: str) -> None:
        self.label.font_size = CPanel.MaxTextSize
        self.label.text = text
        self.label._label.refresh()
        text_width = self.label._label._internal_size[0]
        if text_width > self.width:
            while text_width > self.width:
                font_size = self.label.font_size - sp(20)
                if font_size < sp(CPanel.MinTextSize):
                    break
                self.label.font_size = font_size
                self.label.text = text
                self.label._label.refresh()
                text_width = self.label._label._internal_size[0]
            self.font_size = self.label.font_size
        else:
            font_size = self.label.font_size
            while text_width < self.width:
                font_size = self.label.font_size
                if font_size >= sp(CPanel.MaxTextSize):
                    break
                self.label.font_size = font_size + sp(20)
                self.label.text = text
                self.label._label.refresh()
                text_width = self.label._label._internal_size[0]
            self.font_size = font_size

    def get_sign_and_number(self, num: str = NO_VALUE) -> None:
        if num == NO_VALUE:
            n = self.history.pop()
            if n == NO_VALUE:
                self.sign = ""
                self.number = "0"
                return
            self.sign = "-" if n.startswith("-") else ""
            self.number = n[1:] if n.startswith("-") else n
        else:
            self.sign = "-" if num.startswith("-") else ""
            self.number = num[1:] if num.startswith("-") else num

    def to_thousand_sep(self, number: str) -> str:
        if len(number) > 3:
            if bt.Numbers.text_dot in number:
                n1 = number.split(bt.Numbers.text_dot)[0]
                n2 = bt.Numbers.text_dot+number.split(bt.Numbers.text_dot)[1]
            else:
                n1 = number
                n2 = ""

            step = 3
            n1_len = len(n1)
            if n1_len % 3 != 0:
                n1 = ','.join(
                        [n1[(n1_len-(i+1)*step) if (n1_len-(i+1)*step) >= 0 else 0:n1_len-i*step]
                            for i in range(0, n1_len//3+1)][::-1]
                    )
            else:
                n1 = ','.join(
                        [n1[(n1_len-(i+1)*step) if (n1_len-(i+1)*step) >= 0 else 0:n1_len-i*step]
                            for i in range(0, n1_len//3)][::-1]
                    )

            number = n1 + n2

        return number
