'''
    defines.py:
        Define all text of buttons and layout of buttons on calculator

    Author: Peyton Fang
    Date: 2021.02.08

'''

__author__ = 'Peyton Fang'
__version__ = "1.0"
__copyright__ = "Copyright (C) 2021 Peyton Fang"
__email__ = "peyton888@gmail.com"


NO_VALUE = object()


class BtnText(object):
    class Numbers(object):
        text_0 = "0"
        text_1 = "1"
        text_2 = "2"
        text_3 = "3"
        text_4 = "4"
        text_5 = "5"
        text_6 = "6"
        text_7 = "7"
        text_8 = "8"
        text_9 = "9"
        text_dot = "."

    class Operators(object):
        text_plus = "+"
        text_minus = "-"
        text_multiply = "x"
        text_divide = "÷"
        text_equal = "="
        text_percent = "%"
        text_sign = "+/-"
        text_ac = "AC"


class BtnLayout(object):
    '''
    Layout:
        AC +/-  %   ÷
        7   8   9   x
        4   5   6   -
        1   2   3   +
           0    .   =
    '''
    layout = [
        [
            dict(
                text=BtnText.Operators.text_ac,
                font_size="30sp",
                background_normal='colors/red_normal.png',
                background_down='colors/red_down.png'
            ),
            dict(
                text=BtnText.Operators.text_sign,
                font_size="30sp",
                background_normal='colors/blue_normal.png',
                background_down='colors/blue_down.png'
            ),
            dict(
                text=BtnText.Operators.text_percent,
                font_size="30sp",
                background_normal='colors/blue_normal.png',
                background_down='colors/blue_down.png'
            ),
            dict(
                text=BtnText.Operators.text_divide,
                font_size="30sp",
                background_normal='colors/yellow_normal.png',
                background_down='colors/yellow_down.png'
            )
        ],
        [
            dict(
                text=BtnText.Numbers.text_7,
                font_size="30sp",
                background_normal='colors/gray_normal.png',
                background_down='colors/gray_down.png'),
            dict(
                text=BtnText.Numbers.text_8,
                font_size="30sp",
                background_normal='colors/gray_normal.png',
                background_down='colors/gray_down.png'),
            dict(
                text=BtnText.Numbers.text_9,
                font_size="30sp",
                background_normal='colors/gray_normal.png',
                background_down='colors/gray_down.png'),
            dict(
                text=BtnText.Operators.text_multiply,
                font_size="30sp",
                background_normal='colors/yellow_normal.png',
                background_down='colors/yellow_down.png')
        ],
        [
            dict(
                text=BtnText.Numbers.text_4,
                font_size="30sp",
                background_normal='colors/gray_normal.png',
                background_down='colors/gray_down.png'),
            dict(
                text=BtnText.Numbers.text_5,
                font_size="30sp",
                background_normal='colors/gray_normal.png',
                background_down='colors/gray_down.png'),
            dict(
                text=BtnText.Numbers.text_6,
                font_size="30sp",
                background_normal='colors/gray_normal.png',
                background_down='colors/gray_down.png'),
            dict(
                text=BtnText.Operators.text_minus,
                font_size="30sp",
                background_normal='colors/yellow_normal.png',
                background_down='colors/yellow_down.png')
        ],
        [
            dict(
                text=BtnText.Numbers.text_1,
                font_size="30sp",
                background_normal='colors/gray_normal.png',
                background_down='colors/gray_down.png'),
            dict(
                text=BtnText.Numbers.text_2,
                font_size="30sp",
                background_normal='colors/gray_normal.png',
                background_down='colors/gray_down.png'),
            dict(
                text=BtnText.Numbers.text_3,
                font_size="30sp",
                background_normal='colors/gray_normal.png',
                background_down='colors/gray_down.png'),
            dict(
                text=BtnText.Operators.text_plus,
                font_size="30sp",
                background_normal='colors/yellow_normal.png',
                background_down='colors/yellow_down.png')
        ],
        [
            dict(
                text=BtnText.Numbers.text_0,
                size_hint=(2, 1),
                font_size="30sp",
                background_normal='colors/gray_normal.png',
                background_down='colors/gray_down.png'),
            dict(
                text=BtnText.Numbers.text_dot,
                font_size="30sp",
                background_normal='colors/gray_normal.png',
                background_down='colors/gray_down.png'),
            dict(
                text=BtnText.Operators.text_equal,
                font_size="30sp",
                background_normal='colors/yellow_normal.png',
                background_down='colors/yellow_down.png')
        ]
    ]
