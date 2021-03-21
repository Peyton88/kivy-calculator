'''
    control.py:
        Define control component to use

    Author: Peyton Fang
    Date: 2021.02.08

'''

__author__ = 'Peyton Fang'
__version__ = "1.0"
__copyright__ = "Copyright (C) 2021 Peyton Fang"
__email__ = "peyton888@gmail.com"


from components.observer import Topic
from components.observer import Subscriber


class CControl(Topic, Subscriber):

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.observers = []

    def addSubscriber(self, observer: Subscriber) -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def removeSubscriber(self, observer: Subscriber) -> None:
        if observer in self.observers:
            self.observers.pop(observer)

    def notifySubscriber(self, data):
        for o in self.observers:
            o.update(data)
