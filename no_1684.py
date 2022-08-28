from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        # allowed = list(allowed)
        for word in words:
            flag=True
            for i in word:
                if i not in allowed:
                    flag=False
                    break
            if not flag:
                break
            res+=1
        return res

if __name__ == "__main__":
    a = Solution()
    b = a.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"])
    print(b)
