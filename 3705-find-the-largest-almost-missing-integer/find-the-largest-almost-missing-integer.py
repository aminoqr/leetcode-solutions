class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        res = {}

        for s in range(len(nums)-k+1):
            lst = list(set(nums[s:s+k]))
            for i in lst:
                if i in res:
                    res[i] += 1
                else:
                    res[i] = 1
        
        ans = [i for i in res if res[i] == 1]
        if not ans:
            return -1
        
        ans = sorted(ans, reverse=True)

        return ans[0]
        