from scientific_calculator import ScientificCalculator
from tokenizer import Tokenizer
from calculator import Calculator
from parser import Parser
import math

class CalculatorEngine:

    def __init__(self):
        self.current = ScientificCalculator(0)
        self.ans = None
        self.history = []
        self.angle_mode = "DEG"
        self.memory = ScientificCalculator(0)

    def set_angle_mode(self, mode):
        mode = mode.upper()

        if mode not in ("DEG", "RAD", "GRAD"):
            raise ValueError("Angle must be in DEG, RAG or GRAD")

        self.angle_mode = mode

    def memory_add(self):
        self.memory = ScientificCalculator(
            self.memory.num + self.current.num,
            self.angle_mode
        )

        return self.memory

    def memory_subtract(self):
        self.memory = ScientificCalculator(
            self.memory.num - self.current.num,
            self.angle_mode
        )

        return self.memory

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = ScientificCalculator(0, self.angle_mode)

    def show_history(self):
        for item in self.history:
            print(f"{item["expression"]} = {item["result"]}")

    def add_to_history(self, expression, result):
        self.history.append({
            "expression": expression,
            "result": result
        })

    def clear_history(self):
        self.history.clear()


    def delete_history(self, index):
        if index < 0 or index >= len(self.history):
            raise IndexError("Invalid history index")

        self.history.pop(index)

    def apply_function(self, name, value, second_value = None):

        if isinstance(value, Calculator):
            value = value.num

        if isinstance(second_value, Calculator):
            second_value = second_value.num

        cal = ScientificCalculator(value, self.angle_mode)

        if name == "sqrt":
            return cal.sqrt()
        elif name == "sin":
            return cal.sin()
        elif name == "cos":
            return cal.cos()
        elif name == "tan":
            return cal.tan()
        elif name == "asin":
            return cal.asin()
        elif name == "acos":
            return cal.acos()
        elif name == "atan":
            return cal.atan()
        elif name == "ln":
            return cal.ln()
        elif name == "log":
            if second_value is None:
                return cal.log()

            return ScientificCalculator(
                math.log(second_value, value),
                self.angle_mode
            )
        elif name == "log10":
            return cal.log10()
        elif name == "exp":
            return cal.exp()
        elif name == 'factorial':
            return cal.factorial()
        elif name == "square":
            return cal.square()
        elif name == "cube":
            return cal.cube()
        elif name == "reciprocal":
            return cal.reciprocal()
        elif name == "sinh":
            return cal.sinh()
        elif name == "cosh":
            return cal.cosh()
        elif name == "tanh":
            return cal.tanh()
        elif name == "asinh":
            return cal.asinh()

        elif name == "acosh":
            return cal.acosh()

        elif name == "atanh":
            return cal.atanh()

        elif name == "ncr":
            return cal.ncr(second_value)


        elif name == "npr":
            return cal.npr(second_value)

        else:
            raise ValueError(f"Unknown function : {name}")


    def resolve_value(self, name):

        if name == "Ans":

            if self.ans is None:
                raise ValueError("Ans is not available yet")

            return self.ans

        elif name == "M":
            return self.memory

        elif name in ("pi",  "π"):
            return Calculator(math.pi)

        elif name == "e":
            return Calculator(math.e)

        raise ValueError(f"Unknown identifier: {name}")

    def evaluate(self, expression, angle_mode = None):

        if angle_mode is not None:
            self.angle_mode = angle_mode

        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize(expression)

        parser = Parser(
            tokens,
            self.apply_function,
            self.resolve_value
        )

        result = parser.parse()

         # Extract the actual numeric value
        if isinstance(result, Calculator):
            value = result.num
        else:
            value = result

        value = round(value, 12)

        self.current = ScientificCalculator(value, self.angle_mode)
        self.ans = self.current

        self.add_to_history(
            expression, value
        )

        return self.current

    def calculate(self, a, operator, b):
        if operator == "+":
            result = a + b

        elif operator == "-":
            result = a - b

        elif operator == "*":
            result = a * b

        elif operator == "/":
            result = a / b

        elif operator == "//":
            result = a // b

        else:
            raise ValueError("Invalid operator")

        self.current = ScientificCalculator(result)
        self.ans = self.current

        self.add_to_history(
            f"{a} {operator} {b}",
            result
        )

        return self.current
