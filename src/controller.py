'''
    controller.py:
        Process all button event and related calculation.
        Update results to panel.

    Author: Peyton Fang
    Date: 2021.02.08

'''

__author__ = 'Peyton Fang'
__version__ = "1.0"
__copyright__ = "Copyright (C) 2021 Peyton Fang"
__email__ = "peyton888@gmail.com"


from components.control import CControl
from common.defines import BtnText as bt
from common.defines import NO_VALUE


class Controller(CControl):
    MaxTextSize = 70
    MinTextSize = 10
    MaxLength = 12

    def __init__(self):
        super().__init__()
        self.sign = ""
        self.number = "0"
        self.do_operation = {
            bt.Operators.text_ac: self.op_symbol,
            bt.Operators.text_percent: self.op_symbol,
            bt.Operators.text_sign: self.op_symbol,
            bt.Operators.text_equal: self.op_symbol,
            bt.Operators.text_plus: self.op_arithmetic,
            bt.Operators.text_minus: self.op_arithmetic,
            bt.Operators.text_multiply: self.op_arithmetic,
            bt.Operators.text_divide: self.op_arithmetic,
        }
        self.history = [self.sign+self.number]
        self.op = NO_VALUE
        self.error = False

    @staticmethod
    def create():
        C = Controller()
        return C

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

    def is_max_number(self, number: str) -> bool:
        number = str(number)
        number = number[1:] if number.startswith("-") else number
        if bt.Numbers.text_dot in number:
            n1 = number.split(bt.Numbers.text_dot)[0]
            n2 = number.split(bt.Numbers.text_dot)[1]
            if len(n1) + len(n2) >= Controller.MaxLength:
                return True
        else:
            if len(number) >= Controller.MaxLength:
                return True

        return False

    def update(self, data: str) -> None:
        if data in bt.Numbers.__dict__.values():
            self.update_number(data)
        elif data in bt.Operators.__dict__.values():
            self.update_operator(data)
        else:
            print(f"Unsupport command \"{data}\"")

        if self.error is True:
            self.notifySubscriber("Error")
            self.error = False
        else:
            self.notifySubscriber(self.sign + self.number)

    def update_number(self, data: str) -> None:
        self.get_sign_and_number()

        is_max = self.is_max_number(self.number)
        if is_max is True:
            self.history.append(self.sign+self.number)
            return

        if data == bt.Numbers.text_dot:
            if data in self.number:
                pass
            else:
                self.number = self.number + data
        else:
            if self.number == bt.Numbers.text_0:
                self.number = data
            else:
                self.number = self.number + data
        self.history.append(self.sign+self.number)

    def update_operator(self, data: str) -> None:
        if self.number.endswith(bt.Numbers.text_dot):
            self.number = self.number[:len(self.number)-1]
        try:
            self.do_operation[data](data)
        except ZeroDivisionError:
            self.do_ac()
            self.error = True

    def do_ac(self) -> None:
        self.sign = ""
        self.number = "0"
        self.op = NO_VALUE
        self.history.clear()
        self.history.append(self.sign+self.number)

    def do_percent(self) -> None:
        self.get_sign_and_number()
        if self.number == bt.Numbers.text_0:
            self.sign = ""
        elif bt.Numbers.text_dot in self.number:
            r = len(self.number) - self.number.find(bt.Numbers.text_dot) + 1
            self.number = str(round(float(self.number)/100, r))  # To fix case like 89.07/100 = 0.8906999999999999
        else:
            self.number = str(int(self.number)/100)
        self.history.append(self.sign+self.number)

    def do_sign(self) -> None:
        self.get_sign_and_number()
        self.sign = "" if self.sign == "-" else "-"
        self.history.append(self.sign+self.number)

    def do_equal(self) -> None:
        if len(self.history) < 2 or self.history[-1] == NO_VALUE:
            self.op = NO_VALUE
            return

        num2 = self.history.pop()
        num1 = self.history.pop()
        if bt.Numbers.text_dot in num1:
            num1 = float(num1)
        else:
            num1 = int(num1)
        if bt.Numbers.text_dot in num2:
            num2 = float(num2)
        else:
            num2 = int(num2)

        if self.op == bt.Operators.text_plus:
            r = self.get_round_for_plus_minus(num1, num2)
            num = round(num1 + num2, r)
        elif self.op == bt.Operators.text_multiply:
            num = num1 * num2
        elif self.op == bt.Operators.text_divide:
            num = num1 / num2
        else:
            r = self.get_round_for_plus_minus(num1, num2)
            num = round(num1 - num2, r)

        num_str = str(num)
        num_str = self.remove_dot_zero(num_str)

        self.get_sign_and_number(num_str)
        self.history.append(self.sign+self.number)
        self.op = NO_VALUE

    def op_symbol(self, symbol: str) -> None:
        do_symbol = {
            bt.Operators.text_ac: self.do_ac,
            bt.Operators.text_percent: self.do_percent,
            bt.Operators.text_sign: self.do_sign,
            bt.Operators.text_equal: self.do_equal,
        }
        do_symbol[symbol]()

    def op_arithmetic(self, operation: str) -> None:
        if self.op != NO_VALUE and self.history[-1] != NO_VALUE:
            self.do_equal()

        self.op = operation
        if self.history[-1] != NO_VALUE:
            self.history.append(NO_VALUE)

    def remove_dot_zero(self, num_str) -> str:
        if bt.Numbers.text_dot in num_str:
            if int(num_str.split(bt.Numbers.text_dot)[1]) == 0:
                num_str = num_str.split(bt.Numbers.text_dot)[0]
        return num_str

    def get_round_for_plus_minus(self, num1: int, num2: int) -> int:  # To fix case like 89.99-0.2 = 89.78999999999999
        num1_str = str(num1)
        num2_str = str(num2)
        r1 = 0
        r2 = 0
        if bt.Numbers.text_dot in str(num1_str):
            r1 = len(num1_str) - num1_str.find(bt.Numbers.text_dot) - 1
        if bt.Numbers.text_dot in str(num2_str):
            r2 = len(num2_str) - num2_str.find(bt.Numbers.text_dot) - 1

        return max(r1, r2)
