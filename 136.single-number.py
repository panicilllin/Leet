#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (70.60%)
# Likes:    13288
# Dislikes: 511
# Total Accepted:    2.1M
# Total Submissions: 3M
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one.
# 
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
# 
# 
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
# Input: nums = [1]
# Output: 1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# Each element in the array appears twice except for one element which appears
# only once.
# 
# 
#

# @lc code=start
from typing import List, Tuple
import heapq
class Solution:

    def searchInsert(self, nums: List[int], target: int) -> Tuple[bool, int]:
        # print(nums,target)
        if not nums:
            return False, 0
        if target < nums[0]:
            return False, 0
        if target == nums[0]:
            return True, 0
        if target == nums[-1]:
            return True, len(nums)-1
        if target > nums[-1]:
            return False, len(nums)
        
        start = 0
        end = len(nums)-1
        middle = (end-start)//2 + start
        while middle > start and middle < end:
            if nums[middle] == target:
                return True, middle
            elif nums[middle] > target:
                end = middle
                middle = (end-start)//2 + start
            else:
                start = middle
                middle = (end-start)//2 + start
        if nums[middle] > target:
            return False, middle
        else:
            return False, middle+1


    def singleNumber(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            exist, idx = self.searchInsert(res,i)
            if not exist:
                res.insert(idx, i)
            else:
                del res[idx]
        return res[0]
    
# @lc code=end


if __name__ =="__main__":
    a = Solution()
    b = a.singleNumber(nums = [1,0,1])
    print(b)
