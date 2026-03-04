class Solution:
    def isValid(self, s: str) -> bool:
        op = ["[", "(", "{"]
        cl = ["]", ")", "}"]
        bracets = []
        for c in s:
            if c in op:
                bracets.append(c)
            elif c in cl:
                if not bracets:
                    return False
                if c == "]" and bracets[-1] == "[":
                    bracets.pop()
                elif c == ")" and bracets[-1] == "(":
                    bracets.pop()
                elif c == "}" and bracets[-1] == "{":
                    bracets.pop()
                else:
                    return False
        return bracets == []
