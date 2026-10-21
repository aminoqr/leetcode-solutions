class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = defaultdict(int)
        hash_map[0] = 1
        prefix_sum = 0
        ans = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in hash_map:
                ans += hash_map[prefix_sum - k]

            hash_map[prefix_sum] += 1
        
        print(hash_map)
        return ans