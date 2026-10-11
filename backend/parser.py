from scientific_calculator import ScientificCalculator
from calculator import Calculator

class Parser:

    def __init__(self, tokens, function_handler, value_resolver):
        self.tokens = tokens
        self.position = 0
        self.function_handler = function_handler
        self.value_resolver = value_resolver


    def current_token(self):
        return self.tokens[self.position]

    def advance(self):
        self.position += 1


    def parse_power(self):
        result = self.parse_postfix()

        if self.position < len(self.tokens):
            token = self.current_token()

            if token in ("^", "**"):
                self.advance()
                result = result ** self.parse_power()

        return result


    def starts_factor(self, token):

        if isinstance(token, float):
            return True

        if token == "(":
            return True

        if isinstance(token, str):
            return token not in {
                "+",
                "-",
                "*",
                "/",
                "//",
                "%",
                "^",
                "**",
                "!",
                ")",
                ","
            }

        return False


    def parse_postfix(self):

        result = self.parse_factor()

        while self.position < len(self.tokens):

            token = self.current_token()

            if token == "!":
                self.advance()
                result = ScientificCalculator(result.num).factorial()

            elif token == "%":
                self.advance()
                result = ScientificCalculator(result.num).percent()

            else:
                break

        return result

    def parse_factor(self):

        token = self.current_token()

        # Unary +
        if token == "+":
            self.advance()
            return +self.parse_factor()

        # Unary -
        if token == "-":
            self.advance()
            return -self.parse_factor()

        # Number
        if isinstance(token, float):
            self.advance()
            return Calculator(token)

        # Parentheses
        if token == "(":
            self.advance()

            result = self.parse_expression()

            if (
                self.position >= len(self.tokens)
                or self.current_token() != ")"
            ):
                raise ValueError("Missing closing parenthesis")

            self.advance()

            return result

        # Identifier or function
        if isinstance(token, str):
            # Normal identifier / constant
            if (
                self.position + 1 >= len(self.tokens)
                or self.tokens[self.position + 1] != "("
            ):
                self.advance()
                return self.value_resolver(token)

            function_name = token
            self.advance()  # function name

            # Expect (
            if (
                self.position >= len(self.tokens)
                or self.current_token() != "("
            ):
                raise ValueError(
                    f"Expected '(' after function '{function_name}'"
                )

            self.advance()  # (

            # Empty argument: sin()
            if (
                self.position >= len(self.tokens)
                or self.current_token() == ")"
            ):
                raise ValueError(
                    f"Function '{function_name}' requires an argument"
                )

            # First argument
            first_argument = self.parse_expression()

            # End of expression before )
            if self.position >= len(self.tokens):
                raise ValueError(
                    f"Missing ')' after function '{function_name}'"
                )

            # One argument: sin(30)
            if self.current_token() == ")":
                self.advance()

                return self.function_handler(
                    function_name,
                    first_argument
                )

            # Two arguments
            if self.current_token() == ",":
                self.advance()

                # Missing second argument: ncr(5,)
                if (
                    self.position >= len(self.tokens)
                    or self.current_token() == ")"
                ):
                    raise ValueError(
                        f"Missing second argument in '{function_name}'"
                    )

                second_argument = self.parse_expression()

                # Missing )
                if self.position >= len(self.tokens):
                    raise ValueError(
                        f"Missing ')' after function '{function_name}'"
                    )

                # Extra argument: ncr(5,2,3)
                if self.current_token() != ")":
                    raise ValueError(
                        f"Too many arguments for function '{function_name}'"
                    )

                self.advance()

                return self.function_handler(
                    function_name,
                    first_argument,
                    second_argument
                )

            raise ValueError(
                f"Expected ',' or ')' after first argument "
                f"of '{function_name}'"
            )

        raise ValueError(f"Unexpected token: {token}")



    def parse_term(self):
        result = self.parse_power()

        while self.position < len(self.tokens):
            token = self.current_token()

            if token == "*":
                self.advance()
                result *= self.parse_power()

            elif token == "/":
                self.advance()
                result /= self.parse_power()

            elif token == "//":
                self.advance()
                result //= self.parse_power()

            elif token == "%":
                self.advance()
                result %= self.parse_power()

            elif self.starts_factor(token):
                # implicit multiplication
                result *= self.parse_power()

            else:
                break

        return result

    def parse_expression(self):
        result = self.parse_term()

        while self.position < len(self.tokens):
            token = self.current_token()

            if token == "+":
                self.advance()
                result += self.parse_term()

            elif token == "-":
                self.advance()
                result -= self.parse_term()

            else:
                break

        return result



    def parse(self):
        if not self.tokens:
            raise ValueError("Expression cannot be empty")

        result = self.parse_expression()

        if self.position != len(self.tokens):
            raise ValueError(
                f"Unexpected token: {self.current_token()}"
            )

        return result
