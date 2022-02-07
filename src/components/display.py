'''
    display.py:
        Define display component to use

    Author: Peyton Fang
    Date: 2021.02.08

'''

__author__ = 'Peyton Fang'
__version__ = "1.0"
__email__ = "peyton888@gmail.com"


from kivy.uix.label import Label
from components.observer import Subscriber


class CDisplay(Label, Subscriber):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
