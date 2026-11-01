from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # counter = Counter(nums)
        # heap = []
        # for key, value in counter.items():
        #     if len(heap) < k:
        #         heapq.heappush(heap, (value, key))
        #     else:
        #         heapq.heappushpop(heap, (value, key))
        # return [pair[1] for pair in heap]

        counter = Counter(nums)
        freq_map = [[] for _ in range(len(nums) + 1)]
        ans = []
        for num, count in counter.items():
            freq_map[count].append(num)
        
        for i in range(len(nums), -1, -1):
            if freq_map[i] != []:
                ans.extend(freq_map[i])
                if len(ans) == k:
                    return ans