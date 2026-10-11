from calculator import Calculator
import math

class ScientificCalculator(Calculator):

    def __init__(self, num, angle_mode = "DEG"):
        super().__init__(num)
        self.angle_mode = angle_mode

    def sqrt(self):
        # returning object so that we can chaining
        if self.num < 0:
            raise ValueError("Square root of negative number is not real")
        return ScientificCalculator(math.sqrt(self.num))

    def set_angle_mode(self, mode):
        mode = mode.upper()

        if mode not in ("DEG", "RAD", "GRAD"):
            raise ValueError("Angle mode must be DEG, RAD or GRAD")

        self.angle_mode = mode

    def _to_radians(self):
        if self.angle_mode == "DEG":
            return math.radians(self.num)

        elif self.angle_mode == "RAD":
            return self.num

        elif self.angle_mode == 'GRAD':
            return self.num * math.pi / 200

        else:
            raise ValueError("Invalid angle mode")


    def sin(self):
        return ScientificCalculator(
            math.sin(self._to_radians()),
            self.angle_mode
        )

    def cos(self):
        return ScientificCalculator(
            math.cos(self._to_radians()),
            self.angle_mode
        )

    def tan(self):
        return ScientificCalculator(
            math.tan(self._to_radians()),
            self.angle_mode
        )

    def _from_radians(self, value):
        if self.angle_mode == "DEG":
            return math.degrees(value)

        elif self.angle_mode == "RAD":
            return value

        elif self.angle_mode == "GRAD":
            return value * 200 / math.pi

        else:
            raise ValueError("Invalid angle mode")

    def asin(self):
        result = math.asin(self.num)

        return ScientificCalculator(
            self._from_radians(result),
            self.angle_mode
        )

    def acos(self):
        result = math.acos(self.num)

        return ScientificCalculator(
            self._from_radians(result),
            self.angle_mode
        )

    def atan(self):
        result = math.atan(self.num)

        return ScientificCalculator(
            self._from_radians(result),
            self.angle_mode
        )


    def ln(self):
        if self.num <= 0:
            raise ValueError("ln is defined only for positive numbers")
        return ScientificCalculator(math.log(self.num))

    def log10(self):
        if self.num <= 0:
            raise ValueError("log10 is defined only for positive numbers")
        return ScientificCalculator(math.log10(self.num))

    def log(self, base = 10):
        if self.num <= 0:
            raise ValueError("Logarithm is defined only for positive numbers")

        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")
        return ScientificCalculator(math.log(self.num, base))

    def exp(self):
        return ScientificCalculator(math.exp(self.num))


    def factorial(self):
        if self.num < 0 or self.num != int(self.num):
            raise ValueError("Factorial is defined only non-negative integers")

        return ScientificCalculator(math.factorial(int(self.num)))

    def percent(self):
        return ScientificCalculator(self.num / 100)


    def square(self):
        return ScientificCalculator(
            self.num ** 2,
            self.angle_mode
        )

    def cube(self):
        return ScientificCalculator(
            self.num ** 3,
            self.angle_mode
        )

    def reciprocal(self):
        if self.num == 0:
            raise ZeroDivisionError("Cannot take reciprocal of zero")

        return ScientificCalculator(
            1 / self.num,
            self.angle_mode
        )


    def sinh(self):
        return ScientificCalculator(
            math.sinh(self.num),
            self.angle_mode
        )

    def cosh(self):
        return ScientificCalculator(
            math.cosh(self.num),
            self.angle_mode
        )

    def tanh(self):
        return ScientificCalculator(
            math.tanh(self.num),
            self.angle_mode
        )

    def asinh(self):
        return ScientificCalculator(
            math.asinh(self.num),
            self.angle_mode
        )

    def acosh(self):

        if self.num < 1:
            raise ValueError("acosh is defined only for x >= 1")
        return ScientificCalculator(
            math.acosh(self.num),
            self.angle_mode
        )

    def atanh(self):
        if self.num <= -1 or self.num >= 1:
            raise ValueError("atanh is defined only for -1 < x < 1")
        return ScientificCalculator(
            math.atanh(self.num),
            self.angle_mode
        )

    def ncr(self, r):
        n = self.num
        if n < 0 or r < 0:
            raise ValueError("n and r must be non-negative")

        if n != int(n) or r != int(r):
            raise ValueError("n and r must be integer")

        n = int(n)
        r = int(r)

        if r > n:
            raise ValueError("r can not be greater than n")

        return ScientificCalculator(
            math.comb(n, r),
            self.angle_mode
        )


    def npr(self, r):
        n = self.num
        if n < 0 or r < 0:
            raise ValueError("n and r must be non-negative")

        if n != int(n) or r != int(r):
            raise ValueError("n and r must be integer")

        n = int(n)
        r = int(r)

        if r > n:
            raise ValueError("r can not be greater than n")

        return ScientificCalculator(
            math.factorial(n) // math.factorial(n - r),
            self.angle_mode
        )
