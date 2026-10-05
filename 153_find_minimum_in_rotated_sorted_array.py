class Solution:
    def findMin(self, nums: List[int]) -> int:
        l =- 1
        r = len(nums)
        while l+1 < r:
            m = (l+r)//2
            if nums[l]<nums[m]:
                l=m
            else:
                r=m
        return min(nums[l],nums[r])

# AC