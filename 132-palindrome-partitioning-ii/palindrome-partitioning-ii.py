class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        memo = {}

        def is_palindrome(substr: str) -> bool:
            return substr == substr[::-1]
        
        def helper(i: int) -> int:
            if i == n:
                return -1
            
            if i in memo:
                return memo[i]
            
            min_cost = 10**99

            for j in range(i, n):
                if is_palindrome(s[i:j+1]):
                    cost = 1 + helper(j+1)
                    min_cost = min(min_cost, cost)
            
            memo[i] = min_cost
            return min_cost
        
        return helper(0)

