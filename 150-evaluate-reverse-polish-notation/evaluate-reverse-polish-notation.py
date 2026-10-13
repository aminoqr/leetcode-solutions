class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            "+" : lambda a, b: a + b,
            "-" : lambda a, b: a - b,
            "*" : lambda a, b: a * b,
            "/" : lambda a, b: int(a / b),
        }
        stack = []
        for token in tokens:
            try:
                num = int(token)
                stack.append(token)
            except:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                new_num = operations[token](num1, num2)
                stack.append(new_num)
        
        return int(stack[0])

        