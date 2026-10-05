"""
49. Group Anagrams
Medium
Topics
premium lock icon
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from typing import List
from collections import defaultdict

class Solution1:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # alphabet = [0]*26
        alphadict={}
        for i, str in enumerate(strs):
            alphalist = [0]*26
            for k in str:
                alphalist[ord(k)-ord('a')] +=1
            # print(alphalist)
            alpha_key = "% s" % alphalist
            if not alphadict.get(alpha_key):
                alphadict[alpha_key] = []
            alphadict[alpha_key].append(str)
        ans = []
        for value in alphadict.values():
            ans.append(value)
        return ans

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for word in strs:
            alpha_list = [0] * 26
            for letter in word:
                alpha_list[ord(letter) - ord('a')] += 1
            alpha_list = tuple(alpha_list)
            if alpha_list in anagram_dict:
                anagram_dict[alpha_list].append(word)
            else:
                anagram_dict[alpha_list] = [word]
        return list(anagram_dict.values())


class Solution3:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        base = ord('a')
        for word in strs:
            alpha_list = [0] * 26
            for letter in word:
                alpha_list[ord(letter) - base] += 1
            anagram_dict[tuple(alpha_list)].append(word)
        return list(anagram_dict.values())

# 2026.10.03
# Leet 49
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        wc_dict = defaultdict(list)
        for s in strs:
            wc = [0]*26
            for i in s:
                wc[ord(i) - ord('a')] += 1
            wc_key = '_'.join(str(i) for i in wc)
            wc_dict[wc_key].append(s)
        res = []
        for v in wc_dict.values():
            res.append(v)
        return res
if __name__ == "__main__":
    a = Solution()
    b = a.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"])
    print(b)
