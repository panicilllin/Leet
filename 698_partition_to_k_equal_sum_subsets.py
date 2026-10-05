from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        all_nums = sum(nums)
        if all_nums % k != 0:
            return False
        avg = all_nums//k
        nums.sort()
        if nums[-1] > avg:
            return False
        for i in range(len(nums)-1,-1,-1):
            leck = avg-nums[i]
            if leck == 0:
                continue
            for j in range(i):
                if 
            
        
        