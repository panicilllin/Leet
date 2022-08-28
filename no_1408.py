from typing import List


class Solution:
    def stringMaching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda l: len(l))
        res = []
        for i in range(len(words)):
            word = words[i]
            for p_word in words[i + 1:]:
                if word in p_word:
                    res.append(word)
                    break
        return res


if __name__ == "__main__":
    a = Solution()
    b = a.stringMaching(words=["leetcode", "et", "code"])
    print(b)
