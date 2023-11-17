#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode.cn/problems/single-number/description/
#
# algorithms
# Easy (72.26%)
# Likes:    2784
# Dislikes: 0
# Total Accepted:    871.4K
# Total Submissions: 1.2M
# Testcase Example:  '[2,2,1]'
#
# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 
# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
# 
# 
# 
# 
# 
# 示例 1 ：
# 
# 
# 输入：nums = [2,2,1]
# 输出：1
# 
# 
# 示例 2 ：
# 
# 
# 输入：nums = [4,1,2,1,2]
# 输出：4
# 
# 
# 示例 3 ：
# 
# 
# 输入：nums = [1]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# 除了某个元素只出现一次以外，其余每个元素均出现两次。
# 
# 
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
