/*
347. Top K Frequent Elements
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
*/

import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;

class Solution {
    
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq_dict = new HashMap<>();
        for (int num : nums) {
            int count = freq_dict.getOrDefault(num,0);
            count +=1;
            freq_dict.put(num, count);
        }
        
        // 1. Create buckets where the index represents the frequency
        List<Integer>[] buckets = new List[nums.length + 1];
        for (int key : freq_dict.keySet()) {
            int freq = freq_dict.get(key);
            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(key);
        }
        
        // 2. Iterate backwards to get the top k frequent elements
        int[] res = new int[k];
        int index = 0;
        for (int i = buckets.length - 1; i >= 0 && index < k; i--) {
            if (buckets[i] != null) {
                for (int num : buckets[i]) {
                    res[index++] = num;
                    if (index == k) break; // Break out if we reached k elements
                }
            }
        }
        return res;
    }
}