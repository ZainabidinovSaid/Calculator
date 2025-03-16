from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from calculator import Calculator

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the .ui file dynamically
        uic.loadUi("calculator.ui", self)

        # Initialize the calculator logic
        self.calculator = Calculator()

        # Connect buttons to functions
        self.bind_buttons()

    def bind_buttons(self):
        """Connects UI buttons to their respective functions."""
        self.button0.clicked.connect(lambda: self.on_button_click("0"))
        self.button1.clicked.connect(lambda: self.on_button_click("1"))
        self.button2.clicked.connect(lambda: self.on_button_click("2"))
        self.button3.clicked.connect(lambda: self.on_button_click("3"))
        self.button4.clicked.connect(lambda: self.on_button_click("4"))
        self.button5.clicked.connect(lambda: self.on_button_click("5"))
        self.button6.clicked.connect(lambda: self.on_button_click("6"))
        self.button7.clicked.connect(lambda: self.on_button_click("7"))
        self.button8.clicked.connect(lambda: self.on_button_click("8"))
        self.button9.clicked.connect(lambda: self.on_button_click("9"))

        self.button_plus.clicked.connect(lambda: self.on_button_click("+"))
        self.button_minus.clicked.connect(lambda: self.on_button_click("-"))
        self.button_mult.clicked.connect(lambda: self.on_button_click("*"))
        self.button_div.clicked.connect(lambda: self.on_button_click("/"))

        self.button_clear.clicked.connect(self.clear_input)
        self.button_backspace.clicked.connect(self.remove_last_character)
        self.button_equal.clicked.connect(self.calculate_result)
        self.button_toggle_sign.clicked.connect(self.toggle_sign)

    def on_button_click(self, button_text):
        self.calculator.add_to_expression(button_text)
        self.update_display()

    def clear_input(self):
        self.calculator.clear_expression()
        self.update_display()

    def remove_last_character(self):
        self.calculator.remove_last_character()
        self.update_display()

    def calculate_result(self):
        result = self.calculator.calculate()
        self.input.setText(str(result))

    def toggle_sign(self):
        self.calculator.toggle_sign()
        self.update_display()

    def update_display(self):
        self.input.setText(self.calculator.get_expression())