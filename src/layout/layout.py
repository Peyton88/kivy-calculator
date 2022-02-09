'''
    layout.py:
        Calculator layout

    Author: Peyton Fang
    Date: 2021.02.08

'''

__author__ = 'Peyton Fang'
__version__ = "1.0"
__email__ = "peyton888@gmail.com"


from kivy.uix.boxlayout import BoxLayout
from components.button import CButton
from components.panel import CPanel
from common.defines import BtnLayout


class CalculatorLayout(BoxLayout):

    def __init__(self):
        super().__init__(orientation='vertical')
        self.layout_rows = []
        self.btn_rows = []
        self.textpanel = CPanel.create()
        self.button_create()
        for row in self.btn_rows:
            layout_row = BoxLayout(orientation='horizontal', padding=2, spacing=4)
            for btn in row:
                layout_row.add_widget(btn)
            self.layout_rows.append(layout_row)

        self.add_widget(self.textpanel)
        for row in self.layout_rows:
            self.add_widget(row)

    def button_create(self) -> None:
        for row in BtnLayout.layout:
            btn_row = [CButton(**btn) for btn in row]
            self.btn_rows.append(btn_row)

    def on_window_size_changed(self, *args):
        '''
            In case of phone rotation, check if text exceed panel again
        '''
        _, window_width, _ = args
        self.textpanel.width = window_width
        self.textpanel.check_if_text_exceed_panel(self.textpanel.text)
