from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        min_after=[None]* len(nums)
        max_before=[None] * len(nums)
        min_after[-1] = nums[-1]
        max_before[0] = nums[0]
        for i in range(len(nums)-2,-1,-1):
            min_after[i] =min(min_after[i+1],nums[i])

        for i in range(1,len(nums)):
            max_before[i] = max(max_before[i-1],nums[i])
        print(nums)
        print(min_after)
        print(max_before)

        for i in range(len(nums)-1):
            if max_before[i] <= min_after[i+1]:
                return i+1
        return -1
        

if __name__ == "__main__":
    a = Solution()
    b = a.partitionDisjoint([1,1,1,1])
    print(b)
    
# AC