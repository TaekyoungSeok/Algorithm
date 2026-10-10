class Infix2Postfix:
    def __init__(self):
        self.stack = []
        self.output = []

    def tokenization(self, expression):
        token = []
        number = ""

        for char in expression:
            if char in "0123456789.":
                number += char

            else:
                if number:
                    token.append(number)
                    number = ""

                if char.isspace():
                    continue

                elif char in "+-*/^()":
                    token.append(char)

                else:
                    raise ValueError(f"지원하지 않는 문자 : {char}")

        if number:
            token.append(number)

        return token

    def is_operand(self, token):
        try:
            float(token)
            return True
        
        except ValueError:
            return False
        
    def precedence(self, operator):
        if operator in ("+", "-"):
            return 1
        
        elif operator in ("*", "/"):
            return 2
        
        elif operator == "^":
            return 3
        
        else:
            return 0
    
    def infix_to_postfix(self, expression):
        self.stack = []
        self.output = []

        tokens = self.tokenization(expression)

        for token in tokens:
            if self.is_operand(token):
                self.output.append(token)

            elif token == "(":
                self.stack.append(token)

            elif token == ")":
                while self.stack and (self.stack[-1] != "("):
                    self.output.append(self.stack.pop())

                if not self.stack:
                    raise ValueError("괄호가 맞지 않습니다.")

                self.stack.pop()

            elif token in ("+", "-", "*", "/", "^"):
                while self.stack and self.stack[-1] != "(":
                    top_priority = self.precedence(self.stack[-1])
                    current_priority = self.precedence(token)

                    if (top_priority >= current_priority) and (token != "^"):
                        self.output.append(self.stack.pop())

                    else:
                        break

                self.stack.append(token)

            else:
                raise ValueError(f"잘못된 토큰 : {token}")

        while self.stack:
            operator = self.stack.pop()

            if operator == "(":
                raise ValueError("괄호가 맞지 않습니다.")

            self.output.append(operator)

        return " ".join(self.output)
    
def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token in ("+", "-", "*", "/", "^"):
            if len(stack) < 2:
                raise ValueError("연산에 필요한 숫자가 부족합니다.")

            right = stack.pop()
            left = stack.pop()

            if token == "+":
                result = left + right

            elif token == "-":
                result = left - right

            elif token == "*":
                result = left * right

            elif token == "/":
                result = left / right

            elif token == "^":
                result = left ** right

            stack.append(result)

        else:
            stack.append(float(token))

    if len(stack) != 1:
        raise ValueError("올바르지 않은 후위 수식입니다.")

    return stack.pop()

if __name__ == "__main__":
    expression = input("수식을 입력하세요: ")

    converter = Infix2Postfix()
    postfix = converter.infix_to_postfix(expression)
    result = evaluate_postfix(postfix)

    print("후위 수식:", postfix)
    print("계산 결과:", result)