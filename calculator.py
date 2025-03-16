# calculator.py (Model)
class Calculator:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, char: str):
        self.expression += char

    def remove_last_character(self):
        self.expression = self.expression[:-1]

    def clear_expression(self):
        self.expression = ""

    def toggle_sign(self):
        if self.expression:
            tokens = self.expression.split()  # Splitting by spaces to handle multi-digit numbers
            last_token = tokens[-1]

            if last_token.lstrip("-").isdigit():  # Check if it's a number
                if last_token.startswith("-"):
                    tokens[-1] = last_token[1:]  # Remove '-' if negative
                else:
                    tokens[-1] = "-" + last_token  # Add '-' if positive

                self.expression = " ".join(tokens)  # Reconstruct the expression

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception:
            return "Error: Invalid expression"

    def get_expression(self):
        return self.expression
