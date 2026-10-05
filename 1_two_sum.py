'''
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''
# 2026.10.05
class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num1 in enumerate(nums[:-1]):
            for j, num2 in enumerate(nums[i+1:], start=i+1):
                print(f"i:{i} -> {num1}; j:{j} -> {num2}")
                if num1 + num2 == target:
                    return [i,j]
        return []

# 2026.10.05
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [i, hash_map[target - num]]
            hash_map[num] = i
        return []

if __name__ == '__main__':
    s = Solution()
    nums = [2,7,11,15]
    target = 9
    print(s.twoSum(nums, target))