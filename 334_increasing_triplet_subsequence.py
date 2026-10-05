
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if nums[j]> nums[i]:
                    for k in range(j+1, len(nums)):
                        if nums[k] > nums[j]:
                            return True
        return False
                
            

if __name__ == "__main__":
    a = Solution()
    b = a.increasingTriplet(nums = [1,2,3,4,5])
    print(b)