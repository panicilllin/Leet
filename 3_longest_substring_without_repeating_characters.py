"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        left=0
        characters = defaultdict(int)
        res = 0
        for right in range(len(s)):
            if s[right] in characters:
                left =  max(left, characters[s[right]]+1)
            characters[s[right]] = right
            res = max(res, right-left+1)
        return res

class SolutionOld:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        max_length = 0
        for i, _ in enumerate(s):
            tmp_list = []
            max_length = 0
            # print(i,tmp_list,max_length)
            for j, cha in enumerate(s[i:]):
                if cha in tmp_list:
                    ans = max(ans, max_length)
                    print(i,j,tmp_list)
                    break
                else:
                    tmp_list.append(cha)
                    max_length+=1
                ans = max(ans, max_length)
                print(i,j,tmp_list)
                
        ans = max(ans,max_length)
        return ans

if __name__ == "__main__":
    a = Solution()
    b = a.lengthOfLongestSubstring("abcabcbb")
    print(b)
        
 # AC