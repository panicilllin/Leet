from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums)-1
        if target > nums[-1]:
            return len(nums)
        
        start = 0
        end = len(nums)-1
        middle = (end-start)//2 + start
        while middle > start and middle < end:
            print(nums[start],nums[middle],nums[end])
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle
                middle = (end-start)//2 + start
            else:
                start = middle
                middle = (end-start)//2 + start
        if nums[middle] > target:
            return middle
        else:
            return middle+1
            

if __name__ == '__main__':
    a = Solution()
    b = a.searchInsert([-3,-1,3,90], 0)
    print(b)