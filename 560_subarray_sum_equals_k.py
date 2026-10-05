"""
560. Subarray Sum Equals K
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""

from typing import List

# Sum(i,j) = prefixSum(j) - prefixSum(i-1) = k
# prefixSum(i-1) = prefixSum(j) - k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        # Hash map to store the frequency of prefix sums.
        # Initialize with {0: 1}. This is crucial! 
        # It represents a prefix sum of 0 occurring once (before any elements are processed).
        # This allows us to count subarrays that start from index 0.
        prefix_map = {0: 1}
        
        for num in nums:
            current_sum += num
            
            # Key Logic:
            # We want to find a subarray ending at the current position with sum k.
            # Formula: subarray_sum = current_prefix_sum - previous_prefix_sum
            # We want: k = current_sum - previous_prefix_sum
            # So look for: previous_prefix_sum = current_sum - k
            
            # If (current_sum - k) is in our map, it means there are one or more
            # previous indices where the prefix sum was equal to that value.
            # Each such occurrence represents a valid start point for our subarray.
            if (current_sum - k) in prefix_map:
                count += prefix_map[current_sum - k]
            
            # Record the current prefix sum so future iterations can look back at it.
            prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
            
        return count
        
# Example Walkthrough:
# Input: nums = [1, -1, 1, 1, 1], k = 2
#
# 1. Init: map={0:1}, sum=0, count=0
# 2. num=1: sum=1. Target (1-2)=-1. Map has no -1. Map={0:1, 1:1}
# 3. num=-1: sum=0. Target (0-2)=-2. Map has no -2. Map={0:2, 1:1}
# 4. num=1: sum=1. Target (1-2)=-1. Map has no -1. Map={0:2, 1:2}
# 5. num=1: sum=2. Target (2-2)=0. Map has 0 (val=2). Count+=2 (Total 2). Map={0:2, 1:2, 2:1}
# 6. num=1: sum=3. Target (3-2)=1. Map has 1 (val=2). Count+=2 (Total 4). Map={..., 3:1}
# Result: 4

if __name__ == '__main__':
    a = Solution()
    b = a.subarraySum(nums=[1, -1, 1, 1, 1], k=2)
    print(b)