class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort()
        n = len(nums)

        # '-4' -1 -1 0 1 2 5 6 9 

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left, right = i+1, n-1

            while left < right:
                summ = nums[i] + nums[left] + nums[right]

                if summ == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1 
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                
                elif summ < 0:
                    left += 1
                else:
                    right -= 1
            
        return answer
            

        

        

        