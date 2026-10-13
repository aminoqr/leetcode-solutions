class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ""
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                curr = ""
                while stack and stack[-1] != "[":
                    curr = stack.pop() + curr
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                curr = int(num) * curr
                stack.append(curr)
        
        return "".join(stack)
