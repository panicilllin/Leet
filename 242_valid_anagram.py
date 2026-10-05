'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_dict = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}
        for i in s:
            letter_dict[i] += 1
        for i in t:
            letter_dict[i] -= 1
        for i in letter_dict.values():
            if i != 0:
                return False
        return True


# 2026.10.03
# Leet 242
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wc = [0]*26
        for i in s:
            wc[ord(i)-ord('a')] +=1
        for i in t:
            wc[ord(i)-ord('a')] -=1
        
        for i in range(0,26):
            if wc[i] != 0:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram")) # True
    print(sol.isAnagram("rat", "car")) # False