#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
# https://leetcode.com/problems/combination-sum-iv/description/
#
# algorithms
# Medium (52.26%)
# Likes:    6540
# Dislikes: 608
# Total Accepted:    404.9K
# Total Submissions: 764K
# Testcase Example:  '[1,2,3]\n4'
#
# Given an array of distinct integers nums and a target integer target, return
# the number of possible combinations that add up to target.
# 
# The test cases are generated so that the answer can fit in a 32-bit
# integer.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.
# 
# 
# Example 2:
# 
# 
# Input: nums = [9], target = 3
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 1000
# All the elements of nums are unique.
# 1 <= target <= 1000
# 
# 
# 
# Follow up: What if negative numbers are allowed in the given array? How does
# it change the problem? What limitation we need to add to the question to
# allow negative numbers?
# 
#

# @lc code=start
from typing import List


class Solution0:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(i for i in nums if i <= target)
        # print(nums)
        res=0
        for i in range(len(nums),0,-1):
            # print(i)
            nums = nums[:i]
            this_round = self.cal_num(nums,target)
            res+=this_round
            # print('---------->',nums,'\n',nums[-1],'==',this_round)
        return res
    
    
    def cal_num(self, nums: List[int], target: int) -> int:
        if len(nums)<=1:
            return 0 if(not nums or target%nums[0] != 0) else 1
        # print(nums)
        res=0
        num = nums[-1]
        if num > target:
            res += self.cal_num(nums[:-1],target)
        elif num == target:
            res+=1
            res += self.cal_num(nums[:-1],target)
        else:
            if target%num == 0:
                res+=1
            res += self.cal_num(nums[:-1],target-num)
        # print(f"nums=={nums},tg={target},res=={res}")
        return res

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1,target+1):
            for num in nums:
                if num <= target:
                    dp[i] = dp[i-num]+dp[i]
        return dp[target]
    
if __name__ =='__main__':
    a = Solution()
    b = a.combinationSum4([1,2,3],4)
    print(b)
# @lc code=end

