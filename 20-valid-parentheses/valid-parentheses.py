class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pars = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for par in s:
            if par in pars:
                stack.append(par)
            else:
                if stack == []:
                    return False
                popped = stack.pop()
                if par != pars[popped]:
                    return False
        
        return stack == []

        