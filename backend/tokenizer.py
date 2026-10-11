class Tokenizer:

    def tokenize(self, expression):

        tokens = []
        number = ""
        identifier = ""

        i = 0

        while i < len(expression):

            char = expression[i]

            # -------------------------
            # Number
            # -------------------------
            if char.isdigit() or char == ".":

                if identifier:
                    tokens.append(identifier)
                    identifier = ""

                number += char
                i += 1

            # -------------------------
            # Scientific notation
            # -------------------------
            elif char in "eE" and number:

                exponent_index = i + 1

                # Optional + or -
                if (
                    exponent_index < len(expression)
                    and expression[exponent_index] in "+-"
                ):
                    exponent_index += 1

                # Valid scientific notation
                if (
                    exponent_index < len(expression)
                    and expression[exponent_index].isdigit()
                ):
                    number += char
                    i += 1

                    if expression[i] in "+-":
                        number += expression[i]
                        i += 1

                    while (
                        i < len(expression)
                        and expression[i].isdigit()
                    ):
                        number += expression[i]
                        i += 1

                else:
                    # Finish the current number.
                    # Do NOT consume e.
                    tokens.append(float(number))
                    number = ""
                    continue

            # -------------------------
            # Identifier
            # -------------------------
            elif char.isalpha() or char == "π":

                if number:
                    tokens.append(float(number))
                    number = ""

                identifier += char
                i += 1

            # -------------------------
            # Operators
            # -------------------------
            elif char in "+-/*^()%!,":

                if number:
                    tokens.append(float(number))
                    number = ""

                if identifier:
                    tokens.append(identifier)
                    identifier = ""

                # Two-character operators
                if i + 1 < len(expression):

                    two_char = expression[i:i+2]

                    if two_char in ("//", "**"):
                        tokens.append(two_char)
                        i += 2
                        continue

                tokens.append(char)
                i += 1

            # -------------------------
            # Space
            # -------------------------
            elif char == " ":

                i += 1

            else:
                raise ValueError(
                    f"Invalid character: {char}"
                )

        if number:
            tokens.append(float(number))

        if identifier:
            tokens.append(identifier)

        return tokens
