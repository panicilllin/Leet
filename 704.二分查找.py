#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
# @lc code=start


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 1:
            return -1
        if target < nums[0] or target > nums[-1]:
            return -1
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums)-1
        start = 0
        end = len(nums)-1
        mid = (end-start)//2 + start
        while mid > start and mid < end:
            # print(start, mid, end, '---', nums[mid])
            if target > nums[mid]:
                start = mid
                mid = (end-start)//2 + start
            elif target < nums[mid]:
                end = mid
                mid = (end-start)//2 + start
            else:
                return mid
        return -1
        
# @lc code=end

if __name__ == "__main__":
    a = Solution()
    b = a.search(nums = [-1,0,3,5,9,12], target = 9)
    print(b)