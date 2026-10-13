class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in "+-*/":
                num2 = stack.pop()
                num1 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                else:
                    num = num1 / num2
                    if num > 0:
                        stack.append(floor(num))
                    else:
                        stack.append(ceil(num))
            else:
                stack.append(int(token))
        
        return int(stack[0])

        