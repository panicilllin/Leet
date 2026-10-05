class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        step=0
        min_step = nums[0]
        for i,num in enumerate(nums):
            step +=num
            min_step = min(step,min_step)
        if min_step>=0:
            return 1
        return 1-min_step
# AC