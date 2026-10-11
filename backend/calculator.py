import math

class Calculator:
    def __init__(self, num):
        self.num = num

    # user friendlt
    def __str__(self):
        return str(self.num)

    # developer/ debuging
    def __repr__(self):
        return f"Calculator({self.num!r})"

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.num + other.num)
        return Calculator(self.num + other)

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.num - other.num)
        return Calculator(self.num - other)

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.num * other.num)
        return Calculator(self.num * other)

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            if other.num == 0:
                raise ZeroDivisionError("Can not divide by zero")
            return Calculator(self.num / other.num)

        if other == 0:
            raise ZeroDivisionError("Can not divide by zero")
        return Calculator(self.num / other)

    def __floordiv__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.num // other.num)
        return Calculator(self.num // other)

    def __pow__(self,other):
        if isinstance(other, Calculator):
            if self.num == 0 and other.num < 0:
                raise ZeroDivisionError("0 can not be raised to a negative power")

            if self.num < 0 and not float(other.num).is_integer():
                raise ValueError("Negative number can not have a fractional power in real mode")
            return Calculator(self.num ** other.num)

        if self.num == 0 and other < 0:
                raise ZeroDivisionError("0 can not be raised to a negative power")
        if self.num < 0 and not float(other).is_integer():
                raise ValueError("Negative number can not have a fractional power in real mode")
        return Calculator(self.num ** other)

    def __mod__(self, other):
        if isinstance(other, Calculator):
            if other.num == 0:
                raise ZeroDivisionError("Modulo by zero is not allowed")
            return Calculator(self.num % other.num)
        if other == 0:
            raise ZeroDivisionError("Modulo by zero is not allowed")
        return Calculator(self.num % other)

    def __radd__(self, other):
        return Calculator(other + self.num)

    def __rmul__(self, other):
        return Calculator(other * self.num)

    def __rsub__(self, other):
        return Calculator(other - self.num)

    def __rtruediv__(self, other):
        if self.num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Calculator(other / self.num)

    def __rfloordiv__(self, other):
        if self.num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return Calculator(other // self.num)

    def __rpow__(self, other):
        if other == 0 and self.num < 0:
            raise ZeroDivisionError("0 can not be raised to a negative power")
        if other < 0 and not float(self.num).is_integer():
                raise ValueError("Negative number can not have a fractional power in real mode")
        return Calculator(other ** self.num)

    def __rmod__(self, other):
        if self.num == 0:
            raise ZeroDivisionError("Modulo by zero is not allowed")
        return Calculator(other % self.num)

    # equal to
    def __eq__(self, other):
        if isinstance(other, Calculator):
            return self.num == other.num
        return self.num == other

    # not equal to
    def __ne__(self, other):
        if isinstance(other, Calculator):
            return self.num != other.num
        return self.num != other

    # less than
    def __lt__(self, other):
        if isinstance(other, Calculator):
            return self.num < other.num
        return self.num < other

    # greater than
    def __gt__(self, other):
        if isinstance(other, Calculator):
            return self.num > other.num
        return self.num > other

    # less than or equal to
    def __le__(self, other):
        if isinstance(other, Calculator):
            return self.num <= other.num
        return self.num <= other

    # greater than or equal to
    def __ge__(self, other):
        if isinstance(other, Calculator):
            return self.num >= other.num
        return self.num >= other

    def __neg__(self):
        return Calculator(-self.num)

    def __pos__(self):
        return Calculator(+self.num)

    def __abs__(self):
        return Calculator(abs(self.num))


    # conversion methods
    def __int__(self):
        return int(self.num)

    def __float__(self):
        return float(self.num)

    def __bool__(self):
        return bool(self.num)

    def __round__(self, ndigits = 0):
        return Calculator(round(self.num, ndigits))

    def __floor__(self):
        return math.floor(self.num)

    def __ceil__(self):
        return math.ceil(self.num)


# arithmetic operation --> return Calculator object
# comparison operation --> return boolean object
