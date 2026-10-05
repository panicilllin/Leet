import copy
from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        if len(pattern) == 1:
            return [i for i in words if len(i) == 1]

        pattern_map = self.get_map(pattern)
        res = []
        for i in range(len(words)):
            if len(words[i]) != len(pattern):
                continue
            word_map = self.get_map(words[i])
            # print(f"word={words[i]},pattern={pattern_map},words={word_map}")
            if (word_map) != pattern_map:
                continue
            res.append(words[i])
        return res

    def get_map(self,pattern):
        pattern_map = {}
        for i in range(len(pattern)):
            letter = pattern[i]
            if pattern_map.get(letter):
                pattern_map[letter].append(i)
            else:
                pattern_map[letter] = [i]
        res = [pattern_map[i] for i in pattern_map]
        res.sort(key=lambda nums: (len(nums),nums[0]))
        return res

if __name__ == "__main__":
    a = Solution()
    b = a.findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern="abb")
    print(b)

# AC