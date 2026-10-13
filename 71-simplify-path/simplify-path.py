class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split("/")
        stack = []
        print(lst)
        lst = [x for x in lst if x and x != "."]
        for c in lst:
            if c == "..":
                if not stack:
                    continue
                stack.pop()
            else:
                stack.append(c)
        ans = "/".join(stack)
        ans = "/" + ans
        return ans
            
        