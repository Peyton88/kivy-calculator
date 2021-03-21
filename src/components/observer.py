'''
    observer.py:
        Interfaces define

    Author: Peyton Fang
    Date: 2021.02.08

'''

__author__ = 'Peyton Fang'
__version__ = "1.0"
__copyright__ = "Copyright (C) 2021 Peyton Fang"
__email__ = "peyton888@gmail.com"


class Subscriber:

    def __init__(self):
        pass

    def update(self, data: str) -> None:
        pass


class Topic:

    def __init__(self):
        pass

    def addSubscriber(self, subscriber: Subscriber) -> None:
        pass

    def removeSubscriber(self, subscriber: Subscriber) -> None:
        pass

    def notifySubscriber(self) -> None:
        pass
