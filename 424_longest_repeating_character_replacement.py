"""
424. Longest Repeating Character Replacement
Medium
Topics
premium lock icon
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 10^5
s consists of only uppercase English letters.
0 <= k <= s.length
"""
import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        alphabet = [0] * 26
        res = 0
        for right in range(len(s)):
            alphabet[ord(s[right]) - ord('A')] += 1
            max_freq = max(alphabet)
            window_len = right - left + 1
            if window_len - max_freq > k:
                alphabet[ord(s[left]) - ord('A')] -= 1
                left += 1
                window_len -=1
            res = max(window_len, res)
        return res

        
        
            
            
            


if __name__ == "__main__":
    a = Solution()
    b = a.characterReplacement(s = "ABAB", k = 0)
    print(b)
            